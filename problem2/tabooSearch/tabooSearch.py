#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import sys

# Allows me to import my modules
sys.path.extend(["../../modules", "../"])

# Imports the python definition of f(x) for problem 1.

from problem import f, constraints, check_all_constraints, print_all_constraints


# In[2]:


###### Taboo search stuff
'''
        f                  :   The problem function which is being investigated by the metaheuristic.
        s_0                :   The starting point.
        stopping_cond      :   The function which returns whether to stop the algorithm.
        stopping_args      :   The constant arguments passed to the neighbourhood function.
        taboo_memory       :   The maximum number of taboo values that can be stored.
        neighbourhood_func :   The function which returns the neighbourhood of values about a value.
        neighbourhood_args :   The constant arguments passed to the neighbourhood function.
'''

class TS_defaults:
    def __init__(self, s_0, stopping_cond, stop_args, taboo_memory, neighbourhood_func, neighbourhood_args):
        self.s_0 = s_0
        self.stopping_cond = stopping_cond
        self.stop_args = stop_args
        self.taboo_memory = taboo_memory
        self.neighbourhood_func = neighbourhood_func
        self.neighbourhood_args = neighbourhood_args

def taboo_search(f, is_maximisation, constraints, DEFAULTS, s_0 = None, stopping_cond = None, stop_args = None, taboo_memory = None, neighbourhood_func = None, neighbourhood_args = None, print_workings=False):
    # Default parameters
    s_0 = DEFAULTS.s_0 if s_0 is None else s_0
    stopping_cond = DEFAULTS.stopping_cond if stopping_cond is None else stopping_cond
    stop_args = DEFAULTS.stop_args if stop_args is None else stop_args
    taboo_memory = DEFAULTS.taboo_memory if taboo_memory is None else taboo_memory
    neighbourhood_func = DEFAULTS.neighbourhood_func if neighbourhood_func is None else neighbourhood_func
    neighbourhood_args = DEFAULTS.neighbourhood_args if neighbourhood_args is None else neighbourhood_args
    
    # Initial values of local variables
    taboo_list = [s_0]
    s = {k: v for k, v in s_0.items()}
    i = 1
    
    # Keeps track of where the algorithm has been (without affecting the answer)
    history = [s]
    viable_neighbours = None
    while True:
        neighbourhood = neighbourhood_func(s, **neighbourhood_args)
        neighbourhood = list(filter(lambda item: item not in taboo_list, neighbourhood))
        neighbourhood = list(filter(lambda item: check_all_constraints(item, constraints, print_workings), neighbourhood))
        viable_neighbours = len(neighbourhood)
        if (viable_neighbours > 0):
            neighbourhood.sort(key=lambda item: f(item), reverse=is_maximisation)
            best = neighbourhood[0]
            if ((is_maximisation and f(best) > f(s)) or (not is_maximisation and f(best) < f(s))):
                s = {k: v for k, v in best.items()}
                history.append(best)
            if (len(taboo_list) == taboo_memory):
                taboo_list.pop(0)
            taboo_list.append(best)
        if (print_workings == True):
            print("Iteration: {},\tCurrent solution: {},\tTaboo list: {}".format(i, s, taboo_list))
        if (stopping_cond(i, s, viable_neighbours, **stop_args)):
            break
        i += 1
    # Add final solution
    if (i == 1):
        return ([], False)
    history.append(s)
    return (history, s)


# In[3]:


s_0 = {"x1": 0, "x2": 0, "x3": 0, "x4": 0}

def stopping_cond(i, s, viable_neighbours, max_i):
    return (i != 0 and (max_i < i or (viable_neighbours == 0)))

stopping_args = {"max_i": 300}
taboo_memory = 8

def neighbourhood_func(s_0, step_size):
    neighbourhood = []
    keys = s_0.keys()
    for i in range(len(keys)*2):
        sign = 1 if i < 4 else -1
        key = list(keys)[i % 4]
        neighbour = {k: v for k, v in s_0.items()}
        neighbour[key] += sign*step_size
        neighbourhood.append(neighbour)
    return neighbourhood

neighbourhood_args = {"step_size": 0.1}

DEFAULTS = TS_defaults(s_0 = s_0, stopping_cond = stopping_cond, stop_args = stopping_args, taboo_memory = taboo_memory, neighbourhood_func = neighbourhood_func, neighbourhood_args = neighbourhood_args)


# In[4]:


results = taboo_search(f, True, constraints, DEFAULTS, print_workings=True)


# In[5]:


print_all_constraints(results[1], constraints)
print("Profit: ", f(results[1]))


# In[6]:


# Imports my plotting module
import batch_plotting as batch_plt

# Imports my spiral coordinate generating module
from utilities import n_dim_spiral


# In[7]:


# Batch testing start position
starting_point_results = []
end_point = []
spiral = n_dim_spiral({"x1": 0, "x2": 0, "x3": 0, "x4": 0}, 1000, 0.1)
for j in range(len(spiral)):
    ps = spiral[j]
    result = taboo_search(f, True, constraints, DEFAULTS, s_0 = ps)
    end_point.append(result[1])
    starting_point_results.append({"x": j, "y": f(result[1]) if result[1] is not False else False})


# In[8]:


batch_plt.plot_2d_batch_accuracy("profit: f(s_n)", "starting point: s_0", False, starting_point_results)


# In[13]:


end_point[0:10]


# In[10]:


print_all_constraints({'x1': 1.0999999999999999,
  'x2': 0.5,
  'x3': 1.0999999999999999,
  'x4': 1.0999999999999999}, constraints)


# In[18]:


step_size_results = []
end_point = []

# Batch testing step size
for s in range(20):
    step_size = (s+1)/20
    result = taboo_search(f, True, constraints, DEFAULTS, neighbourhood_args={"step_size": step_size})
    end_point.append(result[1])
    step_size_results.append({"x": step_size, "y": f(result[1]) if result[1] is not False else False})


# In[19]:


batch_plt.plot_2d_batch_accuracy("profit: f(s_n)", "step size", False, step_size_results)


# In[24]:


print_all_constraints(end_point[0], constraints)
print("Profit: ", f(end_point[0]))

