import ga
import HC
import problem
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
    print(cost_his)
    if final_cost == 0:
        num_succ += 1
    del prob, hc

print('Problem (1): 8-queen problem (n = 8)')     
print('\tAverage Runtime :', np.average(aver_runtime))
print('\tAverage Number of Attacks :', np.average(aver_cost))
print('\tSuccess Rate :', num_succ / num_trails)

# Problem (2): 50-queen problem (n = 50)
aver_cost, aver_runtime, num_succ = [], [], 0
for i in range(num_trails):
    prob = problem.N_QueenProblem(50)
    hc = HC.HC(prob, max_iter=30)
    hc.loop()
    sol, runtime, final_cost, cost_his = hc.result()
    aver_runtime.append(runtime)
    aver_cost.append(final_cost)
    if final_cost == 0:
        num_succ += 1
    del prob, hc

print('Problem (1): 50-queen problem (n = 50)')     
print('\tAverage Runtime :', np.average(aver_runtime))
print('\tAverage Number of Attacks :', np.average(aver_cost))
print('\tSuccess Rate :', num_succ / num_trails)