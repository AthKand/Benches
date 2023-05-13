# -*- coding: utf-8 -*-
# @Author: Atharva Kand
# @Date:   2023-05-02 16:14:53
# @Last Modified by:   Atharva Kand
# @Last Modified time: 2023-05-13 12:04:13

import sys
import numpy as np
import gymnasium 
sys.modules["gym"] = gymnasium
import gymnasium as gym

from dm_control import viewer 

class CameraControlWrapper(gym.Wrapper):
    def __init__(self, env, camera_id=0, azimuth=None, elevation=None, distance=None, mode = "rgb_array"):
        super().__init__(env)
        self.camera_id = camera_id
        self.azimuth = azimuth
        self.elevation = elevation
        self.distance = distance
        self.mode = mode

    def step(self, action):
        observation, reward, done, info, _ = self.env.step(action)
        reshaped_observation = self.reshape_observation(observation)
        return reshaped_observation, reward, done, info, _

    def reset(self, **kwargs):
        observation = self.env.reset(**kwargs)
        self._change_camera_settings()
        reshaped_observation = self.reshape_observation(observation)
        return reshaped_observation

    def reshape_observation(self, observation):
        if isinstance(observation, dict):
            return np.concatenate(list(observation.values()))
        else:
            return observation

    def _get_reshaped_observation(self, observation):
        return self.reshape_observation(observation)

    
    def _change_camera_settings(self):
        # Check if the environment is a gymnasium MuJoCo environment
        if hasattr(self.env.unwrapped, 'mujoco_renderer'):
            cam = self.env.unwrapped.mujoco_renderer._get_viewer(render_mode=self.mode).cam
            if self.azimuth is not None:
                cam.azimuth = self.azimuth
            if self.distance is not None:
                cam.distance = self.distance
            if self.elevation is not None:
                cam.elevation = self.elevation
        
        # Check if the environment is a dm_control environment (wrapped with Shimmy)
        elif hasattr(self.env.unwrapped, '_env') and hasattr(self.env.unwrapped._env, 'physics'):
            cam_id = self.camera_id
            cam = self.env.unwrapped._env.physics.model.cam(cam_id)

            if self.azimuth is not None or self.distance is not None or self.elevation is not None:
                # Convert azimuth, elevation, and distance to Cartesian coordinates
                azimuth_rad = np.radians(self.azimuth or 0)
                elevation_rad = np.radians(self.elevation or 0)
                distance = self.distance or 1

                x = distance * np.cos(elevation_rad) * np.cos(azimuth_rad)
                y = distance * np.cos(elevation_rad) * np.sin(azimuth_rad)
                z = distance * np.sin(elevation_rad)

                # Update the camera position
                cam.pos = np.array([x, y, z])
        else:
            raise ValueError("Unsupported environment type for CameraControlWrapper")


# <MjvCamera
#   azimuth: 90.0
#   distance: 4.0
#   elevation: -45.0
#   fixedcamid: -1
#   lookat: array([ 0.3, -0.6,  0. ])
#   trackbodyid: -1
#   type: 0
# >
