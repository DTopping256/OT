# Simulated Annealing

_Source code: [notebook](./simulatedAnnealing.ipynb) or [python script](./simulatedAnnealing.py)_

Being stochastic, SA will create different graphs each time but they will be very similar with the same settings.

## Abstract

The best solution I've found from running SA has been:
A = 0.3, B = 2.9, C = 1.1, D = 0.1 making a profit of 19.9; when I was testing starting position and looked into the highest profit value.

## Simulated annealing with default starting parameters

With the [default](./simulatedAnnealing.py#L102) starting parameters, you get something like this:

```
----------------------------------------------------------------------------------
s_0: {'x3': 0, 'x4': 0, 'x1': 0, 'x2': 0}

Epoch: 1  s: {'x3': -0.1, 'x4': 0, 'x1': 0, 'x2': 0}        t: 5.0  Accepted: True  Diff: -0.4
Epoch: 2  s: {'x3': -0.1, 'x4': 0.1, 'x1': 0, 'x2': 0}      t: 5.0  Accepted: True  Diff: 0.1
Epoch: 3  s: {'x3': -0.1, 'x4': 0.1, 'x1': -0.1, 'x2': 0}   t: 5.0  Accepted: True  Diff: -0.3
Epoch: 4  s: {'x3': 0.0, 'x4': 0.1, 'x1': -0.1, 'x2': 0}    t: 5.0  Accepted: True  Diff: 0.4
Epoch: 5  s: {'x3': 0.0, 'x4': 0.0, 'x1': -0.1, 'x2': 0}    t: 5.0  Accepted: True  Diff: -0.1
Epoch: 6  s: {'x3': 0.1, 'x4': 0.0, 'x1': -0.1, 'x2': 0}    t: 5.0  Accepted: True  Diff: 0.4
Epoch: 7  s: {'x3': 0.1, 'x4': 0.0, 'x1': -0.2, 'x2': 0}    t: 5.0  Accepted: True  Diff: -0.3
Epoch: 8  s: {'x3': 0.1, 'x4': 0.1, 'x1': -0.2, 'x2': 0}    t: 5.0  Accepted: True  Diff: 0.1
(x1 not -ve constraint fails)

{'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0}
```

Simulated annealing in this problem is a lot more prone to random walk (we can see this by the rate of "Accepted" answers which have a negative difference). This is because the difference of a step are so low (±0.5 at most), however the step size cannot be increased too much since the search space is quite small.

<div class="page"/>

## Changing the starting point

For this independant variable I tested a range of starting points in a spiral shape from (0, 0, 0, 0) outwards over 1000 points. Each point was repeated 20 times (as the algorithm is stochastic) to get a general idea of consistency.

When it gave answers which were infeasible, because the algorithm started outside the feasible region, the profit was set to 0.

![SA](./profit_against_starting_point.png?raw=true "Profit against starting point.")

Good starting points (with profit above 16) included:

| Starting point           | End point            | Profit |
| ------------------------ | -------------------- | ------ |
| 754 (1.0, 1.0, 1.0, 0.4) | (0.5, 1.7, 0.8, 0.0) | 17.2   |
| 270 (0.6, 0.0, 0.6, 0.6) | (0.7, 0.3, 0.1, 0.4) | 16.3   |
| 269 (0.6, 0.1, 0.6, 0.6) | (0.6, 0.6, 0.2, 0.1) | 17.4   |

Average starting point: (0.733, 0.367, 0.733, 0.533)

Decided to round upto (0.7, 0.7, 0.7, 0.7) for future tests.

<div class="page"/>

## Changing starting temperature and temperature change

I tested 40 different gradients from 1/41 to 1 and I tested for each of those 30 starting temperatures from 0.2 to 6.

Each combination was repeated 10 times so that an overall trend could be observed.

![SA Temperature params 1](./profit_against_temp_params.png?raw=true "Profit against temperature params.")

![SA Temperature params 2](./profit_against_temp_grad.png?raw=true "Profit against temperature params.")

![SA Temperature params 3](./profit_against_start_temp.png?raw=true "Profit against temperature params.")

From the data, we can see that:

- Average profit was around 12.
- There was a much wider range of results as the temperature gradient increased.
- Start temperatures of less than 1 were the most consistent, however this is not where you tend find the best results.

I decided to use a high temperature gradient of 0.9 and a low starting temperature of 2, so that I had a slower increase of intensification from an already intenisfied starting temperature.

## Amount of epochs and step size

I decided to test the amount of epochs and step size together because per iteration these both contribute to the overall difference in profit because of the amount of movement of the solution.

I tested epoch amounts from 5 to 30 and for each of these tested step sizes from 1/40 to 3/4 (in increments of 1/40).

I repeated each combination 10 times.

![SA Temperature params 1](./profit_against_step_epoch_params.png?raw=true "Profit against temperature params.")

![SA Temperature params 2](./profit_against_epochs.png?raw=true "Profit against temperature params.")

![SA Temperature params 3](./profit_against_step_size.png?raw=true "Profit against temperature params.")

I have found that the most consistently good results have been found where there is low epochs per iteration and a small step size.

I fixed epochs to 10 and step size to 0.1.

<div class="page"/>

## Final run with improved parameters

```
----------------------------------------------------------------------------------
s_0: {'x4': 0.7, 'x2': 0.7, 'x3': 0.7, 'x1': 0.7}
Epoch: 1	s: {'x4': 0.7, 'x2': 0.7, 'x1': 0.6, 'x3': 0.7}    	t: 2	Accepted: True	Diff: -0.3
Epoch: 2	s: {'x4': 0.7, 'x2': 0.7, 'x1': 0.6, 'x3': 0.8}    	t: 2	Accepted: True	Diff: 0.4
Epoch: 3	s: {'x4': 0.7, 'x2': 0.6, 'x1': 0.6, 'x3': 0.8}    	t: 2	Accepted: True	Diff: -0.5
Epoch: 4	s: {'x4': 0.7, 'x2': 0.5, 'x1': 0.6, 'x3': 0.8}    	t: 2	Accepted: True	Diff: -0.5
Epoch: 5	s: {'x4': 0.8, 'x2': 0.5, 'x1': 0.6, 'x3': 0.8}    	t: 2	Accepted: True	Diff: 0.1
Epoch: 6	s: {'x4': 0.8, 'x2': 0.4, 'x1': 0.6, 'x3': 0.8}    	t: 2	Accepted: False	Diff: -0.5
Epoch: 7	s: {'x4': 0.8, 'x2': 0.4, 'x1': 0.6, 'x3': 0.8}    	t: 2	Accepted: True	Diff: -0.5
Epoch: 8	s: {'x4': 0.9, 'x2': 0.4, 'x1': 0.6, 'x3': 0.8}    	t: 2	Accepted: True	Diff: 0.1
Epoch: 9	s: {'x4': 0.9, 'x2': 0.4, 'x1': 0.5, 'x3': 0.8}    	t: 2	Accepted: True	Diff: -0.3
Epoch: 10	s: {'x4': 0.9, 'x2': 0.4, 'x1': 0.5, 'x3': 0.9}    	t: 2	Accepted: True	Diff: 0.4
----------------------------------------------------------------------------------
s_1: {'x4': 0.9, 'x2': 0.4, 'x3': 0.9, 'x1': 0.5}
Epoch: 1	s: {'x4': 0.9, 'x2': 0.5, 'x1': 0.5, 'x3': 0.9}    	t: 1.8	Accepted: True	Diff: 0.5
Epoch: 2	s: {'x4': 0.9, 'x2': 0.5, 'x1': 0.5, 'x3': 0.8}    	t: 1.8	Accepted: True	Diff: -0.4
Epoch: 3	s: {'x4': 0.9, 'x2': 0.5, 'x1': 0.6, 'x3': 0.8}    	t: 1.8	Accepted: True	Diff: 0.3
Epoch: 4	s: {'x4': 0.9, 'x2': 0.4, 'x1': 0.6, 'x3': 0.8}    	t: 1.8	Accepted: True	Diff: -0.5
Epoch: 5	s: {'x4': 1.0, 'x2': 0.4, 'x1': 0.6, 'x3': 0.8}    	t: 1.8	Accepted: True	Diff: 0.1
Epoch: 6	s: {'x4': 1.0, 'x2': 0.5, 'x1': 0.6, 'x3': 0.8}    	t: 1.8	Accepted: True	Diff: 0.5
Epoch: 7	s: {'x4': 1.0, 'x2': 0.5, 'x1': 0.5, 'x3': 0.8}    	t: 1.8	Accepted: True	Diff: -0.3
Epoch: 8	s: {'x4': 1.0, 'x2': 0.5, 'x1': 0.5, 'x3': 0.9}    	t: 1.8	Accepted: True	Diff: 0.4
Epoch: 9	s: {'x4': 1.1, 'x2': 0.5, 'x1': 0.5, 'x3': 0.9}    	t: 1.8	Accepted: True	Diff: 0.1
Epoch: 10	s: {'x4': 1.1, 'x2': 0.6, 'x1': 0.5, 'x3': 0.9}    	t: 1.8	Accepted: True	Diff: 0.5
----------------------------------------------------------------------------------
s_2: {'x4': 1.1, 'x2': 0.6, 'x3': 0.9, 'x1': 0.5}
Epoch: 1	s: {'x4': 1.1, 'x2': 0.6, 'x1': 0.4, 'x3': 0.9}    	t: 1.62	Accepted: False	Diff: -0.3
Epoch: 2	s: {'x4': 1.1, 'x2': 0.5, 'x1': 0.5, 'x3': 0.9}    	t: 1.62	Accepted: False	Diff: -0.5
Epoch: 3	s: {'x4': 1.1, 'x2': 0.6, 'x1': 0.5, 'x3': 0.8}    	t: 1.62	Accepted: True	Diff: -0.4
Epoch: 4	s: {'x4': 1.1, 'x2': 0.5, 'x1': 0.5, 'x3': 0.8}    	t: 1.62	Accepted: True	Diff: -0.5
Epoch: 5	s: {'x4': 1.1, 'x2': 0.5, 'x1': 0.5, 'x3': 0.9}    	t: 1.62	Accepted: True	Diff: 0.4
Epoch: 6	s: {'x4': 1.1, 'x2': 0.5, 'x1': 0.6, 'x3': 0.9}    	t: 1.62	Accepted: True	Diff: 0.3
Epoch: 7	s: {'x4': 1.1, 'x2': 0.4, 'x1': 0.6, 'x3': 0.9}    	t: 1.62	Accepted: True	Diff: -0.5
Epoch: 8	s: {'x4': 1.1, 'x2': 0.5, 'x1': 0.6, 'x3': 0.9}    	t: 1.62	Accepted: True	Diff: 0.5
Epoch: 9	s: {'x4': 1.1, 'x2': 0.5, 'x1': 0.5, 'x3': 0.9}    	t: 1.62	Accepted: True	Diff: -0.3
Epoch: 10	s: {'x4': 1.1, 'x2': 0.5, 'x1': 0.5, 'x3': 1.0}    	t: 1.62	Accepted: True	Diff: 0.4
----------------------------------------------------------------------------------
s_3: {'x4': 1.1, 'x2': 0.5, 'x3': 1.0, 'x1': 0.5}
Epoch: 1	s: {'x4': 1.2, 'x2': 0.5, 'x1': 0.5, 'x3': 1.0}    	t: 1.458	Accepted: True	Diff: 0.1
Epoch: 2	s: {'x4': 1.2, 'x2': 0.6, 'x1': 0.5, 'x3': 1.0}    	t: 1.458	Accepted: True	Diff: 0.5
Epoch: 3	s: {'x4': 1.1, 'x2': 0.6, 'x1': 0.5, 'x3': 1.0}    	t: 1.458	Accepted: True	Diff: -0.1
Epoch: 4	s: {'x4': 1.1, 'x2': 0.6, 'x1': 0.5, 'x3': 0.9}    	t: 1.458	Accepted: False	Diff: -0.4
Epoch: 5	s: {'x4': 1.1, 'x2': 0.6, 'x1': 0.5, 'x3': 1.1}    	t: 1.458	Accepted: True	Diff: 0.4
Epoch: 6	s: {'x4': 1.1, 'x2': 0.6, 'x1': 0.4, 'x3': 1.1}    	t: 1.458	Accepted: True	Diff: -0.3
Epoch: 7	s: {'x4': 1.1, 'x2': 0.6, 'x1': 0.4, 'x3': 1.2}    	t: 1.458	Accepted: True	Diff: 0.4
Epoch: 8	s: {'x4': 1.2, 'x2': 0.6, 'x1': 0.4, 'x3': 1.2}    	t: 1.458	Accepted: True	Diff: 0.1
Epoch: 9	s: {'x4': 1.2, 'x2': 0.5, 'x1': 0.4, 'x3': 1.2}    	t: 1.458	Accepted: True	Diff: -0.5
Epoch: 10	s: {'x4': 1.3, 'x2': 0.5, 'x1': 0.4, 'x3': 1.2}    	t: 1.458	Accepted: True	Diff: 0.1
----------------------------------------------------------------------------------
s_4: {'x4': 1.3, 'x2': 0.5, 'x3': 1.2, 'x1': 0.4}
Epoch: 1	s: {'x4': 1.3, 'x2': 0.5, 'x1': 0.4, 'x3': 1.3}    	t: 1.312	Accepted: True	Diff: 0.4
Epoch: 2	s: {'x4': 1.3, 'x2': 0.5, 'x1': 0.3, 'x3': 1.3}    	t: 1.312	Accepted: True	Diff: -0.3
Epoch: 3	s: {'x4': 1.3, 'x2': 0.4, 'x1': 0.3, 'x3': 1.3}    	t: 1.312	Accepted: True	Diff: -0.5
Epoch: 4	s: {'x4': 1.3, 'x2': 0.4, 'x1': 0.3, 'x3': 1.4}    	t: 1.312	Accepted: True	Diff: 0.4
Epoch: 5	s: {'x4': 1.3, 'x2': 0.3, 'x1': 0.3, 'x3': 1.4}    	t: 1.312	Accepted: False	Diff: -0.5
Epoch: 6	s: {'x4': 1.3, 'x2': 0.4, 'x1': 0.2, 'x3': 1.4}    	t: 1.312	Accepted: True	Diff: -0.3
Epoch: 7	s: {'x4': 1.2, 'x2': 0.4, 'x1': 0.2, 'x3': 1.4}    	t: 1.312	Accepted: True	Diff: -0.1
Epoch: 8	s: {'x4': 1.2, 'x2': 0.5, 'x1': 0.2, 'x3': 1.4}    	t: 1.312	Accepted: True	Diff: 0.5
Epoch: 9	s: {'x4': 1.2, 'x2': 0.5, 'x1': 0.1, 'x3': 1.4}    	t: 1.312	Accepted: True	Diff: -0.3
Epoch: 10	s: {'x4': 1.2, 'x2': 0.5, 'x1': 0.1, 'x3': 1.5}    	t: 1.312	Accepted: True	Diff: 0.4
----------------------------------------------------------------------------------
s_5: {'x4': 1.2, 'x2': 0.5, 'x3': 1.5, 'x1': 0.1}
Epoch: 1	s: {'x4': 1.2, 'x2': 0.6, 'x1': 0.1, 'x3': 1.5}    	t: 1.181	Accepted: True	Diff: 0.5
Epoch: 2	s: {'x4': 1.2, 'x2': 0.6, 'x1': 0.1, 'x3': 1.6}    	t: 1.181	Accepted: True	Diff: 0.4
Epoch: 3	s: {'x4': 1.2, 'x2': 0.6, 'x1': 0.2, 'x3': 1.6}    	t: 1.181	Accepted: True	Diff: 0.3
Epoch: 4	s: {'x4': 1.2, 'x2': 0.6, 'x1': 0.2, 'x3': 1.7}    	t: 1.181	Accepted: True	Diff: 0.4
Epoch: 5	s: {'x4': 1.2, 'x2': 0.6, 'x1': 0.2, 'x3': 1.6}    	t: 1.181	Accepted: True	Diff: -0.4
Epoch: 6	s: {'x4': 1.2, 'x2': 0.7, 'x1': 0.2, 'x3': 1.6}    	t: 1.181	Accepted: True	Diff: 0.5
Epoch: 7	s: {'x4': 1.2, 'x2': 0.7, 'x1': 0.1, 'x3': 1.6}    	t: 1.181	Accepted: True	Diff: -0.3
Epoch: 8	s: {'x4': 1.2, 'x2': 0.7, 'x1': 0.1, 'x3': 1.5}    	t: 1.181	Accepted: False	Diff: -0.4
Epoch: 9	s: {'x4': 1.2, 'x2': 0.7, 'x1': 0.1, 'x3': 1.7}    	t: 1.181	Accepted: True	Diff: 0.4
Epoch: 10	s: {'x4': 1.1, 'x2': 0.7, 'x1': 0.1, 'x3': 1.7}    	t: 1.181	Accepted: True	Diff: -0.1
----------------------------------------------------------------------------------
s_6: {'x4': 1.1, 'x2': 0.7, 'x3': 1.7, 'x1': 0.1}
Epoch: 1	s: {'x4': 1.1, 'x2': 0.8, 'x1': 0.1, 'x3': 1.7}    	t: 1.063	Accepted: True	Diff: 0.5
Epoch: 2	s: {'x4': 1.1, 'x2': 0.7, 'x1': 0.1, 'x3': 1.7}    	t: 1.063	Accepted: True	Diff: -0.5
Epoch: 3	s: {'x4': 1.1, 'x2': 0.6, 'x1': 0.1, 'x3': 1.7}    	t: 1.063	Accepted: False	Diff: -0.5
Epoch: 4	s: {'x4': 1.2, 'x2': 0.7, 'x1': 0.1, 'x3': 1.7}    	t: 1.063	Accepted: True	Diff: 0.1
Epoch: 5	s: {'x4': 1.1, 'x2': 0.7, 'x1': 0.1, 'x3': 1.7}    	t: 1.063	Accepted: True	Diff: -0.1
Epoch: 6	s: {'x4': 1.2, 'x2': 0.7, 'x1': 0.1, 'x3': 1.7}    	t: 1.063	Accepted: True	Diff: 0.1
Epoch: 7	s: {'x4': 1.2, 'x2': 0.8, 'x1': 0.1, 'x3': 1.7}    	t: 1.063	Accepted: True	Diff: 0.5
Epoch: 8	s: {'x4': 1.2, 'x2': 0.8, 'x1': 0.1, 'x3': 1.8}    	t: 1.063	Accepted: True	Diff: 0.4
Epoch: 9	s: {'x4': 1.2, 'x2': 0.7, 'x1': 0.1, 'x3': 1.8}    	t: 1.063	Accepted: False	Diff: -0.5
Epoch: 10	s: {'x4': 1.2, 'x2': 0.8, 'x1': 0.1, 'x3': 1.9}    	t: 1.063	Accepted: True	Diff: 0.4
(red constraint fails)

Stats:
x1 not -ve constraint: 0 <= 0.10000000000000003
x2 not -ve constraint: 0 <= 0.7
x3 not -ve constraint: 0 <= 1.7000000000000004
x4 not -ve constraint: 0 <= 1.0999999999999999
green constraint: 4.3 <= 10
red constraint: 5.4 <= 6
blue constraint: 1.0 <= 10
yellow constraint: 2.9 <= 18
brown constraint: 5.0 <= 8
purple constraint: 8.4 <= 12

Profit: 11.700000000000001
Solution: [0.1, 0.7, 1.7, 1.1]
```

## Conclusion

Although I managed to tune the parameters to fail and stop on a wool constraint instead of a non negative constraint; the simulated annealing algorithm seems to still be very inconsistent in finding good profit values.

Pros:

- Fairly quick.
- Can be tuned to increase intensification.

Cons:

- With small differences acts very randomly.
