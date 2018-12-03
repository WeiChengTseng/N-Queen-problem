import environment
import random
import copy
import numpy as np
import time

class N_QueenProblem():
    def __init__(self, n):
        self.env = environment.Environment(n)
        self.size = n
        self.current_state = ()
        self.cost_map = dict({})
        random.seed(time.time())
        return

    def cost(self, state=None):
        '''
        Calculate the cost of a given state.

        Input
        - state: a state of the n-queen problem 
        
        Output
        - total_state: the cost of the state
        '''
        if state is None:
            state = self.current_state

        if state in self.cost_map.keys():
            return self.cost_map[state]
        else:
            total_cost = 0
            grid = np.zeros((self.size, self.size), dtype=int)
            for inx, q in enumerate(state):
                grid[inx, q] = 1
            for i in range(self.size):
                n = np.count_nonzero(grid[i, :])
                if n >= 2:
                    total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))

                n = np.count_nonzero(grid[:, i])
                if n < 2:
                    continue 
                total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))

            for k in range(self.size):
                dia = [grid[i+k, i] for i in range(self.size-k)]
                n = dia.count(1)
                if n >= 2:
                    total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))

            for k in range(1, self.size):
                dia = [grid[i, i+k] for i in range(self.size-k)]
                n = dia.count(1)
                if n >= 2:
                    total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))

            for k in range(self.size):
                dia = [grid[-i-k-1, i] for i in range(self.size-k)]
                n = dia.count(1)
                if n >= 2:
                    total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))

            for k in range(1, self.size):
                dia = [grid[-i-1, i+k] for i in range(self.size-k)]
                n = dia.count(1)
                if n >= 2:
                    total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))

            self.cost_map[state] = int(total_cost)
            return int(total_cost)

    def get_successors(self, state=None):
        successors, combination = [], []
        for i in range(self.size-1):
            for j in range(i+1, self.size):
                combination.append((i, j))
        for com in combination:
            succ = list(copy.deepcopy(state))
            succ[com[0]], succ[com[1]] = succ[com[1]], succ[com[0]]
            successors.append(tuple(succ))
        return successors 

    def show(self):
        self.env.show()
        return

    def random_generate_state(self):
        choice = np.random.choice(self.size, self.size, replace=False)
        return tuple(choice)
        
        state = ()
        for i in range(self.size):
            state += ((i, choice[i]), )
        return state
    
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
    print('cost =', prob.cost())
    # print(len(prob.get_successors()))