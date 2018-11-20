#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import numpy as np
import matplotlib.pyplot as plt

e = math.e

# The python definition of f(x) for problem 1.

def problem_function(x):
    if (x <= 100):
        return float(-e**(-(x/100)**2))
    else:
        return float(-e**(-1) + (x - 100)*(x - 102))


# In[34]:


import os
import sys
import random

# Some definitions for the following variables which will be used in simulated annealing.
'''
        f               :   The function which metaheuristics are being used to test.
        s_0             :   Initial solution.
        t_0             :   Initial temperature.
        temp_reduc_func :   Temperature reduction function.
        acc_prob_func   :   Acceptance probability function.
        stop_cond       :   The function which yields a boolean value of whether to continue the algorithm.
        max_i           :   The maximum amount of iterations
        max_epoch       :   The amount of epochs before the the temperature reduction function is used. 
'''


def simulated_annealing(f, s_0, t_0, neighbourhood_func, temp_reduc_func, acc_prob_func, stop_cond, max_i, max_epoch, print_workings=False):
    # Sets the initial value of s_n (when n = 0)
    solution = s_0
    # Sets the initial value of s_n-1 (not used for the first iteration of the outer loop)
    prev_solution = s_0
    # The current temperature
    temperature = t_0
    # The iterations of the outer (while) loop.
    iteration_counter = 0
    step_array = []
    while (iteration_counter == 0 or not stop_cond(iteration_counter, max_i, solution, prev_solution)):
        if (print_workings == True):
            print("--------------------------------------------------------------------------------------------\ns_%d: %f" % (iteration_counter, solution))
        prev_solution = solution
        step_array.append((solution, temperature))
        for epoch in range(1, max_epoch+1):
            neighbourhood = neighbourhood_func(solution)
            possible_solution = neighbourhood[random.randrange(
                0, len(neighbourhood))]
            solution_eval_diff = f(possible_solution) - f(solution)
            # If the difference between the possible solution (solution picked in the current epoch) and the solution (the solution of the current iteration of epochs) when put through the acceptance probablity function, is greater than random noise then pick it.
            accepted = False
            if (solution_eval_diff < 0 or acc_prob_func(
                    solution_eval_diff, temperature) > random.random()):
                # Set a new value of solution
                solution = possible_solution
                accepted = True
            if (print_workings == True):
                print("Epoch: %d\ts: %f\tt: %f\tAccepted: %g" % (epoch, possible_solution, temperature, accepted))
        # Reduce the temperature and increment the iteration counter
        temperature = temp_reduc_func(temperature)
        iteration_counter += 1
    step_array.append((solution, temperature))
    return (step_array, solution)


# In[38]:


def plot_problem(f, xrange, data, print_data=False): 
    xs = np.linspace(xrange[0], xrange[1], 2*(xrange[1]-xrange[0]))
    ys = np.array([f(i) for i in xs ])
    
    data_length = len(data)
    s_0 = data[0][0]
    s_n = data[-1][0]
    
    temperatures = np.array([round(i[1], 2) for i in data])
    xdata = np.array([i[0] for i in data])
    xplots = np.array([round(i, 2) for i in xdata])
    yplots = np.array([round(f(i), 2) for i in xdata])
    
    # Work out bounds of graph
    height = (f(xrange[0]), f(xrange[1]))
    width = xrange
    midpoint = ((width[0]+width[1])/2, (height[0]+height[1])/2)

    # MatPlotLib
    
    # Plot the results against problem line
    plt.title("Results against problem line")
    plt.plot(xs, ys, '-g', label="f(x)")
    plt.plot(xplots, yplots, "ok", label="Results")
    
    # Annotate first and last plots
    plt.annotate(s="Start point", xy=(xplots[0], yplots[0]), xytext=(midpoint[0], midpoint[1]+70), arrowprops=dict(arrowstyle='->'))
    plt.annotate(s="Finish point", xy=(xplots[-1], yplots[-1]), xytext=(midpoint[0], midpoint[1]+30), arrowprops=dict(arrowstyle='->'))
    
    plt.legend(framealpha=0.4)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()
    if (print_data == True):
        print("Plot data (2DP)\n_____________________________________\nEpoch\tTemperature\tSolution")
        for i in range(data_length):
            print("{}\t{}\t\t({}, {})".format(i, temperatures[i], xplots[i], yplots[i]))
            
# Graph the results (data is a tuple of x's and tempaturature per epoch)

def plot_problem_wth_temp(f, xrange, data, print_data=False): 
    xs = np.linspace(xrange[0], xrange[1], 2*(xrange[1]-xrange[0]))
    ys = np.array([f(i) for i in xs ])
    
    data_length = len(data)
    s_0 = data[0][0]
    s_n = data[-1][0]
    
    temperatures = np.array([round(i[1], 2) for i in data])
    xdata = np.array([i[0] for i in data])
    xplots = np.array([round(i, 2) for i in xdata])
    yplots = np.array([round(f(i), 2) for i in xdata])
    
    # Work out bounds of graph
    height = (f(xrange[0]), f(xrange[1]))
    width = xrange
    midpoint = ((width[0]+width[1])/2, (height[0]+height[1])/2)

    # MatPlotLib
    
    # Plot the problem line
    plt.title("Problem line (only)")
    plt.plot(xs, ys, '-g', label="f(x)")
    plt.legend(framealpha=0.4)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()
    
    # Plot the results against problem line
    plt.title("Results against problem line")
    line = plt.plot(xs, ys, '-g', label="f(x)")
    
    # Plot array_plottings
    tenth_data_length = int(data_length/10)
    for i in range(10):
        colour = ((10-i)/10, 0, i/10)
        label=" "
        if (i == 0):
            label="Epoch (hot temp)"
        if (i == 9):
            label="Epoch (cold temp)"
        plt.plot(xplots[i*tenth_data_length:(i+1)*tenth_data_length], yplots[i*tenth_data_length:(i+1)*tenth_data_length], "o", color=colour, label=label)
    
    # Annotate first and last plots
    plt.annotate(s="Start point", xy=(xplots[0], yplots[0]), xytext=(midpoint[0], midpoint[1]+70), arrowprops=dict(arrowstyle='->'))
    plt.annotate(s="Finish point", xy=(xplots[-1], yplots[-1]), xytext=(midpoint[0], midpoint[1]+30), arrowprops=dict(arrowstyle='->'))
    
    plt.legend(framealpha=0.4)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()
    if (print_data == True):
        print("Plot data (2DP)\n_____________________________________\nEpoch\tTemperature\tSolution")
        for i in range(data_length):
            print("{}\t{}\t\t({}, {})".format(i, temperatures[i], xplots[i], yplots[i]))


# In[3]:


s_0 = 120
t_0 = float(1000)
max_i = 50
max_epoch = 50

def neighbourhood_func(x):
    neighbourhood = [x-0.1, x+0.1]
    return neighbourhood


def temp_reduc_func(x):
    return float(0.75*x)


def acc_prob_func(diff, temperature):
    return float(e**(-diff/temperature))


def stop_cond(iteration_counter, max_i, solution, prev_solution):
    if (iteration_counter > 0):
        if (iteration_counter >= max_i):
            return True
    return False


# In[24]:


# Run simulated annealing (test)
simulated_annealing_results = simulated_annealing(problem_function, s_0,
                    t_0, neighbourhood_func, temp_reduc_func, acc_prob_func, stop_cond, max_i, max_epoch, True)


# In[25]:


# Graph results
plot_problem_wth_temp(problem_function, (-5, 125), simulated_annealing_results[0])


# In[26]:


# Graph results
plot_problem_wth_temp(problem_function, (90, 120), simulated_annealing_results[0])


# In[9]:


# Imports my plotting module
sys.path.append('../../modules')
import batch_plotting as batch_plt


# In[10]:


#Run the simulated annealing on a range of different starting positions

accuracy_wth_respect_to_starting_position = []
for i in range(60):
    start = i*5-50
    s_a_result = simulated_annealing(problem_function, start,
                    t_0, neighbourhood_func, temp_reduc_func, acc_prob_func, stop_cond, max_i, max_epoch)[1]
    accuracy_wth_respect_to_starting_position.append({"x": start, "y": s_a_result, "diff_to_target": abs(101-s_a_result)})


# In[11]:


batch_plt.plot_2d_batch_accuracy("final solution (s_n)", "starting point (s_0)", 101, accuracy_wth_respect_to_starting_position)


# In[9]:


#Run the simulated annealing on a range of different starting temperatures and temperature reduction gradients

def accuracy_with_temp(s_0):
    results = []
    for i in range(50):
        start_temp = i*20+1
        for j in range(50):
            temp_gradient = (1+j)/52
            def linear_temp_reduction_f(t):
                return t*temp_gradient
            s_a_result = simulated_annealing(problem_function, s_0,
                        start_temp, neighbourhood_func, linear_temp_reduction_f, acc_prob_func, stop_cond, max_i, max_epoch)[1]
            results.append({"x": start_temp, "y": temp_gradient, "z": s_a_result})
    return results
    
#starting at s_0 = 80 (-21 from target)
accuracy_wth_respect_to_temp_at_80 = accuracy_with_temp(80)
#starting at s_0 = 101 (on target)
accuracy_wth_respect_to_temp_at_101 = accuracy_with_temp(101)
#starting at s_0 = 120 (+21 from target)
accuracy_wth_respect_to_temp_at_120 = accuracy_with_temp(120)


# In[10]:


print("When s_0 is 80")
batch_plt.plot_3d_batch_accuracy("start temperature (t_0)", "temperature gradient", "result (s_n)", 101, accuracy_wth_respect_to_temp_at_80)

print("When s_0 is 101")
batch_plt.plot_3d_batch_accuracy("start temperature (t_0)", "temperature gradient", "result (s_n)", 101, accuracy_wth_respect_to_temp_at_101)

print("When s_0 is 120")
batch_plt.plot_3d_batch_accuracy("start temperature (t_0)", "temperature gradient", "result (s_n)", 101, accuracy_wth_respect_to_temp_at_120)


# In[11]:


# Create a neighbourhood of pairs amount of points either side of x, which have a difference of step.
# Returns [x-0.1, x+0.1] by default
def flexible_neighbourhood_func(x, step=0.1, pairs=1):
    neighbourhood = []
    for i in range(0, pairs):
        xdiff = step*(i+1)
        neighbourhood.append(x-xdiff)
        neighbourhood.append(x+xdiff)
    return neighbourhood


# In[12]:


flexible_neighbourhood_func(1, 0.2, 2)


# In[13]:


def accuracy_with_neighbourhood(s_0):
    results = []
    for i in range(1, 11):
        pairs = i
        for j in range(40):
            step = (j+1)/20
            s_a_result = simulated_annealing(problem_function, s_0,
                        t_0, lambda x: flexible_neighbourhood_func(x, step, pairs), temp_reduc_func, acc_prob_func, stop_cond, max_i, max_epoch)[1]
            results.append({"x": step, "y": pairs, "z": s_a_result})
    return results

#starting at s_0 = 80 (-21 from target)
accuracy_wth_respect_to_nh_at_80 = accuracy_with_neighbourhood(80)
#starting at s_0 = 101 (on target)
accuracy_wth_respect_to_nh_at_101 = accuracy_with_neighbourhood(101)
#starting at s_0 = 120 (+21 from target)
accuracy_wth_respect_to_nh_at_120 = accuracy_with_neighbourhood(120)


# In[15]:


print("When s_0 is 80")
batch_plt.plot_3d_batch_accuracy("step", "pairs of neighbourhood values", "result (s_n)", 101, accuracy_wth_respect_to_nh_at_80)

print("When s_0 is 101")
batch_plt.plot_3d_batch_accuracy("step", "pairs of neighbourhood values", "result (s_n)", 101, accuracy_wth_respect_to_nh_at_101)

print("When s_0 is 120")
batch_plt.plot_3d_batch_accuracy("step", "pairs of neighbourhood values", "result (s_n)", 101, accuracy_wth_respect_to_nh_at_120)


# In[15]:


# Batch testing with stop_condition, iterations & epochs
def accuracy_with_stop_condition(s_0, stop_condition):
    results = []
    for e in range(1, 11):
        for i in range(50):
            s_a_result = simulated_annealing(problem_function, s_0, t_0, neighbourhood_func, temp_reduc_func, acc_prob_func, stop_condition, i, e)[1]
            results.append({"x": e, "y": i, "z": s_a_result})
    return results


# In[39]:


print("#1 Stop condition is iteration based")
def stop_condition_1(i, max_i, s, prev_s):
    if (i < max_i):
        return False
    else:
        return True
    
print("Example run through")
sa_results = simulated_annealing(problem_function, s_0, t_0, neighbourhood_func, temp_reduc_func, acc_prob_func, stop_condition_1, max_i, max_epoch)
plot_problem(problem_function, (-5, 125), sa_results[0], True)


# In[17]:


print("Batch testing with varied iterations and epochs")
#starting at s_0 = 80 (-21 from target)
accuracy_wth_respect_to_sc_at_80_1 = accuracy_with_stop_condition(80, stop_condition_1)
#starting at s_0 = 101 (on target)
accuracy_wth_respect_to_sc_at_101_1 = accuracy_with_stop_condition(101, stop_condition_1)
#starting at s_0 = 120 (+21 from target)
accuracy_wth_respect_to_sc_at_120_1 = accuracy_with_stop_condition(120, stop_condition_1)

print("When s_0 is 80")
batch_plt.plot_3d_batch_accuracy("epochs", "iterations (max_i)", "result (s_n)", 101, accuracy_wth_respect_to_sc_at_80_1)
print("When s_0 is 101")
batch_plt.plot_3d_batch_accuracy("epochs", "iterations (max_i)", "result (s_n)", 101, accuracy_wth_respect_to_sc_at_101_1)
print("When s_0 is 120")
batch_plt.plot_3d_batch_accuracy("epochs", "iterations (max_i)", "result (s_n)", 101, accuracy_wth_respect_to_sc_at_120_1)


# In[40]:


print("#2 Stop condition is solution difference based")
def stop_condition_2(i, max_i, s, prev_s):
    if (abs(s-prev_s) <= 0.1):
        return True
    else:
        return False
    
print("Example run through")
sa_results = simulated_annealing(problem_function, s_0, t_0, neighbourhood_func, temp_reduc_func, acc_prob_func, stop_condition_2, max_i, max_epoch)
plot_problem(problem_function, (-5, 125), sa_results[0], True)


# In[36]:


print("Batch testing with varied iterations and epochs")
#starting at s_0 = 80 (-21 from target)
accuracy_wth_respect_to_sc_at_80_2 = accuracy_with_stop_condition(80, stop_condition_2)
#starting at s_0 = 101 (on target)
accuracy_wth_respect_to_sc_at_101_2 = accuracy_with_stop_condition(101, stop_condition_2)
#starting at s_0 = 120 (+21 from target)
accuracy_wth_respect_to_sc_at_120_2 = accuracy_with_stop_condition(120, stop_condition_2)

print("When s_0 is 80")
batch_plt.plot_3d_batch_accuracy("epochs", "iterations (max_i)", "result (s_n)", 101, accuracy_wth_respect_to_sc_at_80_2)
print("When s_0 is 101")
batch_plt.plot_3d_batch_accuracy("epochs", "iterations (max_i)", "result (s_n)", 101, accuracy_wth_respect_to_sc_at_101_2)
print("When s_0 is 120")
batch_plt.plot_3d_batch_accuracy("epochs", "iterations (max_i)", "result (s_n)", 101, accuracy_wth_respect_to_sc_at_120_2)


# In[47]:


print("#3 Stop condition is solution output difference based")
def stop_condition_3(i, max_i, s, prev_s):
    if (abs(problem_function(s)-problem_function(prev_s)) <= 0.1):
        return True
    else:
        return False
    
print("Example run through")
sa_results = simulated_annealing(problem_function, s_0, t_0, neighbourhood_func, temp_reduc_func, acc_prob_func, stop_condition_3, max_i, max_epoch)
plot_problem(problem_function, (-5, 125), sa_results[0], True)


# In[46]:


print("Batch testing with varied iterations and epochs")
#starting at s_0 = 80 (-21 from target)
accuracy_wth_respect_to_sc_at_80_3 = accuracy_with_stop_condition(80, stop_condition_3)
#starting at s_0 = 101 (on target)
accuracy_wth_respect_to_sc_at_101_3 = accuracy_with_stop_condition(101, stop_condition_3)
#starting at s_0 = 120 (+21 from target)
accuracy_wth_respect_to_sc_at_120_3 = accuracy_with_stop_condition(120, stop_condition_3)

print("When s_0 is 80")
batch_plt.plot_3d_batch_accuracy("epochs", "iterations (max_i)", "result (s_n)", 101, accuracy_wth_respect_to_sc_at_80_3)
print("When s_0 is 101")
batch_plt.plot_3d_batch_accuracy("epochs", "iterations (max_i)", "result (s_n)", 101, accuracy_wth_respect_to_sc_at_101_3)
print("When s_0 is 120")
batch_plt.plot_3d_batch_accuracy("epochs", "iterations (max_i)", "result (s_n)", 101, accuracy_wth_respect_to_sc_at_120_3)


# In[ ]:




