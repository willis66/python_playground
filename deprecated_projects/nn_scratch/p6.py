
import numpy as np
#import math 

temp_layer_outputs = [
    [4.8, 1.21, 2.385],
    [8.9, -1.81, 0.2],
    [1.41, 1.051, 0.026]]

#E = math.e

#print(np.sum(temp_layer_outputs, axis=1, keepdims=True)) #asix None default (1 scalar val), axis 0 is sum of columns, axis 1 sum of rows # keepdims keeps it as a matrix of the same dimension

#exp_values = []
exp_values = np.exp(temp_layer_outputs)
#print(exp_values
norm_values = exp_values / np.sum(exp_values, axis=1, keepdims=True)
print(norm_values)

'''
for output in temp_layer_outputs:
    exp_values.append(E**output) #get rid of negatives while not getting rid of actual values
'''
'''
#normalizing
norm_base = sum(exp_values)
norm_values = []

for val in exp_values:
    norm_values.append(val / norm_base)
'''
#print(norm_values)
#print(sum(norm_values))
