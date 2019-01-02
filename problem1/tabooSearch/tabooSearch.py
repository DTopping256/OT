#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append('../../modules')

# Imports the python definition of f(x) for problem 1.

from problem_function import f


# In[2]:


from metaheuristics import taboo_search


# In[3]:


# Graph the results of one full GA run

def plot_taboo_search_metaheuristic(f, xrange, results, print_data=False):
    xs = np.linspace(xrange[0], xrange[1], 2*(xrange[1]-xrange[0]))
    ys = np.array([f(i) for i in xs])
    
    midpoint = (int(abs(xs[-1]-xs[0])/2), int(abs(ys[-1]-ys[0])/2))
    
    data = results[0]
    data_length = len(data)
    solution = results[1]
    
    # MatPlotLib
    
    # Plot the problem line
    plt.title("Problem line (only)")
    plt.plot(xs, ys, '-g', label="f(x)")
    plt.legend(framealpha=0.4)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()
    
    xplots = []
    yplots = []
    
    # Get plotting data
    if (print_data == True):
        print("Plot data (2DP)\n_____________________________________\nX")
    for i in range(data_length):
        val = data[i]
        xplots.append(val)
        yplots.append(f(val))
        if (print_data == True):
            print(round(val, 2))
    
    # Plot best results against problem line
    plt.title("Results against problem line")
    line = plt.plot(xs, ys, '-g', label="f(x)")
    plt.plot(xplots, yplots, "o", color="b", label="Solution")
    
    # Annotate first and last plots
    plt.annotate(s="First s", xy=(xplots[0], yplots[0]), xytext=(midpoint[0], midpoint[1]+170), arrowprops=dict(arrowstyle='->'))
    plt.annotate(s="Last s", xy=(xplots[-1], yplots[-1]), xytext=(midpoint[0], midpoint[1]+30), arrowprops=dict(arrowstyle='->'))
    
    plt.legend(framealpha=0.4)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()


# In[4]:


s0 = 120
def stop_function(i, s, viable_neighbours, max_i):
    return (i != 0 and (max_i < i or (viable_neighbours == 0)))
taboo_memory = 5
def get_neighbourhood(s0, step_size):
    return [round(s0 - step_size, 2), round(s0 + step_size, 2)]
max_i = 300
step_size = 0.1

results = taboo_search(f, s0, stop_function, taboo_memory, get_neighbourhood, True, stop_args={"max_i": max_i}, neighbourhood_args={"step_size": step_size})


# In[5]:


plot_taboo_search_metaheuristic(f, (-5, 150), results)


# In[6]:


# Imports my plotting module
import batch_plotting as batch_plt


# In[7]:


# Batch test taboo search with different starting points
starting_point_results = []
for start_x in range(80, 120):
    result = taboo_search(f, start_x, stop_function, taboo_memory, get_neighbourhood, False, stop_args={"max_i": max_i}, neighbourhood_args={"step_size": step_size})
    starting_point_results.append({"x": start_x, "y": result[1]})
batch_plt.plot_2d_batch_accuracy("finish point (x_n)", "starting point (x_0)", 101, starting_point_results)


# In[8]:


# Batch test gradient descent with different max_iterations (over 3 starting points)
starting_points = [80, 101, 120]
for starting_point in starting_points:
    iteration_results = []
    for max_i in range(40):
        max_iter = (max_i+1)*5
        result = taboo_search(f, starting_point, stop_function, taboo_memory, get_neighbourhood, False, stop_args={"max_i": max_iter}, neighbourhood_args={"step_size": step_size})
        iteration_results.append({"x": max_iter, "y": result[1]})

    print("Starting at {}".format(starting_point))
    batch_plt.plot_2d_batch_accuracy("finish point (x_n)", "iterations (max_i)", 101, iteration_results)


# In[9]:


# Batch test for step size
for starting_point in starting_points:
    iteration_results = []
    for s in range(40):
        step = (s+1)/20
        result = taboo_search(f, starting_point, stop_function, taboo_memory, get_neighbourhood, False, stop_args={"max_i": max_iter}, neighbourhood_args={"step_size": step})
        iteration_results.append({"x": step, "y": result[1]})

    print("Starting at {}".format(starting_point))
    batch_plt.plot_2d_batch_accuracy("finish point (x_n)", "step size", 101, iteration_results)


# In[12]:


# Batch test for taboo memory
for starting_point in starting_points:
    iteration_results = []
    for memory in range(1, 5):
        result = taboo_search(f, starting_point, stop_function, memory, get_neighbourhood, False, stop_args={"max_i": max_iter}, neighbourhood_args={"step_size": step_size})
        iteration_results.append({"x": memory, "y": len(result[0]), "z": result[1]})

    print("Starting at {}".format(starting_point))
    batch_plt.plot_3d_batch_accuracy("taboo memory", "iterations needed", "solution", 101, iteration_results)


# In[ ]:




