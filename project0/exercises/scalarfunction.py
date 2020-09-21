import numpy as np

def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    #Your code here
    if x <= y:
      f = x * y
    else:
      f = x/y
    return f

result = scalar_function(3,2)
print(result)

