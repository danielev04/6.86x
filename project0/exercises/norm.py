import numpy as np

def norm(A, B):
    """
    Takes two Numpy column arrays, A and B, and returns the L2 norm of their
    sum.

    Arg:
      A - a Numpy array
      B - a Numpy array
    Returns:
      s - the L2 norm of A+B.
    """
    #Your code here
    s = np.linalg.norm(A+B)
    return s

x = np.array([2,3,4])
y = np.array([6,7,8])
result = norm(x,y)
print(result)

