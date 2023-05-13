'''

TO-DO: Input all parameters from config files 


'''
import argparse
from experiment import RLExperiment
import utils.defaults as defaults
from utils.defaults import *

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--algo", default="PPO")                     # algorithm
    parser.add_argument("--env", default = "DM_CART")                # gym(nasium) environment name
    parser.add_argument("--policy", default = "MlpPolicy")           # policy used
    parser.add_argument("--save_videos", default=False)              # Save videos
    parser.add_argument("--cam_control", default=None)               # Camera control settings
    parser.add_argument("--custom_env", default=None)                # Custom environment
    parser.add_argument("--custom_algo", default=None)               # Custom algorithm
    parser.add_argument("--name", default="benchmarks")              # Name of the experiment
    parser.add_argument("--camera_id", default=0)
    parser.add_argument("--azimuth", default=None)
    parser.add_argument("--elevation", default=None)
    parser.add_argument("--distance", default=None)
    parser.add_argument("--mode", default='rgb_array')

    # remove all the CLI stuff -- go for json
    args = parser.parse_args()

    camera_settings = {
        'camera_id': args.camera_id,
        'azimuth': args.azimuth,
        'elevation': args.elevation,
        'distance': args.distance,
        'mode': args.mode
    }


    experiment = RLExperiment(algo=args.algo, env_id=ENVS[args.env], policy=args.policy, 
                              save_videos=args.save_videos, cam_control=args.cam_control,
                              cam_settings=camera_settings, 
                              custom_env=args.custom_env, custom_algo=args.custom_algo, 
                              experiment_name=args.name)
    experiment.run()
