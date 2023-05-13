# -*- coding: utf-8 -*-
# @Author: ath
# @Date:   2023-03-11 16:49:28
# @Last Modified by:   ath

import gymnasium as gym
from shimmy.registration import DM_CONTROL_SUITE_ENVS

# run this as standalone to initialise dm_control envs as gym environments
if __name__ == "__main__": 
	env_ids = [f"dm_control/{'-'.join(item)}-v0" for item in DM_CONTROL_SUITE_ENVS]
	# print(env_ids)
	print('Environment with wrappers initialised!')
