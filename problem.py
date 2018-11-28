import environment
import random
import copy
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

    def cost(self, state):
        total_cost = 0
        grid = [[None for i in range(self.size)] for j in range(self.size)]
        for q in state:
            grid[q[1], q[0]] = 'Q'
        for i in range(self.size):
            n = grid[i, :].count('Q')
            if n >= 2:
                total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))

            n = grid[:, i].count('Q')
            if n < 2:
                continue 
            total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))

        n = [grid[i, i] for i in self.size].count('Q')
        if n >= 2:
            total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))
        n = [grid[-i, i] for i in self.size].count('Q')
        if n >= 2:
            total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))
        return total_cost
    
    def get_successors(self, state, successors=[], col=0):
        # recursive

        for i in range(self.size):
            avai = list(range(self.size)).remove(state[i][1])
            for j in avai:
                succ = copy.deepcopy(state)
                succ[i][1] = avai[j]
                successors.append(succ)
            
        return successors

    def _random_generate(self):
        for i in range(self.size):
            rand = random.randint(0, self.size-1)
            self.current_state.append((i, rand))
            self.env.grid[rand, i] = 'Q' 
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
    print(prob._combination(1))