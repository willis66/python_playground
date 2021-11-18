
inputs = [1.2, 5.1, 2.1] #input from 3 (imaginary) neurons in the previous layer
weights = [2.3, 2.4, 5.6] #3 inputs is 3 weights
bias = 3 # each neuron has a unique bias

output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias #output of fake nn
print(output)
