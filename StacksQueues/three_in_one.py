# pg98: Implement three stacks using a single array.

import unittest

class TripleStack(object):
    def __init__(self, n=100):
        self.data = [None] * (n * 3)
        self.idxs = {1: 0, 2: 1, 3: 2}
        self.stackmax = n

    def push(self, stackNum, value):
        stack_idx = self.idxs[stackNum] + 3
        if stack_idx > self.stackmax:
            self.expand()
        self.idxs[stackNum] = stack_idx
        self.data[stack_idx] = value

    def pop(self, stackNum):
        if self.idxs[stackNum] < 0:
            return None
        stack_idx = self.idxs[stackNum]
        self.idxs[stackNum] -= 3
        return self.data[stack_idx]

    def peek(self, stackNum):
        stack_idx = self.idxs[stackNum]
        return self.data[stack_idx]

    def expand(self):
        self.data += [None] * (self.stackmax * 3)
