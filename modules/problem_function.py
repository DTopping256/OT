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
