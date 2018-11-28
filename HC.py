import numpy as np
import problem

class HC():
    def __init__(self, problem):
        self.prob = problem
        self.current_state = None
        return
    
    def loop(self):
        while True:
            successors = self.prob.get_successors(self.current_state)
            costs = [self.prob.cost(i) for i in successors]
            neighbor_idx = np.argmin(costs)
            neighbor = successors[neighbor_idx]
            print(costs[neighbor_idx])

            if costs[neighbor_idx] > self.prob.cost(self.current_state):
                return self.current_state
            self.current_state = neighbor

    def result(self, visualization=False):
        print(self.current_state)
        return

if __name__ == '__main__':
    prob = problem.N_QueenProblem(8)
    hc = HC(prob)
    hc.loop()
