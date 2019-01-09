#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import math
import sys

# Allows me to import my modules
sys.path.extend(["../../modules", "../"])

e = math.e


# In[2]:


from problem import f, constraints, check_all_constraints, print_all_constraints


# In[3]:


class SA_defaults:
    def __init__(self, is_maximisation=False, s_0=None, t_0=None, neighbourhood_func=None, step_size=None, temp_reduc_func=None, acc_prob_func=None, stop_cond=None, max_i=None, max_epoch=None, tolerance=None):
        self.is_maximisation = is_maximisation
        self.s_0 = s_0
        self.t_0 = t_0
        self.neighbourhood_func = neighbourhood_func
        self.step_size = step_size
        self.temp_reduc_func = temp_reduc_func
        self.acc_prob_func = acc_prob_func
        self.stop_cond = stop_cond
        self.max_i = max_i
        self.max_epoch = max_epoch
        self.tolerance = tolerance

def simulated_annealing(f, DEFAULTS, is_maximisation=None, s_0=None, t_0=None, neighbourhood_func=None, step_size=None, temp_reduc_func=None, acc_prob_func=None, stop_cond=None, max_i=None, max_epoch=None, tolerance=None, print_workings=False):
    # Default parameters
    is_maximisation = DEFAULTS.is_maximisation if is_maximisation is None else is_maximisation
    s_0 = DEFAULTS.s_0 if s_0 is None else s_0
    t_0 = DEFAULTS.t_0 if t_0 is None else t_0
    neighbourhood_func = DEFAULTS.neighbourhood_func if neighbourhood_func is None else neighbourhood_func
    step_size = DEFAULTS.step_size if step_size is None else step_size
    temp_reduc_func = DEFAULTS.temp_reduc_func if temp_reduc_func is None else temp_reduc_func
    acc_prob_func = DEFAULTS.acc_prob_func if acc_prob_func is None else acc_prob_func
    stop_cond = DEFAULTS.stop_cond if stop_cond is None else stop_cond
    max_i = DEFAULTS.max_i if max_i is None else max_i
    max_epoch = DEFAULTS.max_epoch if max_epoch is None else max_epoch
    tolerance = DEFAULTS.tolerance if tolerance is None else tolerance
    
    # Sets the initial value of s_n (when n = 0)
    solution = {k: v for k, v in s_0.items()}
    # Sets the initial value of s_n-1 (not used for the first iteration of the outer loop)
    prev_solution = {k: v for k, v in s_0.items()}
    # The current temperature
    temperature = t_0
    
    # The iterations of the outer (while) loop.
    iteration_counter = 0
    step_array = []
    while (iteration_counter == 0 or not stop_cond(iteration_counter, max_i, solution, prev_solution, tolerance)):
        if (not check_all_constraints(solution, constraints, print_workings)): 
            if (iteration_counter > 0):
                solution = {k: v for k, v in step_array[-1][0].items()}
                temperature = step_array[-1][1]
                step_array = step_array[:-1]
            if (iteration_counter == 0):
                solution = False
            break
        if (print_workings == True):
            print("--------------------------------------------------------------------------------------------\ns_{}: {}".format(iteration_counter, {k: round(v, 3) for k, v in solution.items()}))
        prev_solution = {k: v for k, v in solution.items()}
        step_array.append((prev_solution, temperature))
        for epoch in range(1, max_epoch+1):
            neighbourhood = neighbourhood_func(solution, step_size)
            possible_solution = neighbourhood[random.randrange(
                0, len(neighbourhood))]
            solution_eval_diff = f(possible_solution) - f(solution)
            # If the difference between the possible solution (solution picked in the current epoch) and the solution (the solution of the current iteration of epochs) when put through the acceptance probablity function, is greater than random noise then pick it.
            accepted = solution_eval_diff > 0 if is_maximisation else solution_eval_diff < 0 
            if (accepted or acc_prob_func(
                    solution_eval_diff, temperature) > random.random()):
                # Set a new value of solution
                solution = {k: v for k, v in possible_solution.items()}
                accepted = True
            if (print_workings == True):
                print("Epoch: {}\ts: {}    \tt: {}\tAccepted: {}\tDiff: {}".format(epoch, {k: round(v, 3) for k, v in possible_solution.items()}, round(temperature, 3), accepted, round(solution_eval_diff, 3)))
        # Reduce the temperature and increment the iteration counter
        temperature = temp_reduc_func(temperature)
        iteration_counter += 1
    if (iteration_counter > 0):
        step_array.append(({k: v for k, v in solution.items()}, temperature))
    return (step_array, solution)


# In[4]:


s_0 = {"x1": 0, "x2": 0, "x3": 0, "x4": 0}
t_0 = 5.0
step_size = 0.1
max_i = 50
max_epoch = 8
tolerance = 0.1

# ±x1 or ±x2 or ±x3 or ±x4
def neighbourhood_func(s, step_size):
    neighbourhood = []
    keys = s.keys()
    for i in range(len(keys)*2):
        sign = 1 if i < 4 else -1
        key = list(keys)[i % 4]
        neighbour = {k: v for k, v in s.items()}
        neighbour[key] += sign*step_size
        neighbourhood.append(neighbour)
    return neighbourhood

def temp_reduc_func(x):
    return float(0.75*x)

def acc_prob_func(diff, temperature):
    return float(e**(-abs(diff)/temperature))

def stop_cond(iteration_counter=None, max_i=None, solution=None, prev_solution=None, tolerance=None):
    if (iteration_counter > 0):
        if (iteration_counter >= max_i):
            return True
    return False

DEFAULTS = SA_defaults(True, s_0, t_0, neighbourhood_func, step_size, temp_reduc_func, acc_prob_func, stop_cond, max_i, max_epoch, tolerance)


# In[5]:


results = simulated_annealing(f, DEFAULTS, print_workings=True)
results[1]


# In[6]:


print_all_constraints(results[1], constraints)
print("Profit: ", f(results[1]))


# In[7]:


# Imports my plotting module
import batch_plotting as batch_plt

# Imports my spiral coordinate generating module
from utilities import n_dim_spiral


# In[8]:


# Batch testing start position
starting_point_results = []
end_point = []
spiral = n_dim_spiral({"x1": 0, "x2": 0, "x3": 0, "x4": 0}, 1000, 0.1)
for i in range(20):
    for j in range(len(spiral)):
        ps = spiral[j]
        result = simulated_annealing(f, DEFAULTS, s_0 = ps)
        end_point.append(result[1])
        starting_point_results.append({"x": j, "y": f(result[1]) if result[1] is not False else False})


# In[9]:


batch_plt.plot_2d_batch_accuracy("profit: f(s_n)", "starting point: s_0", False, starting_point_results)


# In[10]:


# Extract the results above 16 profit

best_sprs = [(i, list(filter(lambda e: e["y"] > 16, starting_point_results[i*1000: (i+1)*1000]))) for i in range(20)]
best_sprs = list(filter(lambda e: len(e[1]) > 0, best_sprs))
best_sprs


# In[11]:


best_start_sprs = []
for t in best_sprs:
    for ele in t[1]:
        keys = ["x1", "x2", "x3", "x4"]
        x = ele["x"]
        y = ele["y"]
        start_cx = spiral[x]
        end_cx = end_point[x+t[0]*1000]
        if end_cx is not False:
            best_start_sprs.append(start_cx)
            print("{} {} | {} | {}".format(x, [round(start_cx[key],3) for key in keys], [round(end_cx[key],3) for key in keys], round(y, 3)))


# In[12]:


# Finding the average best start point indicated by the batch test
avg = {"x1": 0, "x2": 0, "x3": 0, "x4": 0}
dims = 4
for i in best_start_sprs:
    for k, v in i.items():
        avg[k] += v
for k, v in avg.items():
    avg[k] = round(avg[k]/len(best_start_sprs), 3)
print("Best starting point on average: ", avg, "\n (will vary each time batch test run)")


# In[13]:


# Testing certain 'end_points'
print_all_constraints(end_point[4372], constraints)
print("Profit: ", f(end_point[4372]))


# In[14]:


# Set my start point to (0.7, 0.7, 0.7, 0.7) which was the best the first time I ran the starting point batch test
DEFAULTS.s_0 = {"x1": 0.7, "x2": 0.7, "x3": 0.7, "x4": 0.7}

# Batch testing starting temperature and temperature function
temp_results = []
end_point = []

for g in range(40):
    grad = (1+g)/41
    linear_temp_func = lambda x: x*grad
    for t in range(30):
        start_temp = (t+1)*0.2
        for i in range(10):
            result = simulated_annealing(f, DEFAULTS, t_0=start_temp, temp_reduc_func=linear_temp_func)
            end_point.append(result[1])
            temp_results.append({"x": grad, "y": start_temp, "z": f(result[1]) if result[1] is not False else False})


# In[15]:


batch_plt.plot_3d_batch_accuracy("temperature gradient", "start temperature: t_0", "profit: f(s_n)", False, temp_results)


# In[16]:


DEFAULTS.t_0 = 2
DEFAULTS.temp_reduc_func = lambda x: 0.9*x

# Batch testing step_size and max_epoch
step_epoch_results = []
end_point= []

for ep in range(5, 31):
    for s in range(30):
        step_size = (s+1)/40
        for i in range(10):
            result = simulated_annealing(f, DEFAULTS, max_epoch=ep, step_size=step_size)
            end_point.append(result[1])
            step_epoch_results.append({"x": step_size, "y": ep, "z": f(result[1]) if result[1] is not False else False})


# In[17]:


batch_plt.plot_3d_batch_accuracy("step size", "epochs", "profit: f(s_n)", False, step_epoch_results)


# In[18]:


DEFAULTS.max_epoch = 10
DEFAULTS.step_size = 0.1

# Run through with improved parameters
results = simulated_annealing(f, DEFAULTS, print_workings=True)
print("\nStats:")
print_all_constraints(results[1], constraints)
print("\nProfit: {}\nSolution: {}".format(f(results[1]), [round(results[1][key], 3) for key in ["x1", "x2", "x3", "x4"]]))

