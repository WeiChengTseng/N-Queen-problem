import matplotlib.pyplot as plt

class Environment():
    def __init__(self, size):
        self.grid = [[None for i in range(size)] for j in range(size)]
        self.size = size
    
    def show(self):
        for i in range(self.size):
            for j in range(self.size):
                print('%4s' % (self.grid[i][j]))
    
        print('-' * 4 * self.size)
    
class Visualization():
    def __init__(self):
        pass