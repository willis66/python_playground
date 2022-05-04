
#copied from p6_2 then edited
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

class Loss():
    def calculate(self, output, y): #y is correct vals # output is output from model
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses)
        return data_loss

class Loss_CategoricalCrossentropy(Loss):
    def forward(self, outp, real_val):
        samples = len(outp)
        output_clipped = np.clip(outp, 1e-8, 1-1e-8)

        if len(real_val.shape) == 1:
            correct_confidences = output_clipped[range(samples), real_val]
        elif len(real_val.shape) == 2:
            correct_confidences = np.sum(output_clipped*real_val, axis=1) #the clipped array times an array of 0's and 1's that perfects matches with clipped array.. then sum all together as anything * 0 = 0

        negative_log_likelyhoods = -np.log(correct_confidences)
        return negative_log_likelyhoods

loss_function = Loss_CategoricalCrossentropy()
dense1 = Layer_Dense(2, 3)
activation1 = Activation_ReLU()
dense2 = Layer_Dense(3, 3) #three classes defined in creation of data
activation2 = Activation_Softmax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

print(activation2.output)
loss = loss_function.calculate(activation2.output, y)
print()
print(loss)