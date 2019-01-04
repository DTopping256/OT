# Taboo Search

_Source code: [notebook](./tabooSearch.ipynb) or [python script](./tabooSearch.py)_

Taboo search is deterministic so doesn't need to be run more than once for the same parameters, because its going to yield the same results.

## Abstract

I have made a generalised `taboo_search` function in the [metaheuristics module](../../modules/metaheuristics.py#L101) which can take in many parameters.

Throughout testing I found that the 2 minima picked up by simulated annealing are 0 and 101, and I have shown that 101 is the best solution out of the two; so for the rest of this I will refer to 101 as the global minimum and 0 as the local minimum.

## Default taboo search

With the [default](./tabooSearch.py#L81) starting parameters, you get this:

![Taboo search (against line)](./taboo_search_on_f_wth_start_vars.png?raw=true "Taboo search")

When the algorithm starts it finds the neighbours of the start position and selects the better neighbour using `f`. It carries on like this until reaching a minimum where it can't find a better neighbour and fills its taboo list with the neighbourhood before stopping, since there are no other viable neighbours.

<div class="page"/>

## Algorithm by hand (first few iterations)

**With these starting parameters**

- s0 = 120
- taboo_memory = 5
- max_i = 300
- step_size = 0.1
- neighbourhood: s ± step_size (2 neighbours)
- stop_function: if max iterations is reached or there aren't any viable neighbours.

**Algorithm:**

- Set taboo list to just s0 (`taboo_list = [120]`)
- Repeat (until stop condition is satisfied):
  - Calculate the neighbourhood (`[s - step_size, s + step_size] = [119.9, 120.1]`)
  - Filter (remove) the neighbours which appear in the taboo list (none)
  - Sort the neighbourhood by the problem function. (`[119.9, 120.1]`)
  - If the best neighbour is better than the current `s` replace `s` with it. (`s = 119.9`)
  - Add best neighbour to taboo list, removing oldest if no memory left (`taboo_list = [120, 119.9]`)

## Starting point (s0)

Since this algorithm taboo's the current solution, there is no change of direction and the minimum that it finds will be the first one in that direction.

I tested starting positions from 80 - 120 in increments of 1.

![results_against_s0](./results_wth_starting_point.png?raw=true "Results against start point")

With a starting position of 80 - 100, the algorithm heads towards the local minimum at x = 0 (but reaches the max iterations before it can).

Otherwise, with a starting position of between 101 - 120 the search finds the global minimum at x = 101.

<div class="page"/>

## Max iterations

I tested 40 amounts of iterations from 5 to 200.

### s0 = 80

![results_against_max_i_at_s0_80](./results_wth_max_i_at_s0_80.png?raw=true "Results against max iterations (s0 = 80)")

Increasing the max iterations gets the final solution closer to `x = 0` (local min).

### s0 = 101

![results_against_max_i_at_s0_101](./results_wth_max_i_at_s0_101.png?raw=true "Results against max iterations (s0 = 101)")

Here there is no affect as the stop condition is acheived every time, because the start is in a minimum.

<div class="page"/>

### s0 = 120

![results_against_max_i_at_s0_120](./results_wth_max_i_at_s0_120.png?raw=true "Results against max iterations (s0 = 120)")

Here 192 iterations are necessary for the stop condition to be met from a start at 120.

## Step size

I tested 40 step sizes from 0.05 to 2.

### s0 = 80

![results_against_step_at_s0_80](./results_wth_step_at_s0_80.png?raw=true "Results against step size (s0 = 80)")

The local minimum was reached when the step size got to 0.4 or greater (with a max_i of 200); but since the step size is not a multiplier but is the actual size of each difference per iteration, step sizes which didn't divide 80 evenly gave inaccurate results around the minimum.

<div class="page"/>

### s0 = 101

![results_against_step_at_s0_101](./results_wth_step_at_s0_101.png?raw=true "Results against step size (s0 = 101)")

Here there is no affect as the algorithm doesn't step away from the minimum.

### s0 = 120

![results_against_step_at_s0_120](./results_wth_step_at_s0_120.png?raw=true "Results against step size (s0 = 120)")

In this case the global minimum isn't far away but since the difference from the start to the minimum is 19, the affects of a step size which doesn't divide perfectly into 19 is clearer about the minimum.

<div class="page"/>

## Taboo memory

In this test I varied the maximum amount of values that could be stored in the taboo list per iteration. I tested between 1 and 4.

### s0 = 80

![results_against_memory_at_s0_80](./results_wth_memory_at_s0_80.png?raw=true "Results against memory size (s0 = 80)")

### s0 = 101

![results_against_memory_at_s0_101](./results_wth_memory_at_s0_101.png?raw=true "Results against memory size (s0 = 101)")

<div class="page"/>

### s0 = 120

![results_against_memory_at_s0_120](./results_wth_memory_at_s0_120.png?raw=true "Results against memory size (s0 = 120)")

As you can see memory in this case doesn't affect the end result since either the stop condition is reached or the maximum iterations are reached and we only need space for 2 values, 1 step away either side of the current position (for a 1 dimentional problem).

## Conclusion

Taboo search is very similar to gradient descent in its simplicity, and its deterministic nature.

Pros:

- It doesn't need a gradient to determine the direction to follow. So can deal with non-continuous functions.
- Not computationally intensive.

Cons:

- Only as accurate as the step size.
- Finds the closest minimum down the slope from where-ever it starts (with enough iterations)
