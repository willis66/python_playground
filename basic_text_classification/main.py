import sys

print(sys.version)

import matplotlib.pyplot as plt
import os
import re
import shutil
import string

import tensorflow as tf

print("Tensorflow version: {}".format(tf.__version__))

# Using regex (or at least Tensorflow's implementation of it) to prase the strings and remove break statements, punctuation, and convert all to lowercase
def custom_standardization(in_data):
    lowercase = tf.strings.lower(in_data)
    stripped_html = tf.strings.regex_replace(lowercase, "<br />", " ")
    return tf.strings.regex_replace(
        stripped_html, "[%s]" % re.escape(string.punctuation), ""
    )


# This uses Tensorflow's functions of the TextVectorization layer
def vectorize_text(text, label):
    text = tf.expand_dims(text, -1)
    return vectorize_layer(text), label


# Grabbing the dataset using a function of Tensorflow's
url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
dataset = tf.keras.utils.get_file(
    "aclImdb_v1", url, untar=True, cache_dir=".", cache_subdir=""
)

# Now that the dataset's been downloaded, using OS based function to navigate to its location
dataset = "./aclImdb"
print(type(dataset))

dataset_dir = os.path.join(os.path.dirname(dataset), "aclImdb")
train_dir = os.path.join(dataset_dir, "train")

# Checking out the contents of a sample file
sample_file = os.path.join(train_dir, "pos/1181_9.txt")
with open(sample_file) as f:
    print(f.read())

# Removing this directory because Tensorflow's text_dataset_from_directory fuction is based on the directories
try:
    remove_dir = os.path.join(train_dir, "unsup")
    shutil.rmtree(remove_dir)
    print("File removed.")
except FileNotFoundError:
    print("File no longer exists.")

# Set here because they're used for each dataset
batch_size = 32
seed = 42

# Using Tensorflow's function to grab a dataset from each directory. Training dataset split into training and validation
raw_train_ds = tf.keras.utils.text_dataset_from_directory(
    "aclImdb/train",
    batch_size=batch_size,
    validation_split=0.2,
    subset="training",
    seed=seed,
)

raw_val_ds = tf.keras.utils.text_dataset_from_directory(
    "aclImdb/train",
    batch_size=batch_size,
    validation_split=0.2,
    subset="validation",
    seed=seed,
)

raw_test_ds = tf.keras.utils.text_dataset_from_directory(
    "aclImdb/test", batch_size=batch_size
)

# Grabbing the first batch, and printing the first three reviews and labels.
for text_batch, label_batch in raw_train_ds.take(1):
    for i in range(3):
        print("Review:", text_batch.numpy()[i])
        print("Label:", label_batch.numpy()[i])

# Printing out label correspondance. From the names of the directory
print("Label 0 corresponds to", raw_train_ds.class_names[0])
print("Label 1 corresponds to", raw_train_ds.class_names[1])

# Variables used in vectorization
sequence_length = 300
max_features = 10000

# Creating one of Tensorflow's TextVectorization layers to vectorize our reviews
vectorize_layer = tf.keras.layers.TextVectorization(
    standardize=custom_standardization,
    max_tokens=max_features,
    output_mode="int",
    output_sequence_length=sequence_length,
)

# Passing through the anonymous lambda funcion, that will take x and y as inputs then return x. Kinds similar to an arrow function in JS
train_text = raw_train_ds.map(lambda x, y: x)

# After setting everything up we call Tensorflow's map function which converts strings to integers
vectorize_layer.adapt(train_text)

# Printing out a batch from the dataset. 32 reviews and labels.
text_batch, label_batch = next(iter(raw_train_ds))
review1, label1 = text_batch[0], label_batch[0]
print("Review: {}".format(review1))
print("Label: {}".format(raw_train_ds.class_names[label1]))
print("Vectorized: {}".format(vectorize_text(review1, label1)))

# Each string/word has been vectorized to an integer, so we're seeing what string corresponds to the integer 1287...
print("1287 --> {}".format(vectorize_layer.get_vocabulary()[1287]))
print("313 --> {}".format(vectorize_layer.get_vocabulary()[313]))
print("Vocabulary size: {}".format(len(vectorize_layer.get_vocabulary())))

# Mapping this vectorized text into our dataset
train_ds = raw_train_ds.map(vectorize_text)
val_ds = raw_val_ds.map(vectorize_text)
test_ds = raw_test_ds.map(vectorize_text)

# Optimizing the eventual traning so that the dataset isn't a bottleneck
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.cache().prefetch(buffer_size=AUTOTUNE)

# Setting up the model
embedding_dim = 16
model = tf.keras.Sequential(
    [
        # This layer takes the integer-encoded reviews and looks up an embedding vector for each word-index. These vectors are learned as the model trains.
        tf.keras.layers.Embedding(max_features + 1, embedding_dim),
        tf.keras.layers.Dropout(0.2),
        # This layer returns a fixed-length output vector for each example by averaging over the sequence dimension. This allows the model to handle input of variable length, in the simplest way possible.
        tf.keras.layers.GlobalAveragePooling1D(),
        tf.keras.layers.Dropout(0.2),
        # Last layer densely connected to a singular output node
        tf.keras.layers.Dense(1),
    ]
)
print(model.summary())

# Setting optimizer and loss functions
model.compile(
    loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
    optimizer="adam",
    metrics=tf.metrics.BinaryAccuracy(threshold=0.0),
)

# model.fit returns a history object that contains a dictionary with everything that happened during training.
epochs = 10
history = model.fit(train_ds, validation_data=val_ds, epochs=epochs)

# Again just getting loss and accuracy
loss, accuracy = model.evaluate(test_ds)
print("Loss: {}".format(loss))
print("Accuracy: {}".format(accuracy))

# Accessing the history dict from the model.fit function
history_dict = history.history
print(history_dict.keys())

# Grabbing the information from the dictionary
acc = history_dict["binary_accuracy"]
val_acc = history_dict["val_binary_accuracy"]
loss = history_dict["loss"]
val_loss = history_dict["val_loss"]

# Changing epoch to a range so that it can be plotted
print(epochs)
epochs = range(1, len(acc) + 1)
print(epochs)

# Plotting the training and validation losses
plt.plot(epochs, loss, "bo", label="Training Loss")
plt.plot(epochs, val_loss, "b", label="Validation Loss")
plt.title("Training and Validation Losses")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()

# Graphing the training and validation accuracy. The validation accuracy can be seen plateauing much sooner than the training accuracy which is an example of overfitting
plt.plot(epochs, acc, "bo", label="Training Accuracy")
plt.plot(epochs, val_acc, "b", label="Validation Accuracy")
plt.title("Training and Validation Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend(loc="lower right")
plt.show()

