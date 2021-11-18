
#copied from p4_2 then edited
import numpy as np


'''
X = [ #capital X becuase standard in machine learning that input feature sets are a cap. X
    [1.2, 5.1, 2.1, 3.3],
    [4.3, -6.9, 2.2, -0.1],
    [3.3, -0.1, -1.1, -0.7]] #shape is (3, 4)

#rectified linear function
'''
'''
inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]
output = []

''' '''
for i in inputs:
    if i > 0:
        output.append(i)
    else:
        output.append(0)
''' '''
# OR
for i in inputs:
    output.append(max(0, i))
print(output)
'''

def spiral_data(points, classes):
    X = np.zeros((points*classes, 2))
    y = np.zeros(points*classes, dtype='uint8')
    for class_number in range(classes):
        ix = range(points*class_number, points*(class_number+1))
        r = np.linspace(0.0, 1, points)  # radius
        t = np.linspace(class_number*4, (class_number+1)*4, points) + np.random.randn(points)*0.2
        X[ix] = np.c_[r*np.sin(t*2.5), r*np.cos(t*2.5)]
        y[ix] = class_number
    return X, y

X, y = spiral_data(100, 3)#100 sets of points, each 1 of 3 classes

# weights generally -1 < x < 1
# biases typically start at 0, but a dead network (when all become 0's) one may need a higher bias
class Layer_Dense():
    def __init__(self, n_inputs, n_neurons): #n_neurons is the output
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons) #creates a random array with n_inputs rowns and n_neurons columns # 0.1 so everything is <|1| #allows skip of transposition
        self.biases = np.zeros((1, n_neurons)) #first param is tuple of shape

    def forward(self, inputs): #inputs can be first training layer or output of prev. layer
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU():
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)
        

layer1 = Layer_Dense(2, 5)
activation1 = Activation_ReLU()
layer1.forward(X)
activation1.forward(layer1.output)
print(activation1.output)

#print(layer1.output)
#layer2.forward(layer1.output)
#print(layer2.output)
