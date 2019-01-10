# Genetic Algorithm

_Source code: [notebook](./geneticAlgorithm.ipynb) or [python script](./geneticAlgorithm.py)_

Being stochastic, GA will create different results each time but they will be very similar with the same settings.

## Abstract

GA consistantly gets close to the best profit answer that I have found so far which is 25.5.

In this GA I decided to design the algorithm to use a quinary dna structure to encode the 4 dimensional coordinates to 3 decimal place precision. I used a 32 length quinary array to hold the a search space between 0.000 and 15.624 (per dimension).

```py
# Coordinate data
{'x1': 0.0, 'x2': 1.234, 'x3': 5.678, 'x4': 6.0}

# Encoded coordinate data
['0', '0', '0', '0', '0', '0', '0', '1', '4', '4', '1', '4', '1', '4', '0', '2', '0', '3', '1', '4', '3', '0', '0', '0']
```

## Genetic algorithm with default starting parameters

With the [default](./simulatedAnnealing.py#L102) starting parameters, you get something like this:

```
Feasible:  10346
Infeasible:  4509
```

![GA](./profits_against_generation.png?raw=true "Profit against starting point.")

Although this graph looks largely like the bulk of the data is infeasible, this is actually not the case and there is a high density of data in a small space of the feasible region.

You can see that on this run of the algorithm, over the first 5 generations, the population largely converges onto the 5 and 25 profit part of the search space. This again converges further after 14 generations between 20 and 30.

The spread of values is largely due to the mutation function which is one of the stochastic features of this metaheuristic. However, most of the population is intersified around the optimal profit value due to the cross-over and selection functions.

## Changing population size

For this variable I tested values from 100 to 2000, for each of these I repeated the test for 5 times (as the algorithm is stochastic) to get a general idea of consistency.

When it gave answers which were infeasible, because the algorithm started outside the feasible region, the profit was set to 0.

![GA](./profit_against_pop_size.png?raw=true "Profit against starting point.")

With a population size of around 1000, profit is more focused around the optimal area. So I fixed the population at 1000 for the subsequent tests, although I did notice a large lag in subsequent testing

<div class="page"/>

## Changing fitness upper bound

For this I tested 20 values from 0.05 to 1.0, repeating testing at each value 5 times.

![GA](./profits_against_fub.png?raw=true "Profit against fitness upper bound.")

I fixed the fitness upper bound to 50% after this for subsquent tests as there didn't seem to be much of an effect.

## Changing amount of generations

I tested 35 amounts of epochs/generations from 5 to 40 epochs, each one repeated 5 times.

![GA](./profits_against_epochs.png?raw=true "Profit against epoch amount.")

I kept epochs at 30 because of the consistency of the results which tend to occur about this amount. However, the execution time is quite slow.

<div class="page"/>

## Changing cross over amount

I tested 15 cross over amounts from 5 to 20, each was repeated 4 times

![GA](./profits_against_cross_over_amount.png?raw=true "Profit against cross over amount.")

`Execution time: 183.16s` (each GA took ~3 seconds)

Cross over amount was fixed at 6 after this because it seemed to be more consistent at the lower amounts.

## Changing mutation chance

I tested 20 different mutation chances ranging from 0.02 to 0.4 in increments of 0.02; each repeated 5 times.

![GA](./profits_against_mutation_chance.png?raw=true "Profit against mutation chance.")

`Execution time: 215.933s` (each GA took ~2 seconds)

Mutation chance was reduced to 3% to make results more consistent over generations, with a larger population.

<div class="page"/>

## Changing selection method

Like in problem 1 in again used truncation selection (by default), fitness proportionate selection and tournament selection.

```
Execution time (Truncation selection GA):  2.118
Feasible:  33393
Infeasible:  11491
```

![GA](./profits_against_generation_trunc.png?raw=true "Profit against selection method (trunc).")

```
Execution time (FPS selection GA):  112.859
Feasible:  35169
Infeasible:  9715
```

![GA](./profits_against_generation_fps.png?raw=true "Profit against selection method (fps).")

```
Execution time (Tournament selection GA):  2.058
Feasible:  40530
Infeasible:  4354
```

![GA](./profits_against_generation_tourn.png?raw=true "Profit against selection method (tourn).")

These show that tournament selection is again far more superior than both truncation and fitness proportionate selection. Furthermore, is is about as quick as truncation selection which is the most basic.

## Conclusions

For the batch tests I would have liked to have had 10 repeats instead of 5, but this would have doubled the already very slow times that it took to do the processing; some of which just gave up and didn't return results.

Although GAs are good at finding very good solutions on average, the amount of time and calculations taken to get there for this problem is excessive compared to the other metaheuristics.

Pros:

- Frequently finds very good solutions.

Cons:

- Can be unreliable (because of the stochastic nature of GA's)
- Takes a huge amount of time / processing power compared with other metaheuristics at this particular problem. (because of the population and amount of epochs used)
