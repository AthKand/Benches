# -*- coding: utf-8 -*-
# @Author: ath
# @Date:   2023-03-11 16:41:07
# @Last Modified by:   Atharva Kand

from stable_baselines3 import PPO, TD3, SAC
from sb3_contrib import RecurrentPPO 


ALGOS = {"PPO":PPO, "TD3":TD3, "SAC":SAC, "RPPO":RecurrentPPO} 
ENVS = {"CART": "CartPole-v1", 
		"REACH" :"Reacher-v4",
		"DM_REACH_HARD" : "dm_control/reacher-hard-v0",
		"DM_CART" : "dm_control/cartpole-balance-v0",
		"PUSH" : "Pusher-v4",
		"CHEETAH" : "HalfCheetah-v4"
		}

SAVE_TIMESTEPS = 2000
TOTAL_TIMESTEPS = 1e6
SEED = 0

SAVE_VIDEOS = False
