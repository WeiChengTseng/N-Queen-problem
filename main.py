import ga as GA
import HC
import problem_new as problem
import numpy as np
num_trails = 30

# Problem (1): 8-queen problem (n = 8)
aver_cost, aver_runtime, num_succ = [], [], 0
for i in range(num_trails):
    prob = problem.N_QueenProblem(8)
    hc = HC.HC(prob, max_iter=30)
    hc.loop()
    sol, runtime, final_cost, cost_his = hc.result()
    aver_runtime.append(runtime)
    aver_cost.append(final_cost)
    if final_cost == 0:
        num_succ += 1
    del prob, hc

print('Problem (1): 8-queen problem (n = 8)')     
print('    Hill Climbing')  
print('\tAverage Runtime :', np.average(aver_runtime))
print('\tAverage Number of Attacks :', np.average(aver_cost))
print('\tSuccess Rate :', num_succ / num_trails)

aver_cost, aver_runtime, num_succ = [], [], 0
for i in range(num_trails):
    prob = problem.N_QueenProblem(8)
    ga = GA.GA(prob, max_iter=30)
    ga.loop()
    sol, runtime, final_cost, cost_his = ga.result()
    aver_runtime.append(runtime)
    aver_cost.append(final_cost)
    if final_cost == 0:
        num_succ += 1
    del prob, ga

print('    Genetic Algorithm')    
print('\tAverage Runtime :', np.average(aver_runtime))
print('\tAverage Number of Attacks :', np.average(aver_cost))
print('\tSuccess Rate :', num_succ / num_trails)

# exit(0)
# Problem (2): 50-queen problem (n = 50)
aver_cost, aver_runtime, num_succ = [], [], 0
for i in range(num_trails):
    prob = problem.N_QueenProblem(50)
    hc = HC.HC(prob, max_iter=100)
    hc.loop()
    sol, runtime, final_cost, cost_his = hc.result()
    aver_runtime.append(runtime)
    aver_cost.append(final_cost)
    if final_cost == 0:
        num_succ += 1
    del prob, hc

print('Problem (2): 50-queen problem (n = 50)')    
print('    Hill Climbing')   
print('\tAverage Runtime :', np.average(aver_runtime))
print('\tAverage Number of Attacks :', np.average(aver_cost))
print('\tSuccess Rate :', num_succ / num_trails)

aver_cost, aver_runtime, num_succ = [], [], 0
for i in range(num_trails):
    prob = problem.N_QueenProblem(50)
    ga = GA.GA(prob, population_size=100, max_iter=120)
    ga.loop()
    sol, runtime, final_cost, cost_his = ga.result()
    aver_runtime.append(runtime)
    aver_cost.append(final_cost)
    if final_cost == 0:
        num_succ += 1
    del prob, ga

print('    Genetic Algorithm')    
print('\tAverage Runtime :', np.average(aver_runtime))
print('\tAverage Number of Attacks :', np.average(aver_cost))
print('\tSuccess Rate :', num_succ / num_trails)