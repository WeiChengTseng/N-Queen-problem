import ga as GA
import HC
import problem_new as problem
import matplotlib.pyplot as plt
import numpy as np
num_trails = 1

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

# Problem (1): 8-queen problem (n = 8)
hc_cost = []
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
    hc_cost.append(cost_his)


print('Problem (1): 8-queen problem (n = 8)')     
print('    Hill Climbing')  
print('\tAverage Runtime :', np.average(aver_runtime))
print('\tAverage Number of Attacks :', np.average(aver_cost))
print('\tSuccess Rate :', num_succ / num_trails)
hc_avg, hc_std = statics(hc_cost)
x_range = np.arange(len(hc_avg))
plt.plot(x_range, hc_avg, label='Hill Climbing')
plt.fill_between(x_range, hc_avg + hc_std, hc_avg - hc_std, alpha=0.15)

ga_cost = []
aver_cost, aver_runtime, num_succ = [], [], 0
for i in range(num_trails):
    prob = problem.N_QueenProblem(8)
    ga = GA.GA(prob, max_iter=25)
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
plt.plot(x_range, ga_avg, label='Genetic Algorithm')
plt.fill_between(x_range, ga_avg + ga_std, ga_avg - ga_std, alpha=0.15)

plt.rcParams["figure.figsize"] = [16, 5]
plt.xlabel('iterations')
plt.ylabel('the number of attacks')
plt.title('Comparison for Different Methods for 8-Queen Problem')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('./result/8-queen.jpg', dpi=500)
plt.show()

# exit(0)
# Problem (2): 50-queen problem (n = 50)
hc_cost = []
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
hc_avg, hc_std = statics(hc_cost)
x_range = np.arange(len(hc_avg))
plt.plot(x_range, hc_avg, label='Hill Climbing')
plt.fill_between(x_range, hc_avg + hc_std, hc_avg - hc_std, alpha=0.15)

ga_cost = []
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
ga_avg, ga_std = statics(ga_cost)
x_range = np.arange(len(ga_avg))
plt.plot(x_range, ga_avg, label='Genetic Algorithm')
plt.fill_between(x_range, ga_avg + ga_std, ga_avg - ga_std, alpha=0.15)

plt.rcParams["figure.figsize"] = [16, 5]
plt.xlabel('iterations')
plt.ylabel('the number of attacks')
plt.title('Comparison for Different Methods for 50-Queen Problem')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('./result/50-queen.jpg', dpi=500)
plt.show()