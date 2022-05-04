
#copied from p3 then edited
import numpy as np

inputs = [ #input from 3 (imaginary) neurons in the previous layer #this is the imaginary (neuron) circle's value #features from a single sample
    [1.2, 5.1, 2.1, 3.3],
    [4.3, -6.9, 2.2, -0.1],
    [3.3, -0.1, -1.1, -0.7]]
#32-64 batch size. giving 32-64 data points at once instead of 1 (this is a batch size of 4)
#3 inputs is 3 weights #this is the imaginary (weight) string's value

weights_old = [2.3, 2.4, 5.6, 1.0]
bias_old = 2

output_old = np.dot(inputs, weights_old) + bias_old #multiplies inputs[0]*weights_old[0] + inputs[1]*weights_old[1] + ... + inputs[n]*weights_old[n] and then add the bias at the end of the line #both are vectors (1d arrays) so order does not matter
# print(output_old)


weights = [
    [2.3, 2.4, 5.6, 1.0],
    [0.5, -0.4, 0.3, -1.0],
    [1.3, -1.4, -0.6, 1.2]]
weights2 = [
    [-2.6, -0.4, 0.6],
    [7.5, 8.4, 9.3],
    [-1.7, 1.4, 8.6]]

# each neuron has a unique bias

biases = [3, 2, 5.6]
biases2 = [4, 7, -5.4]

# pre-transpose shape of inputs is (3, 4) and shape of weights is (3, 4)
# post-transpose shape of inputs is (3, 4) but share of weights is (4, 3) (as columns and rows were switched) so (shape of inputs [1]) = (shape of weights [0])
# (np_array).T transposes #transpose swaps rows and columns
# multiply row of inputs by column of weights
layer1_output = np.dot(inputs, np.array(weights).T) + biases #matrix (2d array) (weights) is going to iterate through and multiply by the vector of inputs # same as np.dot(weights[0], inputs), ... , np.dot(weights[n], inputs) (returns a vector) + biases = finalval
# outputs a 3x3 matix, and the biases are added for each row (biases are 3x1)

layer2_output = np.dot(layer1_output, np.array(weights2).T) + biases2

print(layer2_output)

