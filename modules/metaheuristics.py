#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install numpy')


# In[4]:


import random
import numpy as np


# In[1]:


###### Gradient Descent stuff
'''
        df      :   The differentiated problem function which is being investigated by the metaheuristic.
        x_0     :   Starting position.
        max_i   :   The maximum amount of iterations.
        step_m  :   The multipler of the step size.
        e_g     :   The tolerance of the gradient.
        e_x     :   The tolerance of the difference in x.
'''

def gradient_descent(df, x_0, max_i, step_m, e_g, e_x, print_workings=False):
    # Set the current x and create a way of storing the previous steps.
    current_x = x_0
    g = df(current_x)
    step_array = []
    
    # Whether to print the workings
    if (print_workings == True):
        print("--------------------------------------------------------------------------------------------\nIteration\tX\tg\tdiff\nStart (0)\t{}\t{}\t{}".format(round(current_x, 2), round(g, 2), "N/A"))
        
    
    # Loop for a maximum of max_i
    for i in range(max_i):
        # Set previous x
        step_array.append(current_x)
        # Find the current x
        current_x = round(current_x - step_m*g, 8)
        # Get a new gradient
        g = round(df(current_x), 8)
        # Find difference in x
        diff = current_x - step_array[i]
        
        # Whether to print the workings
        if (print_workings == True):
            print("{}\t\t{}\t{}\t{}".format(i+1, round(current_x, 2), round(g, 2), round(diff, 2)))
        
        # Check if either of the tolerance conditions are met, if so stop the loop. 
        if (abs(g) < e_g or abs(diff) < e_x):
            break
    
    # Add final x to step_array
    step_array.append(current_x)
    # Return a tuple of all steps and final answer
    return (step_array, current_x)


###### Simulated annealing stuff
'''
        f               :   The problem function which is being investigated by the metaheuristic.
        s_0             :   Initial solution.
        t_0             :   Initial temperature.
        temp_reduc_func :   Temperature reduction function.
        acc_prob_func   :   Acceptance probability function.
        stop_cond       :   The function which yields a boolean value of whether to continue the algorithm.
        max_i           :   The maximum amount of iterations
        max_epoch       :   The amount of epochs before the the temperature reduction function is used. 
        tolerance       :   The tolernce value passed to the stop condition. *optional*
'''

def simulated_annealing(f, s_0, t_0, neighbourhood_func, temp_reduc_func, acc_prob_func, stop_cond, max_i, max_epoch, print_workings=False, tolerance=None):
    # Sets the initial value of s_n (when n = 0)
    solution = s_0
    # Sets the initial value of s_n-1 (not used for the first iteration of the outer loop)
    prev_solution = s_0
    # The current temperature
    temperature = t_0
    # The iterations of the outer (while) loop.
    iteration_counter = 0
    step_array = []
    while (iteration_counter == 0 or not stop_cond(iteration_counter, max_i, solution, prev_solution, tolerance)):
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


# In[ ]:


###### Taboo search stuff
'''
        f                  :   The problem function which is being investigated by the metaheuristic.
        s0                 :   The starting point.
        stopping_cond      :   The function which returns whether to stop the algorithm.
        taboo_memory       :   The maximum number of taboo values that can be stored.
        neighbourhood_func :   The function which returns the neighbourhood of values about a value.
'''

def taboo_search(f, s0, stopping_cond, taboo_memory, neighbourhood_func, print_workings=False, stop_args=None, neighbourhood_args=None):
    taboo_list = [s0]
    s = s0
    i = 1
    viable_neighbours = None
    while not stopping_cond(i, s, viable_neighbours, **stop_args):
        neighbourhood = neighbourhood_func(s, **neighbourhood_args)
        best_neighbour = neighbourhood[0]
        viable_neighbours = len(neighbourhood)
        for n in neighbourhood:
            if n in taboo_list:
                viable_neighbours -= 1
            elif f(n) < f(best_neighbour):
                best_neighbour = n                
        if (f(best_neighbour) < f(s)):
            s = best_neighbour
        if (len(taboo_list) == taboo_memory):
            taboo_list.pop(0)
        taboo_list.append(best_neighbour)
        if (print_workings == True):
            print("Iteration: {},\tCurrent solution: {},\tTaboo list: {}".format(i, s, taboo_list))
        i += 1
    return s


# In[2]:


###### Genetic Algorithm Stuff

# Data wrapper for an instance of a member in the 'population'
class individual:
    def __init__(self, dna=None, gen=None):
        # If no dna is provided, generate dna from encoding a random float; with a random sign, exponent and significand
        if (dna == None):
            start_value = (2 * random.random() - 1) * 10**(random.randrange(0, 4))
            dna = encode_dna(start_value)
        self.dna = dna
        self.gen = 0 if gen is None else gen
    def get_dna(self):
        return self.dna
    def get_value(self):
        return decode_dna(self.dna)
    def get_gen(self):
        return self.gen

# Default GA parameters
'''
        fitness_func         :   The problem function which is being investigated by the metaheuristic.
        population_size      :   The size of the population per generation.
        epochs               :   The number of generations that are produced over the course of the algorithm.
        fitness_upper_bound  :   The percentage of the population which survives before the breeding phase.
        selection_func       :   A way of selecting a pair of individuals from a population.
        mutation_chance      :   The chance that any digit can change to another random digit in an offsprings dna structure.
        cross_over_amount    :   The amount of cross over points when offspring dna is being made from the parents.
        sign_change_chance   :   THe chance that the sign changes in an offsprings dna structure.
'''

def genetic_algorithm(population_size, epochs, fitness_upper_bound, selection_function, cross_over_amount, mutation_chance, sign_change_chance, show_workings=False):
    # Initial population instantiation
    population = []
    for p in range(population_size):
        population.append(individual())

    # Genetic algorithm loop
    cumulative_population = []
    result = None
    if (show_workings):
        print("Genetic Algorithm (top 10 results per generation)\n\n\tPopulation size: {}\n\tEpochs/Generations: {}\n\tSelected population: {}%\n\tCrossover amount: {}\n\tMutation chance: {}%\n\tSign change chance: {}%\n________________________________________________________________________________".format(population_size, epochs, fitness_upper_bound*100, cross_over_amount, mutation_chance*100, sign_change_chance*100))
    for e in range(epochs):
        # Where the next population will be stored
        next_gen_pop = []
        # Sort population by their values when input through the fitness function. Highest to lowest
        population.sort(key=lambda ind: fitness_function(ind.get_value()))
        # Put sorted population into cumulative population 
        cumulative_population.extend(population)
        if (show_workings):
            print("Gen: {}  \tValues: [{}]".format(e+1, ', '.join([str(population[i].get_value()) for i in range(10)])))
        # Kill population which aren't in the fitness_upper_bound
        population = population[0:int(fitness_upper_bound*population_size)]
        # Create next generation population
        for p in range(int(len(population)/2)-1):
            individuals = selection_function(p, population)
            # Create an amount of next generation offspring with these individuals greater than or equal to the amount previous generation  
            for m in range(math.ceil(2/fitness_upper_bound)):
                next_gen_pop.append(breed_individuals(individuals[0], individuals[1], cross_over_amount, mutation_chance, sign_change_chance))
        # Replace current generation population with new generation population
        population = next_gen_pop[0:population_size]
    # After all the epochs pick the first individual (fittest) in the population and obtain their value.
    solution = population[0].get_value()
    # Return the history of the population (cumulative population) and the solution. 
    return (cumulative_population, solution)

