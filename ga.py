import numpy as np
import random
import copy
import time
import problem_new as problem
import matplotlib.pyplot as plt

class GA():
    def __init__(self, problem, mutation_rate=0.05, population_size=50, max_iter=100, sel_mode='FPS', mut_mode='SWAP', sur_mode='FB'):
        self.prob = problem
        self.max_iter = max_iter

        self.m_rate = mutation_rate
        self.parent_size = int(population_size * 0.8)
        self.population_size = population_size
        self.population = self._random_generate_population()
        self.fitness_fn = self.prob.cost
        
        self.fitness_history = []
        self.runtime = 0

        self.co_mode = 'OX'
        self.mut_mode = mut_mode
        self.sel_mode = sel_mode
        self.sur_mode = sur_mode
        return

    def selection(self, i):
        # Fitness Selection
        if i == 0:
            self.fitness = 1/(np.array(list(map(self.fitness_fn, self.population)))+1)
            self.fitness /= np.sum(self.fitness)
        if self.sel_mode == 'FPS':
            individual_idx = np.random.choice(self.population_size, p=self.fitness)
            individual = self.population[individual_idx]
        elif self.sel_mode == 'TS':
            ts_size = 20
            candidate_idx = np.random.choice(self.population_size, ts_size)
            fitness = list(map(lambda i: self.fitness_fn(self.population[i]), candidate_idx))
            individual_idx = np.argmin(fitness)
            individual = self.population[individual_idx]

        return individual

    def reproduce(self, x, y):
        # order crossover (OX)
        # print('x =', x)
        # print('y =', y)
        choice = np.random.choice(len(x), 2, replace=False)
        s, e = min(choice), max(choice)
        c1, c2 = np.zeros((2, len(x)), dtype=int)
        c1[s:e+1], c2[s:e+1] = x[s:e+1], y[s:e+1]
        if e - s + 1 == len(x):
            return [tuple(c1), tuple(c2)]

        fix = list(map(lambda i: i % len(x), range(e+1, e+len(x)-(e-s+1)+1)))
        # print(s, e)
        # print('fix =', fix)
        # print(fix)
        acc = fix[0]
        for i in fix:
            while y[acc] in c1[s:e+1]:
                acc = (acc + 1) % len(x)
            c1[i] = y[acc]
            acc = (acc + 1) % len(x)

        acc = fix[0]
        for i in fix:
            while x[acc] in c2[s:e+1]:
                acc = (acc + 1) % len(x)
            c2[i] = x[acc]
            acc = (acc + 1) % len(x)

        return [tuple(c1), tuple(c2)]

    def mutate(self, child):
        mutated = np.array(child)
        if self.mut_mode == 'SWAP':
            combination = []
            for i in range(len(child)-1):
                for j in range(i+1, len(child)):
                    combination.append((i, j))
            random.shuffle(combination)
            com = combination[0]
            mutated[com[0]], mutated[com[1]] = mutated[com[1]], mutated[com[0]]
        else:
            choice = np.random.choice(len(child), 2, replace=False)
            s, e = min(choice), max(choice)
            if self.mut_mode == 'INSERT':
                tmp = mutated[e]
                mutated = np.delete(mutated, e)
                mutated = np.insert(mutated, s, tmp)
            elif self.mut_mode == 'SCRAMBLE':
                scramble = np.random.choice(e-s+1, e-s+1, replace=False)
                mutated[s:e+1] = mutated[s:e+1][scramble]
            elif self.mut_mode == 'INVERSION':
                mutated[s:e+1] = np.flip(mutated[s:e+1], axis=0)
        return tuple(mutated)

    def survive(self):
        if self.sur_mode == 'FB':
            new_idx = np.argsort(list(map(self.fitness_fn, self.population)))[: self.population_size]
            new_population = []
            for i in new_idx:
                new_population.append(self.population[i])
            self.population = new_population
        elif self.sur_mode == 'AB':
            pass
        return

    def loop(self):
        num_iter = 0
        start_time = time.time()
        while True:
            self.fitness_history.append(np.average(list(map(self.fitness_fn, self.population))))
            offspring = []
            for i in range(self.parent_size):
                x, y = self.selection(i), self.selection(i)
                child = self.reproduce(x, y)
                for i in [0, 1]:
                    if np.random.random_sample() < self.m_rate:
                        child[i] = self.mutate(child[i])
                offspring.append(child[0])
                offspring.append(child[1])
            self.population += offspring
            self.survive()
            num_iter += 1
            if num_iter > self.max_iter:
                break
        self.runtime = time.time() - start_time
        return

    def result(self, visualization=False):
        fitness = [self.fitness_fn(i) for i in self.population]
        best_idx = np.argmin(fitness)
        # print(best_idx)
        best_individual = self.population[best_idx]
        # print(fitness[best_idx])
        if visualization:
            plt.plot(range(len(self.fitness_history)), self.fitness_history, '.-')
            plt.xlabel('the number of iterations')
            plt.ylabel('the number of attacks')
            plt.show()
        return best_individual, self.runtime, fitness[best_idx], self.fitness_history

    def _random_generate_population(self):
        population = []
        for i in range(self.population_size):
            population.append(self.prob.random_generate_state())
        return population

if __name__ == '__main__':
    x = (0, 1, 3, 2, 4, 5)
    y = (0, 1, 5, 3, 2, 4)
    
    prob = problem.N_QueenProblem(50)
    ga = GA(prob, population_size=2000, max_iter=200)
    # ga.loop()
    # print(ga.result(True)[2])

    print(ga.reproduce(x, y))
    print(ga.mutate(x))