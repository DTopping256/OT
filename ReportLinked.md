# Technical report

## Problem 1

### Abstract

<img class="default_img_res" src="./problem1/problemFunction.png?raw=true"/>

I defined this in the [problem_function](./modules/problem_function.py) module which I import in all my metaheuristics code.

It plots this graph:

![f(x)](./problem1/f.png?raw=true "f(x)")

### Best solution (found)

Where there is a local minimum (a very shallow one on this scale) at `x = 0` and a global minimum at `x = 101`; so the best solution is 101.

I find both of these minima when testing each of the metaheuristics. I have written the code to each metaheuristic and put it into the `metaheuristics` python module.

### Best metaheuristic

**Genetic algorithms** seem best suited to solving this problem as they find both minima to a high degree of accuracy and it doesn't take much computational power for this problem.

<div class="page"/>

### Solving the problem

The metaheuristics used were the following:

#### [Gradient Descent](./problem1/gradientDescent/gradientDescent.pdf)

#### [Simulated Annealing](./problem1/simulatedAnnealing/simulatedAnnealing.pdf)

#### [Taboo Search](./problem1/tabooSearch/tabooSearch.pdf)

#### [Genetic Algorithm](./problem1/geneticAlgorithm/geneticAlgorithm.pdf)

## Problem 2

### Summary

In a cloth factory there are 4 types of cloth to produce (A, B, C and D), producing a type of cloth requires a combination of different amounts of coloured wool and there is a finite amount of each wool.

| Wool colour | A   | B   | C   | D   | Wool available |
| ----------- | --- | --- | --- | --- | -------------- |
| Green       | 1   | 2   | 1   | 1   | 10             |
| Red         | 2   | 1   | 2   | 1   | 6              |
| Blue        | 3   | 1   | 0   | 0   | 10             |
| Yellow      | 1   | 4   | 0   | 0   | 18             |
| Brown       | 0   | 0   | 1   | 3   | 8              |
| Purple      | 0   | 0   | 3   | 3   | 12             |

The different cloths yield different amounts of profit

| Cloth | Profit |
| ----- | ------ |
| A     | 3      |
| B     | 5      |
| C     | 4      |
| D     | 1      |

These can be modelled into the following Linear Programming model:

![Linear Programming Model](./problem2/model.png?raw=true "Linear programming model")

### Best solution (found)

The best solution I've found during testing has been **A = 0.0, B = 4.5, C = 0.75 & D = 0.0** for a profit of **25.5**. This is also the solution which I found by running simplex on the problem ([see notebook](./problem2/simplex.ipynb)).

Only Taboo Search and Genetic Algorithms found this answer out of the metaheuristics I used.

### Best metaheuristic

**Taboo search** consistently finds the best solution (with the right parameters) with very little computational power needed. The next best was GA but this required high computation and it wasn't 100% accurate.

#### [Gradient Descent](./problem2/gradientDescent/gradientDescent.pdf)

#### [Simulated Annealing](./problem2/simulatedAnnealing/simulatedAnnealing.pdf)

#### [Taboo Search](./problem2/tabooSearch/tabooSearch.pdf)

#### [Genetic Algorithm](./problem2/geneticAlgorithm/geneticAlgorithm.pdf)
