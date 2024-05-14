#Source: https://stackoverflow.com/questions/75261563/gym-0-21-stable-baseline3-typeerror-tuple-indices-must-be-integers-or-slices
import gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv

env = DummyVecEnv([lambda: gym.make("gym_envs:gym_envs/GridWorld-v0")])

model = PPO("MultiInputPolicy", env, verbose=1)
model.learn(total_timesteps=1000)  # TypeError: tuple indices must be integers or slices, not str