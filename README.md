# OT
## OT assignment repo

This repo contains a Jupyter notebook binder which can be imported into Jupyter notebook, as well as executable python scripts which contain graphs which may take a while to load; in which case I have included saved stills of the 3d graphs which take longer to create.

## Problem 1

I defined this in the function: [problem_function](https://github.com/DTopping256/OT/blob/1d24894d233bdabf625ba0f21abf1dd429dead32/simulatedAnnealing/simulatedAnnealing.py#L15)

It plots this graph:

![f(x)](./simulatedAnnealing/f.png?raw=true "f(x)")

Where there is a local minimum (a very shallow one on this scale) at -1 and a global minimum at 101.

### Simulated Annealing

I have made a generalised simulated annealing function which I have plugged in many combinations of parameters.

You can run the python script or import the ipynb into jupyter notebook to get fresh graphs, SA being stochastic will create different graphs each time but they will be very similar with the current settings.

With the [default](https://github.com/DTopping256/OT/blob/1d24894d233bdabf625ba0f21abf1dd429dead32/simulatedAnnealing/simulatedAnnealing.py#L142) starting parameters, you get something like this:

![SA](./simulatedAnnealing/simulated_annealing_on_f_with_start_vars_wide.png?raw=true "SA (wide)")

![SA](./simulatedAnnealing/simulated_annealing_on_f_with_start_vars_close.png?raw=true "SA (close)")

You can see that the simulated annealing can and does often start to overshoot but with the right parameters it finds the global minimum. However, this isn't the case for a lot of combinations of parameters as we will see. 

#### Changing the starting point (s_0)
For this independant variable I tested a range of starting points from -5 to 120.

![SA](./simulatedAnnealing/variable_starting_point_scatter.png?raw=true "result scatter")

![SA](./simulatedAnnealing/variable_starting_point_scatter_sds.png?raw=true "standard deviation scatter")

Values of 90 < x < 200 are a good start point for the model (with these other starting settings); however with a starting point of x < 90 the model does tend to fall towards the local minimum at x = -1.

#### Adjusting temperature variables (t_0 & the cooling function)









