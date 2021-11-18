
#copied from p2 then edited
import numpy as np

inputs = [1.2, 5.1, 2.1, 3.3] #input from 3 (imaginary) neurons in the previous layer #this is the imaginary (neuron) circle's value 
#3 inputs is 3 weights #this is the imaginary (weight) string's value

weights_old = [2.3, 2.4, 5.6, 1.0]
bias_old = 2

output_old = np.dot(inputs, weights_old) + bias_old #multiplies inputs[0]*weights_old[0] + inputs[1]*weights_old[1] + ... + inputs[n]*weights_old[n] and then add the bias at the end of the line #both are vectors (1d arrays) so order does not matter
print(output_old)


weights = [
    [2.3, 2.4, 5.6, 1.0],
    [0.5, -0.4, 0.3, -1.0],
    [1.3, -1.4, -0.6, 1.2]]

# each neuron has a unique bias

biases = [3, 2, 5.6]

output = np.dot(weights, inputs) + biases #matrix (2d array) (weights) is going to iterate through and multiply by the vector of inputs # same as np.dot(weights[0], inputs), ... , np.dot(weights[n], inputs) (returns a vector) + biases = finalval
print(output)


