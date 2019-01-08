#!/usr/bin/env python
# coding: utf-8

def f(xs):
    return 3*xs["x1"]+5*xs["x2"]+4*xs["x3"]+xs["x4"]

pds = {"x1": lambda v: 3, "x2": lambda v: 5, "x3": lambda v: 4, "x4": lambda v: 1}

def x1_non_neg_constraint(xs):
    return ("x1 not -ve", 0, xs["x1"])
def x2_non_neg_constraint(xs):
    return ("x2 not -ve", 0, xs["x2"])
def x3_non_neg_constraint(xs):
    return ("x3 not -ve", 0, xs["x3"])
def x4_non_neg_constraint(xs):
    return ("x4 not -ve", 0, xs["x4"])
def green_wool_constraint(xs):
    return ("green", xs["x1"]+2*xs["x2"]+xs["x3"]+xs["x4"], 10)
def red_wool_constraint(xs):
    return ("red", 2*xs["x1"]+xs["x2"]+2*xs["x3"]+xs["x4"], 6)
def blue_wool_constraint(xs):
    return ("blue", 3*xs["x1"]+xs["x2"], 10)
def yellow_wool_constraint(xs):
    return ("yellow", xs["x1"]+4*xs["x2"], 18)
def brown_wool_constraint(xs):
    return ("brown", xs["x3"]+3*xs["x4"], 8)
def purple_wool_constraint(xs):
    return ("purple", 3*xs["x3"]+3*xs["x4"], 12)

constraints = [x1_non_neg_constraint, x2_non_neg_constraint, x3_non_neg_constraint, x4_non_neg_constraint, green_wool_constraint, red_wool_constraint, blue_wool_constraint, yellow_wool_constraint, brown_wool_constraint, purple_wool_constraint]

# If any constraint is False then False, otherwise if every constraint is True then True. 
def check_all_constraints(xs, constraints, print_fail_point=False):
    for constraint in constraints:
        c = constraint(xs)
        if (c[1] > c[2]):
            if (print_fail_point):
                print("({} constraint fails)".format(c[0]))
            return False
    return True

# Prints all constraint progress 
def print_all_constraints(xs, constraints):
    for constraint in constraints:
        c = constraint(xs)
        print("{} constraint: {} <= {}".format(c[0], round(c[1], 3), c[2]))