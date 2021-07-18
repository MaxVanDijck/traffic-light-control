import gym
import gym_cityflow
import numpy as np

env = gym.make('gym_cityflow:CityFlow-1x1-LowTraffic-v0')
env.step(1)
env._get_state()