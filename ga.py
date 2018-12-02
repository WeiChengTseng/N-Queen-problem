import numpy as np

class GA():
    def __init__(self, problem, mutation_rate=0.1,population_size=50, max_iter=100, fitness_fn=None):
        self.prob = problem
        self.current_state = problem.random_generate_state()
        self.max_iter = max_iter
        self.runtime = 0
        self.population_size = population_size
        self.population = []
        self.m_rate = mutation_rate
        self.fitness_fn = fitness_fn
        self.parent_size = int(population_size * 0.5)
        return

    def selection(self, i):
        if i == 0:
            self.fitness = np.array(list(map(self.fitness_fn, self.population)))
            self.fitness /= np.sum(self.fitness)
        individual_idx = np.random.choice(self.population_size, p=self.fitness)
        individual = self.population[individual_idx]

        return individual

    def reproduce(self, x, y):
        # order crossover (CX)
        choice = np.random.choice(len(x), 2, replace=False)
        s, e = min(choice), max(choice)
        c1, c2 = np.zeros((2, len(x)), dtype=int)
        c1[s:e+1], c2[s:e+1] = x[s:e+1], y[s:e+1]
        fix = map(lambda x: x % len(x), range(e+1, e+len(x)-(e-s)))
        return (tuple(c1), tuple(c2))

    def mutate(self, child):

        return

    def survive(self):

        return

    def loop(self):
        while True:
            for i in range(self.parent_size):
                x, y = self.selection(i), self.selection(i)
                child = self.reproduce(x, y)
                for i in [0, 1]:
                    if np.random.random_sample < self.m_rate:
                        child[i] = self.mutate(child[i])
                self.population.append(child)

            self.survive()
        return

    def _random_generate_population(self):
        for i in range(self.population_size):
            self.population.append(self.prob.random_generate_state())
        return

if __name__ == '__main__':
    x = (0, 1, 3, 2, 4)
    y = (0, 1, 4, 3, 2)