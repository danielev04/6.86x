import numpy as np

def neural_network(inputs, weights):
    """
     Takes an input vector and runs it through a 1-layer neural network
     with a given weight matrix and returns the output.

     Arg:
       inputs - 2 x 1 NumPy array
       weights - 2 x 1 NumPy array
     Returns (in this order):
       out - a 1 x 1 NumPy array, representing the output of the neural network
    """
    #Your code here
    prod = inputs * weights
    out = np.array([[np.tanh(prod.sum())]])
    return out

inp = np.array([1,3]) 
wei = np.array([6,7])
result = neural_network(inp,wei)
print(result)

