
#copied from p5 then edited
import numpy as np

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

class Layer_Dense():
    def __init__(self, n_inputs, n_neurons): #n_neurons is the output
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons) #creates a random array with n_inputs rowns and n_neurons columns # 0.1 so everything is <|1| #allows skip of transposition
        self.biases = np.zeros((1, n_neurons)) #first param is tuple of shape

    def forward(self, inputs): #inputs can be first training layer or output of prev. layer
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU():
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

class Activation_Softmax():
    def forward(self, inputs):
        exp_values = (np.exp(inputs) - np.max(inputs, axis=1, keepdims=True)) #the highest value per batch is 1
        norm_values = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = norm_values


        
dense1 = Layer_Dense(2, 3)
activation1 = Activation_ReLU()
dense2 = Layer_Dense(3, 3) #three classes defined in creation of data
activation2 = Activation_Softmax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

print(activation2.output)