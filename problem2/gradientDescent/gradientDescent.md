# Gradient Descent

_Source code: [notebook](./gradientDescent.ipynb) or [python script](./gradientDescent.py)_

Gradient descent is deterministic so doesn't need to be run more than once for the same parameters, because its going to yield the same results.

## Abstract

The best solution I've found from GD has been A = 1.2, B = 2.0, C = 1.6, D = 0.4 making a profit of 15.3. This is the solution of the algorithm from a starting position of (0, 0, 0, 0).

### Default gradient descent

With the [default](./gradientDescent.py#L106) starting parameters, you get something like this:

```
----------------------------------------------------------------------------------
Iteration             X                         g	        diff
Start (0)             (0, 0, 0, 0)	        (3, 5, 4, 1)	N/A
1		      (0.3, 0.5, 0.4, 0.1)	(3, 5, 4, 1)	0.714
2		      (0.6, 1.0, 0.8, 0.2)	(3, 5, 4, 1)	0.714
3		      (0.9, 1.5, 1.2, 0.3)	(3, 5, 4, 1)	0.714
4		      (1.2, 2.0, 1.6, 0.4)	(3, 5, 4, 1)	0.714

x1 not -ve constraint: 0 <= 0.9
x2 not -ve constraint: 0 <= 1.5
x3 not -ve constraint: 0 <= 1.2
x4 not -ve constraint: 0 <= 0.3
green constraint: 5.4 <= 10
red constraint: 6.0 <= 6
blue constraint: 4.2 <= 10
yellow constraint: 6.9 <= 18
brown constraint: 2.1 <= 8
purple constraint: 4.5 <= 12
Profit:  15.3
```

Gradient descent on a linear multivariable function gives you partial derivatives which are constants. So you don't have a decreasing step size and you don't have the stop condition being satisfied until either a constraint is being hit or the maximum iterations has been reached; not from a gradient or difference tolerance being reached.

## Changing starting point

For this independant variable I tested a range of starting points in a spiral shape from (0, 0, 0, 0) outwards over 1000 points.

When it gave answers which were infeasible, because the algorithm started outside the feasible region, the profit was set to 0.

![GD](./profit_with_starting_point.png?raw=true "Profit against starting point.")

The best starting position is (0, 0, 0, 0)

## Changing step multiplier

I tested 100 step_m values from 0.01 to 1.0.

Again, infeasible answers were set to 0.

![GD](./profit_with_step_m.png?raw=true "Profit against step multipliers.")

0.01, 0.02, 0.03, 0.05, 0.06, 0.1, 0.15 and 0.3 give you the profit of 15.3. The rest get you lower profits from the end of the feasible region being undershot.

## Conclusion

Because of the linear nature of the profit line, the constant gradient in the gradient descent algorithm removes a large amount of the effectivness of this algorithm.

It just goes in one direction until the constraints are hit and the algorithm has no way of following the edge of this feasible region until it finds a path further up the profit function.
