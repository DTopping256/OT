# Technical report

If this is hard to follow, use the `ReportLinked.pdf` instead; as this seperates each problem and metaheuristic using links.

## Problem 1

### Abstract

<img class="default_img_res" src="./problem1/problemFunction.png?raw=true"/>

I defined this in the [problem_function](./modules/problem_function.py) module which I import in all my metaheuristics code.

It plots this graph:

![f(x)](./problem1/simulatedAnnealing/f.png?raw=true "f(x)")

Where there is a local minimum (a very shallow one on this scale) at `x = 0` and a global minimum at `x = 101`; so the best solution is 101.

I find both of these minima when testing each of the metaheuristics. I have written the code to each metaheuristic and put it into the `metaheuristics` python module.

<hr />

## Solving problem 1 with Gradient Descent

_Source code: [notebook](./problem1/gradientDescent/gradientDescent.ipynb) or [python script](./problem1/gradientDescent/gradientDescent.py)_

Gradient descent is deterministic so doesn't need to be run more than once for the same parameters, because its going to yield the same results.

I have made a generalised `gradient_descent` function in the [metaheuristics module](./modules/metaheuristics.py).

### Default gradient descent

With the [default](./problem1/gradientDescent/gradientDescent.py#L136) starting parameters, you get this:

![GD (against line)](./problem1/gradientDescent/default_gd_against_line.png?raw=true "GD (against line)")

When the algorithm starts it uses the derivative to find the gradient and follows the slope downward, until one of the tolerances (`e_g` gradient or `e_x` difference in x) are satisfied or the maximum iterations is reached.

### Algorithm by hand (first few iterations)

**Starting with these parameters:**

- x0 = 120
- max_i = 100
- step_m = 0.1
- e_g = 0.001
- e_x = 0.001

**Algorithm:**

- Set x = x0 ( = 120)
- Calculate the initial gradient (`g = 2*(120-101) = 38`)
- While either of the tolerances aren't satisfied (`xdiff > e_x || g > e_g`) or the maximum iterations isn't reached (`i < max_i`):
  - Calculate the new x value (`x = x - g*step_m = 120 - 38*0.1 = 116.2`)
  - Find the new gradient (`g = 2*(116.2-101) = 30.4`)

_See the notebook, for output of all of the iterations._

### Starting point (x0)

When testing how the starting point affects the gradient descent on this particular function it becomes apparent that gradent descent only works well from a particular set of start positions.

![results_against_x0](./problem1/gradientDescent/results_against_x0.png?raw=true "Results against start point")

Below the value of the global minima the curve is very flat and has little gradient, so the algorithm has tiny steps and doesn't move very far (from where it starts) in the amount of iterations it has. But between 101 and 120 the algorithm consistently finds the global minimum at 101.

### Step multiplier

This is the proportion of the gradient that is subracted from the current x position.

Again doing 3 tests at x0 = 80, x0 = 101 and x0 = 120; this time I varied the step multiplier value between 1/21 and 20/21 (in increments of 1/21 for 20 times)

#### x0 = 80

![results_against_stepm_x0_80](./problem1/gradientDescent/results_against_stepm_x0_80.png?raw=true "Results against step multiplier (starting at x = 80)")

Here the gradient is so small that the amount taken off of x each step is negligible; so the step multiplier has little effect, and the result is approximately `x0`.

#### x0 = 101

![results_against_stepm_x0_101](./problem1/gradientDescent/results_against_stepm_x0_101.png?raw=true "Results against step multiplier (starting at x = 101)")

Here it seems that the stopcondition gets triggered immediently so the step multiplier doesn't have any effect, and the result is `x0`.

#### x0 = 120

![results_against_stepm_x0_120](./problem1/gradientDescent/results_against_stepm_x0_120.png?raw=true "Results against step multiplier (starting at x = 120)")

Here there is a steep gradient so a smaller step multiplier is preferred over a larger one (`step_m < 0.6`) otherwise gradient descent overshoots the global minimum and carries on towards the local minimum.

### Difference tolerance (e_x)

Doing tests at x0 = 80, x0 = 101 and x0 = 120; the difference tolerance was varied from 0.05 to 1.00 (in 20 increments of 0.05).

#### x0 = 80

![results_against_ex_x0_80](./problem1/gradientDescent/results_against_ex_x0_80.png?raw=true "Results against difference tolerance (starting at x = 80)")

Again, (with the step multiplier only being 0.1) the difference at this shallow gradient was very small so the tolerance between this range was pretty much satisfied straight away.

#### x0 = 101

![results_against_ex_x0_101](./problem1/gradientDescent/results_against_ex_x0_101.png?raw=true "Results against difference tolerance (starting at x = 101)")

Similar to the last one, the difference tolerance was satisfied straight away (because of the small gradient) with the algorithm starting at a minimum.

#### x0 = 120

![results_against_ex_x0_120](./problem1/gradientDescent/results_against_ex_x0_120.png?raw=true "Results against difference tolerance (starting at x = 120)")

Because this part of the curve is much more steep, we actually get some movement from the GD algorithm. The correlation favours smaller values of tolerance for getting closer to the minimum.

### Gradient tolerance (e_g)

Doing tests at x0 = 80, x0 = 101 and x0 = 120; the gradient tolerance was varied from 0.05 to 2.00 (in 40 increments of 0.05).

The results were very similar to difference tolerance, however gradient tolerance values are a lot less sensitive in changing the result than difference tolerance.

#### x0 = 80

![results_against_eg_x0_80](./problem1/gradientDescent/results_against_eg_x0_80.png?raw=true "Results against gradient tolerance (starting at x = 80)")

#### x0 = 101

![results_against_eg_x0_101](./problem1/gradientDescent/results_against_eg_x0_101.png?raw=true "Results against gradient tolerance (starting at x = 101)")

#### x0 = 120

![results_against_eg_x0_120](./problem1/gradientDescent/results_against_eg_x0_120.png?raw=true "Results against gradient tolerance (starting at x = 120)")

### Maximum iterations

The maximum iterations value limits how many times the GD algorithm can run when the tolerance values aren't met.

#### x0 = 80

![results_against_iterations_x0_80](./problem1/gradientDescent/results_against_iterations_x0_80.png?raw=true "Results against max iterations (starting at x = 80)")

As the tolerances are met straight away, iterations doesn't affect the GD at this start point on the curve.

#### x0 = 101

![results_against_iterations_x0_101](./problem1/gradientDescent/results_against_iterations_x0_101.png?raw=true "Results against max iterations (starting at x = 101)")

As the tolerances are met straight away, iterations doesn't affect the GD at this start point on the curve.

#### x0 = 120

![results_against_iterations_x0_120](./problem1/gradientDescent/results_against_iterations_x0_120.png?raw=true "Results against max iterations (starting at x = 120)")

The larger the maximum iterations the closer the result is to finding a satisfying the tolerance stop conditions, and getting a good final result.

### Conclusion

Gradient descent is a very simple deterministic algorithm which just follows a gradient down to a minimum.

Pros:

- Its not very computationally intensive and relatively fast, compared to other metaheuristics.
- Accurate when given the right parameters

Cons:

- Can't be used on functions which aren't continuous since it needs the derivative to find the gradient.
- Bad on curves with long shallow gradients, an requires really small or no tolerances and high numbers of iterations to get close to a minima.
- Will find the minima down the gradient to wherever is starts, which isn't neccesarily the global minimum.
