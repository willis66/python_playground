
#copied from p4 then edited
import numpy as np



X = [ #capital X becuase standard in machine learning that input feature sets are a cap. X
    [1.2, 5.1, 2.1, 3.3],
    [4.3, -6.9, 2.2, -0.1],
    [3.3, -0.1, -1.1, -0.7]] #shape is (3, 4)

# weights generally -1 < x < 1
# biases typically start at 0, but a dead network (when all become 0's) one may need a higher bias
class Layer_Dense():
    def __init__(self, n_inputs, n_neurons): #n_neurons is the output
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons) #creates a random array with n_inputs rowns and n_neurons columns # 0.1 so everything is <|1| #allows skip of transposition
        self.biases = np.zeros((1, n_neurons)) #first param is tuple of shape

    def forward(self, inputs): #inputs can be first training layer or output of prev. layer
        self.output = np.dot(inputs, self.weights) + self.biases
        

layer1 = Layer_Dense(4, 5) #3 samples (rows), 3 outputs with 5 values
layer2 = Layer_Dense(5, 2)

layer1.forward(X)
#print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)
