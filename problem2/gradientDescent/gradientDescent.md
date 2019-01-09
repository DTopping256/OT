# Gradient Descent

_Source code: [notebook](./gradientDescent.ipynb) or [python script](./gradientDescent.py)_

Gradient descent is deterministic so doesn't need to be run more than once for the same parameters, because its going to yield the same results.

## Abstract

### Default gradient descent

With the [default](./simulatedAnnealing.py#L102) starting parameters, you get something like this:

```
----------------------------------------------------------------------------------
Iteration             X                         g	        diff
Start (0)             (0, 0, 0, 0)	        (3, 5, 4, 1)	N/A
1		      (0.3, 0.5, 0.4, 0.1)	(3, 5, 4, 1)	0.714
2		      (0.6, 1.0, 0.8, 0.2)	(3, 5, 4, 1)	0.714
3		      (0.9, 1.5, 1.2, 0.3)	(3, 5, 4, 1)	0.714
4		      (1.2, 2.0, 1.6, 0.4)	(3, 5, 4, 1)	0.714
```
