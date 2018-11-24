import environment
import random
class N_QueenProblem():
    def __init__(self, n):
        self.env = environment.Environment(n)
        self.size = n
        self._random_generate()
        pass

    def move(self, ori, new):
        tmp = self.env.grid[new[1]][new[0]]
        self.env.grid[new[1]][new[0]] = self.env.grid[ori[1]][ori[0]]
        self.env.grid[ori[1]][ori[0]] = self.env.grid[new[1]][new[0]]
        pass

    def cost(self):
        total_cost = 0
        for i in range(self.size):
            n = self.env.grid[i, :].find('Q')
            if n >= 2:
                total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))

            n = self.env.grid[:, i].find('Q')
            if n < 2:
                continue 
            total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))

        n = [self.env.grid[i, i] for i in self.size].find('Q')
        if n >= 2:
            total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))
        n = [self.env.grid[-i, i] for i in self.size].find('Q')
        if n >= 2:
            total_cost += self._factorial(n) / (self._factorial(2)*self._factorial(n-2))
        return total_cost
    
    def _random_generate(self):
        for i in range(self.size):
            self.env.grid[random.randint(0, self.size-1), i] = 'Q' 
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