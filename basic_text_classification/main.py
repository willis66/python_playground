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

for text_batch, label_batch in raw_train_ds.take(1):
    for i in range(3):
        print("Review:", text_batch.numpy()[i])
        print("Label:", label_batch.numpy()[i])

print("Label 0 corresponds to", raw_train_ds.class_names[0])
print("Label 1 corresponds to", raw_train_ds.class_names[1])

sequence_length = 300
max_features = 10000

vectorize_layer = tf.keras.layers.TextVectorization(
    standardize=custom_standardization,
    max_tokens=max_features,
    output_mode="int",
    output_sequence_length=sequence_length,
)

train_text = raw_train_ds.map(lambda x, y: x)
vectorize_layer.adapt(train_text)

text_batch, label_batch = next(iter(raw_train_ds))
review1, label1 = text_batch[0], label_batch[0]
print("Review: {}".format(review1))
print("Label: {}".format(raw_train_ds.class_names[label1]))
print("Vectorized: {}".format(vectorize_text(review1, label1)))

print("1287 --> {}".format(vectorize_layer.get_vocabulary()[1287]))
print("313 --> {}".format(vectorize_layer.get_vocabulary()[313]))
print("Vocabulary size: {}".format(len(vectorize_layer.get_vocabulary())))

train_ds = raw_train_ds.map(vectorize_text)
val_ds = raw_val_ds.map(vectorize_text)
test_ds = raw_test_ds.map(vectorize_text)

AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.cache().prefetch(buffer_size=AUTOTUNE)
