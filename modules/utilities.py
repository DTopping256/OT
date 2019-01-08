#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# An n dimentional spiral from a start point of cx of n dimensions
def n_dim_spiral(cx, max_i, step_size):
    i = 0
    # Amount of times the algorithm has reached either an all positive or an all negative areas of n dimentional space.
    turns = 0
    start_points = [{k: v for k, v in cx.items()}]
    while True:
        for k in cx.keys():
            for step in range(turns+1):
                step = step_size
                if (turns % 2 == 1):
                    step = -step
                cx[k] += step
                i += 1
                # Remove pointers to previous answer from start_points array.
                outputDict = {k: v for k, v in cx.items()}
                start_points.append(outputDict)
                if (max_i == i):
                    break
            if (max_i  == i):
                break
        if (max_i == i):
            break
        turns += 1
    return start_points

