import matplotlib.pyplot as plt
import numpy as np

class Environment():
    def __init__(self, size):
        # self.grid = [[None for i in range(size)] for j in range(size)]
        self.grid = np.zeros((size, size), dtype=int)
        self.size = size
    
    def show(self):
        for i in range(self.size):
            for j in range(self.size):
                print('%5s' % (self.grid[i][j]), end='')
            print()
    
        print('-' * 5 * self.size)
    
class Visualization():
    def __init__(self):
        pass

if __name__ == '__main__':
    env = Environment(4)
    env.show()