import ga as GA
import HC
import problem_new as problem
import matplotlib.pyplot as plt
import numpy as np
import tqdm

def statics(cost_his):
    max_len = max(list(map(len, cost_his)))
    cost_his_t = []
    for i in range(max_len):
        tmp = []
        for his in cost_his:
            if len(his) > i:
                tmp.append(his[i])
        cost_his_t.append(tmp)

    cost_std = list(map(np.std, cost_his_t))
    cost_avg = list(map(np.average, cost_his_t))
    return np.array(cost_avg), np.array(cost_std)

num_trails = 30
N = 50
max_iter = 160
sel_mode = 'TS'
population_size = 500

ga_cost = []
aver_cost, aver_runtime, num_succ = [], [], 0
for i in tqdm.tqdm(range(num_trails)):
    prob = problem.N_QueenProblem(N)
    ga = GA.GA(prob, max_iter=max_iter, mut_mode='SWAP', sel_mode=sel_mode, population_size=population_size)
    ga.loop()
    sol, runtime, final_cost, cost_his = ga.result()
    aver_runtime.append(runtime)
    aver_cost.append(final_cost)
    if final_cost == 0:
        num_succ += 1
    del prob, ga
    ga_cost.append(cost_his)

print('    Genetic Algorithm')    
print('\tAverage Runtime :', np.average(aver_runtime))
print('\tAverage Number of Attacks :', np.average(aver_cost))
print('\tSuccess Rate :', num_succ / num_trails)
ga_avg, ga_std = statics(ga_cost)
x_range = np.arange(len(ga_avg))
plt.rcParams["figure.figsize"] = [8, 4.5]
plt.plot(x_range, ga_avg, label='Genetic Algorithm (Swap Mutation)')
plt.fill_between(x_range, ga_avg + ga_std, ga_avg - ga_std, alpha=0.15)


ga_cost = []
aver_cost, aver_runtime, num_succ = [], [], 0
for i in tqdm.tqdm(range(num_trails)):
    prob = problem.N_QueenProblem(N)
    ga = GA.GA(prob, max_iter=max_iter, mut_mode='SCRAMBLE', sel_mode=sel_mode, population_size=population_size)
    ga.loop()
    sol, runtime, final_cost, cost_his = ga.result()
    aver_runtime.append(runtime)
    aver_cost.append(final_cost)
    if final_cost == 0:
        num_succ += 1
    del prob, ga
    ga_cost.append(cost_his)

print('    Genetic Algorithm')    
print('\tAverage Runtime :', np.average(aver_runtime))
print('\tAverage Number of Attacks :', np.average(aver_cost))
print('\tSuccess Rate :', num_succ / num_trails)
ga_avg, ga_std = statics(ga_cost)
x_range = np.arange(len(ga_avg))
plt.plot(x_range, ga_avg, label='Genetic Algorithm (Scramble Mutation)')
plt.fill_between(x_range, ga_avg + ga_std, ga_avg - ga_std, alpha=0.15)


ga_cost = []
aver_cost, aver_runtime, num_succ = [], [], 0
for i in tqdm.tqdm(range(num_trails)):
    prob = problem.N_QueenProblem(N)
    ga = GA.GA(prob, max_iter=max_iter, mut_mode='INVERSION', sel_mode=sel_mode, population_size=population_size)
    ga.loop()
    sol, runtime, final_cost, cost_his = ga.result()
    aver_runtime.append(runtime)
    aver_cost.append(final_cost)
    if final_cost == 0:
        num_succ += 1
    del prob, ga
    ga_cost.append(cost_his)

print('    Genetic Algorithm')    
print('\tAverage Runtime :', np.average(aver_runtime))
print('\tAverage Number of Attacks :', np.average(aver_cost))
print('\tSuccess Rate :', num_succ / num_trails)
ga_avg, ga_std = statics(ga_cost)
x_range = np.arange(len(ga_avg))
plt.plot(x_range, ga_avg, label='Genetic Algorithm (Inversion Mutation)')
plt.fill_between(x_range, ga_avg + ga_std, ga_avg - ga_std, alpha=0.15)


ga_cost = []
aver_cost, aver_runtime, num_succ = [], [], 0
for i in tqdm.tqdm(range(num_trails)):
    prob = problem.N_QueenProblem(N)
    ga = GA.GA(prob, max_iter=max_iter, mut_mode='INSERT', sel_mode=sel_mode, population_size=population_size)
    ga.loop()
    sol, runtime, final_cost, cost_his = ga.result()
    aver_runtime.append(runtime)
    aver_cost.append(final_cost)
    if final_cost == 0:
        num_succ += 1
    del prob, ga
    ga_cost.append(cost_his)

print('    Genetic Algorithm')    
print('\tAverage Runtime :', np.average(aver_runtime))
print('\tAverage Number of Attacks :', np.average(aver_cost))
print('\tSuccess Rate :', num_succ / num_trails)
ga_avg, ga_std = statics(ga_cost)
x_range = np.arange(len(ga_avg))
plt.plot(x_range, ga_avg, label='Genetic Algorithm (Insert Mutation)')
plt.fill_between(x_range, ga_avg + ga_std, ga_avg - ga_std, alpha=0.15)

plt.xlabel('iterations')
plt.ylabel('the number of attacks')
plt.title('Comparison for Different Methods for {}-Queen Problem'.format(N))
plt.legend()
plt.grid()
# plt.yscale('log')
plt.savefig('./result/GA-compare_{}.png'.format(sel_mode), dpi=500)