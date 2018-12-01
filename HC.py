import numpy as np
import problem
import matplotlib.pyplot as plt
import time

class HC():
    def __init__(self, problem, max_iter=100):
        self.prob = problem
        self.current_state = self.prob.current_state
        self.max_iter = max_iter
        self.cost_history = []
        self.runtime = 0
        return
    
    def loop(self):
        num_iter = 0
        start_time = time.time()
        while True:
            self.cost_history.append(self.prob.cost(self.current_state))
            successors = self.prob.get_successors(self.current_state)
            costs = [self.prob.cost(i) for i in successors]
            neighbor_idx = np.argmin(costs)
            neighbor = successors[neighbor_idx]
            # print(costs[neighbor_idx])

            if costs[neighbor_idx] >= self.prob.cost(self.current_state):
                break
            self.current_state = neighbor
            num_iter += 1
            if num_iter >= self.max_iter:
                break
        self.runtime = time.time() - start_time
        # print(self.runtime)
        # print(self.cost_history[-1])
        return

    def result(self, visualization=False):
        # print(self.current_state)
        if visualization:
            plt.plot(range(len(self.cost_history)), self.cost_history, 'o-')
            plt.xlabel('the number of iterations')
            plt.ylabel('the number of attacks')
            plt.show()
        return self.current_state, self.runtime, self.prob.cost(self.current_state), self.cost_history

    def re_initi(self):
        self.__init__(self.prob)
        return

if __name__ == '__main__':
    prob = problem.N_QueenProblem(8)
    hc = HC(prob, max_iter=30)
    hc.loop()
    hc.result(visualization=True)
