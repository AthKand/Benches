# -*- coding: utf-8 -*-
# @Author: ath

'''

TO-DO : 
1. Input all experiment variables with a config file rather than CLI args
2. Find a better way to deal with env wrappers
3. Integrate Vid Writer into new code structure
4. Find a better way to do CallBacks -- esp useful for custom algos 

'''

import os
import sys
import numpy as np
import importlib

from utils.wrapper import CameraControlWrapper
from utils.video_writer import VidWriter
import wandb
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.callbacks import EvalCallback, CheckpointCallback, BaseCallback

import gymnasium 
sys.modules["gym"] = gymnasium
import gymnasium as gym
from utils.defaults import ALGOS
from utils.defaults import *



class RLExperiment:
    def __init__(self, algo, env_id, policy, save_videos, cam_control, cam_settings, custom_env, custom_algo, experiment_name):
        self.algo = algo
        self.env_id = env_id
        self.policy = policy
        self.save_videos = save_videos
        self.cam_control = cam_control
        self.camera_settings = cam_settings
        self.custom_env = custom_env
        self.custom_algo = custom_algo
        self.experiment_name = experiment_name

        # Set up Weights and Biases
        wandb.init(project="Benchmarks", name=self.experiment_name)

        # WandB logs
        wandb.config.update({
            "Algorithm": self.algo,
            "Environment": self.env_id,
            "Policy": self.policy,
            "Save Videos": self.save_videos,
        })

        # Set up the environment
        self.env = self._setup_env()

        # Set up the RL algorithm
        self.model = self._setup_algo()

    def _setup_env(self):
        # Add camera control if specified
        if self.cam_control is not None:
            env = CameraControlWrapper(gym.make(self.env_id), **self.camera_settings)
        else:
            env = gym.make(self.env_id)
        
        # Add your custom environment here
        if self.custom_env is not None:
            CustomEnv = getattr(importlib.import_module(f"envs.{self.custom_env}"), self.custom_env)
            env = CustomEnv()

        # Wrap the environment with Monitor for automatic logging
        env = Monitor(env, filename=None, allow_early_resets=True)
        env = gym.wrappers.FlattenObservation(env)

        if env.action_space.dtype != 'float32':
          # convert action spaces to float32 cause torch's Linear method requires it. 
          # dm_control converted spaces seem to be float64 
          env.action_space.dtype = np.dtype(np.float32)

        env.reset()

        return env

    def _setup_algo(self):
        # Add custom algorithm here
        if self.custom_algo is not None:
            CustomAlgo = getattr(importlib.import_module(f"algos.{self.custom_algo}"), self.custom_algo)
            model = CustomAlgo(self.env)
        else:
            model_class = ALGOS[self.algo]
            model = model_class(self.policy, self.env, verbose=1)

        return model

    def _setup_callbacks(self):
        # Unused
        # Set up the evaluation callback
        eval_callback = EvalCallback(self.env,
                                     best_model_save_path='./models/',
                                     log_path='./logs/',
                                     eval_freq=1000,
                                     deterministic=True,
                                     render=self.save_videos)

        # Set up the checkpoint callback
        checkpoint_callback = CheckpointCallback(save_freq=1000, save_path='./models/',
                                                 name_prefix=self.experiment_name)

        # Set up custom callback here
        # custom_callback = YourCustomCallback()

        return [eval_callback, checkpoint_callback]

    def _get_cumulative_reward(self, model):
        # Get cumulatiave reward of latest run 
        obs = self.env.reset()
        done = False
        cumulative_reward = 0

        max_steps = 1000
        step = 0

        while not done and step < max_steps:
          obs = np.expand_dims(obs[0], axis=0)
          action, _ = model.predict(obs)
          action = action[0]
          observation, reward, done, info, _ = self.env.step(action)
          cumulative_reward += reward
          step += 1

        return cumulative_reward

    def run(self):
        # Run the experiment
        # callbacks = self._setup_callbacks()
        # self.model.learn(total_timesteps=total_timesteps, callback=callbacks)
        
        highest_reward = -np.inf

        for i in range(1, int(TOTAL_TIMESTEPS / SAVE_TIMESTEPS) + 1):
            self.model.learn(
                total_timesteps=SAVE_TIMESTEPS,
                reset_num_timesteps=False
            )

            # Get the cumulative reward for this interval
            current_reward = self._get_cumulative_reward(self.model)

            # If the current reward is greater than the highest reward so far, save the model
            if current_reward > highest_reward:
                self.model.save(f"models/{self.algo}/{self.env_id}_best")
                self.highest_reward = current_reward

            #self.save_video(timestep=i)
            self.env.reset()

        # Save the latest model after the loop
        self.model.save(f"models/{self.algo}/{self.env_id}_latest")

