'''
# a log in programming is BASE e
import math

softmax_output_example = [0.7, 0.1, 0.2]
#target_class = 0
target_output = [1, 0, 0]

loss = -(math.log(softmax_output_example[0])*target_output[0] + math.log(softmax_output_example[1])*target_output[1] + math.log(softmax_output_example[2])*target_output[2])
# loss is the same as:
loss2 = -math.log(softmax_output_example[0])
print(loss)
print(loss2)

#again have to do it for batches

'''

import numpy as np

class_targets = [0, 1, 1]

softmax_outputs_example = np.array([[0.7, 0.1, 0.2],
                                    [0.2, 0.5, 0.4],
                                    [0.02, 0.9, 0.08]])

#print(softmax_outputs_example[[0, 1, 2], class_targets]) #getting 0th row, and 0th val cause its target, then 1st row and 1st val since its target, then 2nd row and 1st val since its target
# prints: [0.7 0.5 0.9]
vals = softmax_outputs_example[range(len(softmax_outputs_example)), class_targets]
print(vals)
#then to get losses just get the negative log (base e)
batch_loss = -np.log(vals)
print(batch_loss)
#avg loss
batch_avg_loss = np.mean(batch_loss)
print(batch_avg_loss)
#-np.log(0) would be infinite, which would obv wouldn't work
