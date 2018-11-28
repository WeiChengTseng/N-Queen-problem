import environment
import random
import copy
import numpy as np
class N_QueenProblem():
    def __init__(self, n):
        self.env = environment.Environment(n)
        self.size = n
        self.current_state = []
        self._random_generate()
        self.closed = []
        pass
        return

    def move(self, ori, new):
        tmp = self.env.grid[new[0]][new[1]]
        self.env.grid[new[0]][new[1]] = self.env.grid[ori[0]][ori[1]]
        self.env.grid[ori[0]][ori[1]] = tmp
        pass

    def cost(self, state=None):
        # has bug
        if state is None:
            state = self.current_state
        total_cost = 0
        grid = np.zeros((self.size, self.size), dtype=int)
        for q in state:
            grid[q] = 1
        for i in range(self.size):
            n = np.count_nonzero(grid[i, :])
            if n >= 2:
                total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))

            n = np.count_nonzero(grid[:, i])
            if n < 2:
                continue 
            total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))


        n = [grid[i, i] for i in range(self.size)].count(1)
        if n >= 2:
            total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))
        n = [grid[-i, i] for i in range(self.size)].count(1)
        if n >= 2:
            total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))
        return int(total_cost)
    
    def get_successors(self, state=None, successors=[], col=0):
        if state is None:
            state = self.current_state

        for i in range(self.size):
            avai = list(range(self.size))
            avai.remove(state[i][1])
            for j in avai:
                succ = copy.deepcopy(state)
                succ[i] = (succ[i][0], j)
                successors.append(succ)   
        return successors

    def show(self):
        self.env.show()
        return

    def _random_generate(self):
        for i in range(self.size):
            rand = random.randint(0, self.size-1)
            self.current_state.append((i, rand))
            self.env.grid[i][rand] = 1 
        return
    
    def _combination(self, n):
        total_cost = 0
        total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))
        return int(total_cost)

    def _factorial(self, n, com=1):
        if n >= 1:
            return self._factorial(n-1, com*n)
        return com

if __name__ == '__main__':
    prob = N_QueenProblem(8)
    # print(prob._combination(1))
    prob.show()
    print(len(prob.get_successors()))