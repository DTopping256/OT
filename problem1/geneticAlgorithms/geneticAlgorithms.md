# Genetic Algorithms

_Source code: [notebook](./geneticAlgorithm.ipynb) or [python script](./geneticAlgorithm.py)_

Being stochastic, GA's will create different graphs each time but they will be very similar with the same settings.

## Abstract

I have made a generalised function `genetic_algorithm` which I can take in many parameters.

Throughout testing I found that the 2 minima picked up by the genetic algorithm are 0 and 101, and I have shown that 101 is the best solution out of the two; so for the rest of this I will refer to 101 as the global minimum and 0 as the local minimum. (see the conclusion)

<hr />

## Default GA

With the [default](./geneticAlgorithm.py#L197) starting parameters, you get something like this:

![GA (against line)](./default_ga_results.png?raw=true "GA (against line)")

![GA (vals per gen)](./default_ga_values_per_generation.png?raw=true "GA (vals per gen)")

The early generations tend to have the fittest individuals closer to the local minima at 0, because the trough is more spread out so theres a higher probability that individuals will be their when they are initially randomly generated. However, with cross-over and mutation there start to be more individuals which find the global minima at 101 and because these then become the fittest more individuals in later generations settle at the global minimum.

<hr />

## The algorithm by hand (first few iterations)

Starting with the [default](./geneticAlgorithm.py#L197) parameters:

- `population_size`: the population size per generation.
- `epochs`: the amount of epochs or generations of individuals. An [individual](./geneticAlgorithm.py#L133) is a class which I made to store the dna, generation and value of an instance of the population.
- `fitness_upper_bound`: The proportion of the population which survive to breed.
- `selection_function`: The way which couples of individuals are selected to pass down their dna.
- `mutation_chance`: The chance that a digit in the dna of an individual can randomly change from its parents.
- `sign_change_chance`: The chance that the sign part of the dna of an individual can randomly change from its parents.
- `cross_over_amount`: The amount of cross over that occurs when dna is combined from parent individuals.

Here are some constants which will be unchanged throughout as they are fundamental about GA's and the problem:

- `fitness_function`: the problem 1 function (imported from [problem_function](../../modules/problem_function.py) module)
- `breed_individuals`: the function ([source](./geneticAlgorithm.py#L164)) which unpacks the generation and dna from 2 individuals and first uses cross-over and then mutation on them to output a new individual with inherited dna and an incremented generation number.

### Representing the decimal values as dna

In GA's the values of a problem need to be partitioned into many units, this is so that cross-over and mutation can create new values by making slight changes to this structure.

I first considered using binary and as I wanted to represent real numbers in my search space I tried implementing a floating point binary structure.

![float diagram](./float_diagram.jpg?raw=true "Float diagram")

What became clear though was that the search space would be very large and that a small change in 1 bit of a float can dramatically change the value of the float; especially in the first 2 bytes of it.

Instead I decided to use a much more simplistic structure and I would convert a real number into an array of 8 characters (1 sign, 1 decimal place and 6 digits).

`["s", "x", "x", "x", ".", "x", "x", "x"]`

(where `x` are digits, `s` is the sign and the `.` is the decimal place)

So: `-111.222` would be `["-", "1", "1", "1", ".", "2", "2", "2"]`

With this system I have a search space between -999.999 and 999.999 which is accurate to 3 decimal places; which is fine for the problem.

### Actual iteration of the GA

- Create a population of random starting values in the search space.
  - `[0.100, 300.500, 120.000, 23.540, -964.000, -63.902]` (for example)
- For the amount of epochs/generations:
  - Sort the population by their value through with the fitness function.
    - fitnesses: `[-1.000, 39798.882, 359.632, -0.946, 0.000, -0.665]`
    - so sorted values are: `[0.100, 23.540, -63.902, -964.000, 120.000, 300.500]`
  - Remove the individuals from the population which are under the pass criteria (set by the `fitness_upper_bound`)
    - lets say that fitness upper-bound is top 4/6 so: `[0.100, 23.540, -63.902, -964.000]`
  - Then for the remaining population produce 6 new offspring by having 2 couples produce `2/fitness_upper_bound` offspring each (so 3).
    - selecting `0.100` and `23.540`
      - cross-over yields `3.500`
      - mutation changes this to `103.500`
      - The fore-mentioned happens another 2 times to produce: `103.500`, `23.1` and `0.34`
    - selecting `-63.902` and `-964.000`
      - cross-over yields `-963.900`
      - mutation changes this to `-903.900`
      - The fore-mentioned happens another 2 times to produce: `-903.900`, `-63.000` and `-974.002`
  - The next generations population is `[103.500, 23.1, 0.34, -903.900, -63.000, -974.002]` which replaces the old one.
