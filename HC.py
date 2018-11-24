import numpy as np

class HC():
    def __init__(self, problem):
        self.prob = problem
        self.current_state = None
        return
    
    def loop(self):
        while True:
            successors = self.prob.get_successors(self.current_state)
            costs = [self.prob.cost(i) for i in successors]
            neighbor = successors[np.argmin(costs)]

            if costs[neighbor] > self.prob.cost(self.current_state):
                return self.current_state
            self.current_state = neighbor

    def result(self, visualization=False):
        print(self.current_state)
        return

    
