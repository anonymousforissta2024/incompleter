#Source: https://stackoverflow.com/questions/75261563/gym-0-21-stable-baseline3-typeerror-tuple-indices-must-be-integers-or-slices
import gym
from stable_baselines3 import ppo

env = gym.make("gym_envs:gym_envs/GridWorld-v0")

model = PPO("MultiInputPolicy", env, tensorboard_log="./logs/", verbose=1)
model.learn(total_timesteps=1000)