# Simulated Annealing

_Source code: [notebook](./simulatedAnnealing.ipynb) or [python script](./simulatedAnnealing.py)_

Being stochastic, SA will create different graphs each time but they will be very similar with the same settings.

## Abstract

I have made a generalised `simulated_annealing` function in the [metaheuristics module](../../modules/metaheuristics.py#L53) which can take in many parameters.

Throughout testing I found that the 2 minima picked up by simulated annealing are 0 and 101, and I have shown that 101 is the best solution out of the two; so for the rest of this I will refer to 101 as the global minimum and 0 as the local minimum.

<hr />

## Parameters which find the best solution

With the [default](./simulatedAnnealing.py#L142) starting parameters, you get something like this:

![SA (wide)](./simulated_annealing_on_f_with_start_vars_wide.png?raw=true "SA (wide)")

![SA (close)](./simulated_annealing_on_f_with_start_vars_close.png?raw=true "SA (close)")

You can see that the simulated annealing can and does often start to overshoot but with the right parameters it eventually finds the global minimum. However, this isn't the case for a lot of combinations of parameters as we will see.

<hr />

## The algorithm by hand (first few iterations)

Starting with the [default](./simulatedAnnealing.py#L142) parameters:

- `f`: the problem 1 function (imported from [problem_function](../../modules/problem_function.py) module)
- `s_0`: 120
- `t_0`: 1000
- `neighbourhood_func`: returns the points either side of s by a step size of 0.1 (returns `[x - 0.1, x + 0.1]`)
- `temp_reduc_func`: returns 75% of the current temperature, `t`.
- `acc_prob_func`: uses the Boltzman distribution to return an acceptance probability of picking a "worse step" (Henderson. D, et al, 2003).
- `stop_cond`: returns `True` when the current iteration reaches the `max_i` variable.
- `max_i`: 50
- `max_epoch`: 50

_Further descriptions of what the parameters mean and how they are used in the algorithm can be found in the [source code](./simulatedAnnealing.py#L29)._

### Algorithm workings

- Set up local variables
  - Iteration counter (`i`) = 0
  - Current solution (`s`) = `s_0`
  - Current temperature (`t`) = `t_0`
- Check stop condition _(`i` (0) is not equal to `max_i` (50))_ so do loop:
  - for number of epochs (`max_epoch`) do loop:
    - get neighbourhood: [119.9, 120.1]
    - pick one solution from the neighbourhood at random: s_1 = 120.1
    - find the difference of this f(s) from previous: f(s_1) - f(s_0) = 363.44 - 359.63 = 3.81
    - as diff < 0 is not true, calculate the acceptance probability: acc_prob = 1.00
    - get a random number (0.12) from 0-1, as acc_prob > random_number s_1 is accepted
  - repeat for epoch 2
    - get neighbourhood: [120, 120.2]
    - pick one solution from the neighbourhood at random: s_2 = 120
    - find the difference of this f(s) from previous: f(s_2) - f(s_1) = 359.63 - 363.44 = -3.81
    - as diff < 0 is true s_2 is accepted
  - repeat for epoch 3
    - get neighbourhood: [119.9 120.1]
    - pick one solution from the neighbourhood at random: s_3 = 119.9
    - find the difference of this f(s) from previous: f(s_3) - f(s_2) = 355.84 - 359.63 = -3.79
    - as diff < 0 is true s_3 is accepted
  - repeat for epoch 4
    - get neighbourhood: [119.8, 120]
    - pick one solution from the neighbourhood at random: s_4 = 120
    - find the difference of this f(s) from previous:f(s_4) - f(s_3) = 359.63 - 355.84 = 3.79
    - as diff < 0 is not true, calculate the acceptance probability: acc_prob = 1.00
    - get a random number (0.83) from 0-1, as acc_prob > random_number s_4 is accepted
  - ... _(after 50 epochs we get to something like 119.8 as at a high acceptance probability a step up and step down are both very likely)_
  - Reduce `t`: 1000 x 0.75 = 750
  - Increment iteration counter: `i = i + 1`
- Check stop condition _(`i` (1) is not equal to `max_i` (50))_ so do loop:
  - for number of epochs (`max_epoch`) do loop:
    - get neighbourhood: [119.7, 119.9]
    - pick one solution from the neighbourhood at random: s_1 = 119.7
    - find the difference of this f(s) from previous: f(s_1) - f(s_0) = 348.32 - 352.07 = -3.75
    - as diff < 0 is true, s_1 is accepted
  - repeat for epoch 2
    - get neighbourhood: [119.6, 119.8]
    - pick one solution from the neighbourhood at random: s_2 = 119.8
    - find the difference of this f(s) from previous: f(s_2) - f(s_1) = 352.07 - 348.32 = 3.75
    - as diff < 0 is not true, calculate the acceptance probability: acc_prob = 1.00
    - get a random number (0.79) from 0-1, as acc_prob > random_number s_2 is accepted
  - repeat for epoch 3
    - get neighbourhood: [119.7 119.9]
    - pick one solution from the neighbourhood at random: s_3 = 119.9
    - find the difference of this f(s) from previous: f(s_3) - f(s_2) = 355.84 - 352.07 = 3.77
    - as diff < 0 is not true, calculate the acceptance probability: acc_prob = 0.99
    - get a random number (0.99) from 0-1, as acc_prob > random_number s_3 is accepted
  - repeat for epoch 4
    - get neighbourhood: [119.8, 120]
    - pick one solution from the neighbourhood at random: s_4 = 120
    - find the difference of this f(s) from previous: f(s_4) - f(s_3) = 359.63 - 355.84 = 3.79
    - as diff < 0 is not true, calculate the acceptance probability: acc_prob = 0.99
    - get a random number (0.99) from 0-1, as acc_prob > random_number s_4 is accepted
  - ... _(after 50 epochs we get to something like 121.0 as at a high acceptance probability a step up and step down are both very likely)_
  - Reduce `t`: 750 x 0.75 = 562.5
  - Increment iteration counter: `i = i + 1`
- ... _And so on for 50 iterations_

_Over time the epochs will tend to choose decreasing values, minimising the difference, because the temperature will decrease and reduce the acceptance probability (of solutions with positive differences)._

See the notebook for a real log of the whole algorithm.

<hr />

## Changing the starting point (s_0)

For this independant variable I tested a range of starting points from -5 to 120.

![SA](./variable_starting_point_scatter.png?raw=true "result scatter")

![SA](./variable_starting_point_scatter_sds.png?raw=true "standard deviation scatter")

Values of 90 < x < 200 are a good start point for the model (with these other starting settings); however with a starting point of x < 90 the model does tend to fall towards the local minimum at x = 0, and with a start x > 200 the start point is too far from the solution with these parameters.

<hr />

## Adjusting temperature variables (t_0 & the cooling function)

For this, since the gradient of the problem function at the starting point itself affects the general direction of where the simulated annealing will end up (as shown above), I did 3 batch tests with s_0: at 80, 101 and 120.

For this my independant variables were:

- The starting temperature, tested with 50 values from 1 to 981
- The gradient of the "linear" cooling function `c(x) -> gx` (where g is the temperature gradient), testing with 50 values from 1/52 to 50/52 (~0.02 to ~0.96)

### s_0 = 80

![SA](./s0_80_temperature_scatter.png?raw=true "result scatter s_0 = 80")

- This shows that very very little simulated annealing attempts starting at 80 finished near 101.
- Start temperature didn't seem to have a big affect on the algorithm as the results for when a certain temperature gradient is constant are largely, very similar.
- Temperature gradient had a massive affect with:
  - `g < 0.5` creating a very quick cooling of temperature and intensifying the search (with very low acceptance probability for non minimising neighbour solutions).
  - `0.5 < g < 0.75` allows for a bit more diversification of the results but as these end up lower than 80 a net minimising towards the local min at 0 is taking place.
  - `g > 0.75` seems like there is very little temperature loss, creating random like results around 80 (start point) even for low starting temperatures (with the execption of temperatures where `t_0 < 10` it seems)

![SA](./s0_80_temperature_scatter_sds.png?raw=true "sd scatter s_0 = 80")

The above uses the same data but the z-axis is standard deviation from 101, to get some measure for accuracy of the test to the global minimum.

- This showed that even very extreme temperature settings couldn't compensate for the starting position at 80.

### s_0 = 101 (starting at the global minimum)

![SA](./s0_101_temperature_scatter.png?raw=true "result scatter s_0 = 101")

- It seems that when you start near the global minimum irrespective of temperature the majority of results will stay nearby (for this function).
- Quite a few did jump out of the global minomum though and travel down towards the local minimum at 0.
- The temperature gradient again strongly influenced how far the solution moved from the start, with lower gradients travelling quite far to 0 and higher ones staying near to 101.
- Again starting temperature `t_0` didn't have much of an affect upon the end result, although it is more likely that for the first epochs high temperature models will jump out of the global minimum and might end up travelling to 0.

![SA](./s0_101_temperature_scatter_sds.png?raw=true "sd scatter s_0 = 101")

The above uses the same data but the z-axis is standard deviation from 101, to get some measure for accuracy of the test to the global minimum.

### s_0 = 120

![SA](./s0_120_temperature_scatter.png?raw=true "result scatter s_0 = 120")

- The majority of results on this start will tend towards 101 because of the
- Start temperature didn't seem to have a big affect on the algorithm as the results for when a certain temperature gradient is constant are largely, very similar.
- Temperature gradient had a massive affect with:
  - `g < 0.5` creating a very quick cooling of temperature and intensifying the search (with very low acceptance probability for non minimising neighbour solutions).
  - `0.5 < g < 0.75` allows for a bit more diversification of the results but as these end up lower than 80 a net minimising towards the local min at 0 is taking place.#
  - `g > 0.75` seems like there is very little temperature loss, creating random like results around 80 (start point) even for low starting temperatures (with the execption of temperatures where `t_0 < 10` it seems)

![SA](./s0_120_temperature_scatter_sds.png?raw=true "sd scatter s_0 = 120")

The above uses the same data but the z-axis is standard deviation from 120, to get some measure for accuracy of the test to the global minimum.

<hr />

## Neighbourhood function

So far, a neighbourhood of `[x - 0.1, x + 0.1]` has been used.

For this test I've adapted the neighbourhood function so that the parameters include a variable step size and variable amount of pairs of steps around x.

Such that:

- step size 0.1, with 2 pairs around x of 1 would yield: `[x - (2 x 0.1), x - (1 x 0.1), x + (1 x 0.1), x + (2 x 0.1)] = [0.8, 0.9, 1.1, 1.2]`
- step size 1, with 3 pairs around x of 5 would yield: `[x - (3 x 1), x - (2 x 1), x - (1 x 1), x + (1 x 1), x + (2 x 1), x + (3 x 1)] = [2, 3, 4, 6, 7, 8]`

Again, I did 3 batch tests with s_0 at: 80, 101 and 120.

### s_0 = 80

![SA](./s0_80_nh_scatter.png?raw=true "result scatter s_0 = 80")

Observations:

- The majority of results occur at 0 (a local minima)
- A combination of small step size and less neighbourhood pairs, decrease the search space around the starting point; so the end result is closer to the start. (you can see this because the result curves up towards 80 nearer to a step size of 0.00 & a neighbourhood pairs of 1)
- When the step size & neighbourhood becomes too large the results can become less reliable (the various outliers around a step of 1.75-2.00 and neighbourhood pairs of 6-10)

![SA](./s0_80_nh_scatter_sd.png?raw=true "sd scatter s_0 = 80")

- The highest accuracy was from the small step size and small neighbourhood SA tests.
- Even with large neighbourhoods small step size can keep the results quite intensified around the start.

### s_0 = 101

![SA](./s0_101_nh_scatter.png?raw=true "result scatter s_0 = 101")

Observations:

- The majority of results again occur at 0 (a local minima), even though the tests started at a global minima
- There are a larger amount of results at the global minima though since tests started on the global minima

![SA](./s0_101_nh_scatter_sd.png?raw=true "sd scatter s_0 = 101")

- The highest accuracy was from the small step size and small neighbourhood SA tests.
- Neighbourhood values of 2 with a smaller step perform best and steps closer to 0.1 with small neighbourhoods perform best. Otherwise results tend to jump out of the global minima and end up at the local minima.
- Large step size and large numbers of neighbourhood pairs again created outliers which didn't find any minima.

### s_0 = 120

![SA](./s0_120_nh_scatter.png?raw=true "result scatter s_0 = 120")

Observations:

- The majority of results again occur at 0 (a local minima)
- There are a larger amount of results at the global minima though since tests had to step past the global minima to get to the local minima.

![SA](./s0_120_nh_scatter_sd.png?raw=true "sd scatter s_0 = 120")

- The highest accuracy was from the small step size and small neighbourhood SA tests.
- Neighbourhood values of 2 with a smaller step perform best and steps closer to 0.1 with small neighbourhoods perform best. Otherwise results tend to jump out of the global minima and end up at the local minima.
- Large step size and large numbers of neighbourhood pairs again created outliers which didn't find any minima.

<hr />

## Stop condition

Up until now an iteration based stop condition has been used.

We will now experiment with various stop condition functions when batch tested over different max_epoch and max_iteration values, these stop conditions are:

- Stop when reaching max_iteration
- Stop when the `x` difference is less than 0.1 (step size) after an iteration of epochs
- Stop when the solution `f(x)` difference is less than 0.1

<hr />

## Conclusion

The two minima found by the algorithm (when the parameters are abjusted) were x = 0 and x = 101.

We can simply do f(0) and f(101) to determine the best.

- f(0) = -1
- f(101) = ~ -1.37

So x = 101 is the best solution out of the minima found from these tests.

The success of this algorithm in terms of success (at reaching a good solution) is quite consistent when the right parameters are chosen, however as what these are change depending upon the problem function, the accuracy of the method is not constant. I'd say the efficiency of this algorithm can be quite efficient again when favourable parameters are chosen, but it can take a large amount of iterations and epochs to get to a good solution (or it might not get to a good solution in time) when bad parameters are chosen.

<hr />

## References

(Henderson. D, et al, 2003) - https://pdfs.semanticscholar.org/2726/93df38b60670a8ea788122a7de353a9a7ff0.pdf (Accessed 30/10/2018)
