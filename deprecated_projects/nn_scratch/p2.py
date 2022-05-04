
#copied from p1 then edited

inputs = [1.2, 5.1, 2.1, 3.3] #input from 3 (imaginary) neurons in the previous layer #this is the imaginary (neuron) circle's value 
weights1 = [2.3, 2.4, 5.6, 1.0] #3 inputs is 3 weights #this is the imaginary (weight) string's value
weights2 = [0.5, -0.4, 0.3, -1.0]
weights3 = [1.3, -1.4, -0.6, 1.2]
bias1 = 3 # each neuron has a unique bias
bias2 = 2
bias3 = 5.6

output = [
    inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1,
    inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] + bias2,
    inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + bias3] #output of fake nn

print(output)
