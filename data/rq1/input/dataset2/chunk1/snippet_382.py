#Source: https://stackoverflow.com/questions/76555136/torch-set-grad-enabledfalse-typeerror-bool-object-is-not-callable
import torch
import torch.nn as nn
import torch.nn.functional as F
import collections
import random
import math
import numpy as np
import torch.optim as optim
from typing import Type


class CardAgent(nn.Module):
    def __init__(self, params):
        super().__init__()
        self.first_layer = params["first_layer_size"]
        self.second_layer = params["second_layer_size"]
        self.third_layer = params["third_layer_size"]
        self.gamma = params["gamma"]
        self.learning_rate = params["learning_rate"]
        self.memory = collections.deque(maxlen= params["memory_size"])
        self.batch_size = params["batch_size"]
        self.weights_path = params["weights_path"]
        self.optimizer = None
        self.mask = None
        self.network()

    def network(self):
        self.requires_grad_ = False
        self.fc1 = nn.Linear(57, self.first_layer)
        self.fc2 = nn.Linear(self.first_layer, self.second_layer)
        self.fc3 = nn.Linear(self.second_layer, self.third_layer)
        self.fc4 = nn.Linear(self.third_layer, 60)


    def forward(self, observation):
        x = F.relu(self.fc1(observation))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x = F.softmax(self.fc4(x), dim=-1)

        if self.mask is not None:
          print(x)
          return x * self.mask
        return x

    def remember(self, observation, move, reward, next_state, complete):
        self.memory.append((observation, move, reward, next_state, complete))

    def train_memory(self, observation, move, reward, next_state, complete):
        self.train()
        torch.set_grad_enabled = True

        state_tensor = torch.tensor(np.expand_dims(observation, 0), dtype=torch.float32, requires_grad=True)
        next_state_tensor = torch.tensor(np.expand_dims(observation, 0), dtype=torch.float32, requires_grad = True)

        if not complete:
            target = reward + self.gamma * torch.max(self.forward(next_state_tensor[0]))

        output = self.forward(state_tensor)
        target_f = output.clone()
        target_f[0][np.argmax(move)] = target
        target_f.detach()
        self.optimizer.zero_grad()
        loss = F.mse_loss(output, target_f)
        loss.backward()
        self.optimizer.step()

    def replay_exp(self):
        if len(self.memory) > self.batch_size:
            minibatch = random.sample(self.memory, self.batch_size)
        else:
            minibatch = self.memory

        for observation, move, reward, next_state, complete in minibatch:
            self.train_memory(observation, move, reward, next_state, complete)