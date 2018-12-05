[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/DTopping256/OT/master)
# Optimisation Techniques

This repository contains python and jupyter notebook files which can be opened in a Jupyter notebook environment (or viewed on Github.com), as well as executable python scripts which build graphs (which may take a while to load). For convenience, I have included saved stills of the graphs which can take a long time to create.

## Problem 1

### Summary

![Problem function](./problem1/problemFunction.png?raw=true "Problem function")

I defined this in the [problem_function](./modules/problem_function.py) module which I import in all my metaheuristics code.

It plots this graph:

![f(x)](./problem1/simulatedAnnealing/f.png?raw=true "f(x)")

Where there is a local minimum (a very shallow one on this scale) at `x = 0` and a global minimum at `x = 101`; so the best solution is 101.

### Solving the problem

The metaheuristics used were the following:

#### [Gradient Descent](./problem1/gradientDescent/gradientDescent.md)

#### [Simulated Annealing](./problem1/simulatedAnnealing/simulatedAnnealing.md)

#### [Taboo Search](./problem1/tabooSearch/tabooSearch.md)

#### [Genetic Algorithm](./problem1/geneticAlgorithms/geneticAlgorithms.md)

## Problem 2

### Summary

In a cloth factory there are 4 types of cloth to produce (A, B, C and D), producing a type of cloth requires a combination of different amounts of coloured wool and there is a finite amount of each wool.

|Wool colour|A|B|C|D|Wool available|
|-----------|-|-|-|-|--------------|
|Green      |1|2|1|1|10            |
|Red        |2|1|2|1|6             |
|Blue       |3|1|0|0|10            |
|Yellow     |1|4|0|0|18            |
|Brown      |0|0|1|3|8             |
|Purple     |0|0|3|3|12            |

The different cloths yield different amounts of profit

|Cloth|Profit|
|-----|------|
|A    |3     |
|B    |5     |
|C    |4     |
|D    |1     |

These can be modelled into the following Linear Programming model:

![Linear Programming Model](./problem2/model.png?raw=true "Linear programming model")

The best solution I've found is

### Solving the problem

The metaheuristics used were the following:

#### [Gradient Descent](./problem2/gradientDescent/gradientDescent.md)

#### [Simulated Annealing](./problem2/simulatedAnnealing/simulatedAnnealing.md)

#### [Taboo Search](./problem2/tabooSearch/tabooSearch.md)

#### [Genetic Algorithm](./problem2/geneticAlgorithm/geneticAlgorithm.md)
