from collections import deque
import random

class ReplayMemory():
    # create FIFO queue - experience replay
    def __init__(self, maxlen, seed=None): # maxlen = size of replay memory
        self.memory = deque([], maxlen= maxlen)

    def append(self, new_exp):
        self.memory.append(new_exp)

    def sample(self, sample_size):
        return random.sample(self.memory, sample_size)

    # curr buffer size
    def __len__(self): # private function to calculate len of memory
        return len(self.memory)