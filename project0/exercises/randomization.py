import numpy as np

def randomization(n):
    """
    Arg:
      n - an integer
    Returns:
      A - a randomly-generated nx1 Numpy array.
    """
    #Your code here

    A = np.random.random([n,1])
    return A


result = randomization(2)
print(result)

