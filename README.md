# Benches

Run RL experiments on a host of environments to benchmark your novel algorithm. 

Now with efficient video recording! 
 

## What's Included?
Continuous control algorithms on environments from various sources all packaged in the manageable easy-to-digest gym wrappers. Experiment tracking on [weights and biases](https://wandb.ai/site). 
### Environments
From the [dm_control suite](https://github.com/deepmind/dm_control) : Reacher-hard, Cartpole-balance

From [Gymnasium MuJoCo](https://gymnasium.farama.org/environments/mujoco/): Reacher-v4, Pusher-v4, HalfCheetah-v4

### Algorithms 
From [stable-baselines3](https://stable-baselines3.readthedocs.io/en/master/) : PPO, SAC, TD3

From [sb3-contrib](https://github.com/Stable-Baselines-Team/stable-baselines3-contrib) : RecurrentPPO


## Usage

Clone repo and initialize your experiments and conda environments with:

```bash
cd ~/path/to/benches
source init.sh
```


Run experiments with 
```bash
source run.sh
```

## Contributing

Pull requests are welcome. 

## License

[MIT](https://choosealicense.com/licenses/mit/)