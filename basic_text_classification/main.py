import sys

print(sys.version)

import matplotlib.pyplot as plt
import os
import re
import shutil
import string

import tensorflow as tf

""" from tensorflow.keras import layers
from tensorflow.keras import losses """

print("Tensorflow version: {}".format(tf.__version__))

url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"

""" dataset = tf.keras.utils.get_file(
    "aclImdb_v1", url, untar=True, cache_dir=".", cache_subdir=""
) """

dataset = "./aclImdb"
print(type(dataset))
dataset_dir = os.path.join(os.path.dirname(dataset), "aclImdb")

print(os.listdir(dataset_dir))

train_dir = os.path.join(dataset_dir, "train")
print(os.listdir(train_dir))

sample_file = os.path.join(train_dir, "pos/1181_9.txt")
with open(sample_file) as f:
    print(f.read())


try:
    remove_dir = os.path.join(train_dir, "unsup")
    shutil.rmtree(remove_dir)
    print("File removed.")
except FileNotFoundError:
    print("File no longer exists.")

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

# Load the dataset

for text_batch, label_batch in raw_train_ds.take(1):
    for i in range(3):
        print("Review:", text_batch.numpy()[i])
        print("Label:", label_batch.numpy()[i])

print("Label 0 corresponds to", raw_train_ds.class_names[0])
print("Label 1 corresponds to", raw_train_ds.class_names[1])

