import ga
import HC
import problem
import numpy as np
num_trails = 30

# Problem (1): For the 8-queen problem (n = 8)
prob = problem.N_QueenProblem(8)
hc = HC.HC(prob, max_iter=30)
aver_cost, aver_runtime, num_succ = [], [], 0
for i in range(num_trails):
    hc.loop()
    sol, runtime, final_cost, cost_his = hc.result()
    aver_runtime.append(runtime)
    aver_cost.append(final_cost)
    if final_cost == 0:
        num_succ += 1
    hc.re_initi()
print('Average Runtime :', np.average(aver_runtime))
print('Average Number of Attacks :', np.average(aver_cost))
print('Success Rate :', num_succ / num_trails)