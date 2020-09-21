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

def vector_function(x, y):
    """
    Make sure vector_function can deal with vector input x,y 
    """
    g = np.vectorize(scalar_function)
    vf = g(x,y)
    return vf

breakpoint()

x = np.array([2,3,4])
y = np.array([6,7,8])

result = vector_function(x,y)
print(result)

