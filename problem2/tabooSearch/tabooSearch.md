# Taboo Search

_Source code: [notebook](./simulatedAnnealing.ipynb) or [python script](./simulatedAnnealing.py)_

Taboo search is deterministic so doesn't need to be run more than once for the same parameters, because its going to yield the same results.

## Abstract

The best solution I've found from running TS has been:
A = 0.0, B = 4.5, C = 0.75, D = 0.0 making a profit of 25.5; when I was testing starting position and looked into the highest profit value.

## Taboo search with default starting parameters

With the [default](./tabooSearch.py#L87) starting parameters, you get something like this:

```
(x3 not -ve constraint fails)
(x1 not -ve constraint fails)
(x4 not -ve constraint fails)
(x2 not -ve constraint fails)
Iteration: 1,	Current solution: {'x3': 0, 'x1': 0, 'x4': 0, 'x2': 0.1},	Taboo list: [{'x3': 0, 'x1': 0, 'x4': 0, 'x2': 0}, {'x3': 0, 'x1': 0, 'x4': 0, 'x2': 0.1}]
(x3 not -ve constraint fails)
(x1 not -ve constraint fails)
(x4 not -ve constraint fails)
Iteration: 2,	Current solution: {'x3': 0, 'x1': 0, 'x4': 0, 'x2': 0.2},	Taboo list: [{'x3': 0, 'x1': 0, 'x4': 0, 'x2': 0}, {'x3': 0, 'x1': 0, 'x4': 0, 'x2': 0.1}, {'x3': 0, 'x1': 0, 'x4': 0, 'x2': 0.2}]
(x3 not -ve constraint fails)
(x1 not -ve constraint fails)
(x4 not -ve constraint fails)
Iteration: 3,	Current solution: {'x3': 0, 'x1': 0, 'x4': 0, 'x2': 0.30000000000000004},	Taboo list: [{'x3': 0, 'x1': 0, 'x4': 0, 'x2': 0}, {'x3': 0, 'x1': 0, 'x4': 0, 'x2': 0.1}, {'x3': 0, 'x1': 0, 'x4': 0, 'x2': 0.2}, {'x3': 0, 'x1': 0, 'x4': 0, 'x2': 0.30000000000000004}]
(x3 not -ve constraint fails)
(x1 not -ve constraint fails)
(x4 not -ve constraint fails)
Iteration: 4,	Current solution: {'x3': 0, 'x1': 0, 'x4': 0, 'x2': 0.4},	Taboo list: [{'x3': 0, 'x1': 0, 'x4': 0, 'x2': 0}, {'x3': 0, 'x1': 0, 'x4': 0, 'x2': 0.1}, {'x3': 0, 'x1': 0, 'x4': 0, 'x2': 0.2}, {'x3': 0, 'x1': 0, 'x4': 0, 'x2': 0.30000000000000004}, {'x3': 0, 'x1': 0, 'x4': 0, 'x2': 0.4}]

(after 52 more iterations...)

Iteration: 56,	Current solution: {'x3': 0.7, 'x1': 0, 'x4': 0.1, 'x2': 4.5},	Taboo list: [{'x3': 0.30000000000000004, 'x1': 0, 'x4': 0, 'x2': 4.5}, {'x3': 0.4, 'x1': 0, 'x4': 0, 'x2': 4.5}, {'x3': 0.5, 'x1': 0, 'x4': 0, 'x2': 4.5}, {'x3': 0.6, 'x1': 0, 'x4': 0, 'x2': 4.5}, {'x3': 0.7, 'x1': 0, 'x4': 0, 'x2': 4.5}, {'x3': 0.7, 'x1': 0, 'x4': 0.1, 'x2': 4.5}, {'x3': 0.6, 'x1': 0, 'x4': 0.1, 'x2': 4.5}, {'x3': 0.7, 'x1': 0, 'x4': 0.1, 'x2': 4.4}]

Stats:
x1 not -ve constraint: 0 <= 0
x2 not -ve constraint: 0 <= 4.5
x3 not -ve constraint: 0 <= 0.7
x4 not -ve constraint: 0 <= 0.1
green constraint: 9.8 <= 10
red constraint: 6.0 <= 6
blue constraint: 4.5 <= 10
yellow constraint: 18.0 <= 18
brown constraint: 1.0 <= 8
purple constraint: 2.4 <= 12
Profit:  25.400000000000002
```

Taboo search in this problem is very effective off the bat, it goes for the best neighbour each iteration and as there aren't any local minima in this problem, because there is just the feasible region and the linear profit function; the taboo search is very effective at this problem and efficient as well.

## Changing the starting point

For this independant variable I tested a range of starting points in a spiral shape from (0, 0, 0, 0) outwards over 1000 points.

When it gave answers which were infeasible, because the algorithm started outside the feasible region, the profit was set to 0.

![TS](./profit_against_starting_point.png?raw=true "Profit against starting point.")

From (0, 0, 0, 0) and an area around this point, TS does worse maybe because the TS algorithm gets stuck at another cross over point between constraints.

<div class="page"/>

## Changing the step size

For this I tested a range of 20 step sizes from 0.05 to 1.0.

![TS](./profit_against_step_size.png?raw=true "Profit against starting point.")

The best step_sizes are those which divide into the best solution. These are: 0.05, 0.15, 0.25 & 0.75.

## Improved found solution

These are the constraint values for the best solution found.

```
x1 not -ve constraint: 0 <= 0
x2 not -ve constraint: 0 <= 4.499999999999992
x3 not -ve constraint: 0 <= 0.7500000000000001
x4 not -ve constraint: 0 <= 0
green constraint: 9.75 <= 10
red constraint: 6.0 <= 6
blue constraint: 4.5 <= 10
yellow constraint: 18.0 <= 18
brown constraint: 0.75 <= 8
purple constraint: 2.25 <= 12
Profit:  25.49999999999996
```

<div class="page"/>

## Conclusion

Taboo search is the best algorithm so far for maximising profit.

By having a neighbourhood of potential values, which are ranked by the profit function and being able to remove infeasible neighbours at the iteration level until you run out of feasible neighbours, it does exactly what is needed following the surface of the feasible region until its found the best solution.

Pros:

- Very efficient, taking very little time to zone in on solutions.
- Very accurate.

Cons:

- From bad starting positions can get stuck at sub-optimal solutions, although these are relatively much better than the other metaheuristics.
