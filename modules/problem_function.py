import math
e = math.e

# The python definitions of f(x) & f'(x) for problem 1.

def f(x):
    if (x <= 100):
        return float(-e**(-(x/100)**2))
    else:
        return float(-e**(-1) + (x - 100)*(x - 102))
    
def diff_f(x):
    if (x <= 100):
        return float(e**(-(x/100)**2)/5000)
    else:
        return float(2*(x - 101))
    
# Data wrapper for a problem.
'''
    f: the problem function, should return a float.
    dfs: an array of partial derivative functions of f, each of which should return a float. 
    maximisation: True or False, if false is a minimisation problem.
'''
class problem:
    def __init__(self, f, dfs, maximisation = False):
        self.maximisation = maximisation
        self.f = f
        self.dfs = dfs