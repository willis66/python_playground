import sys

print("System version:", sys.version)
import tensorflow as tf

import tensorflow_hub as hub
import tensorflow_datasets as tfds

print("Tensorflow version: ", tf.__version__)
print("Tensorflow eager mode: ", tf.executing_eagerly())
print("Tensorflow Hub version: ", hub.__version__)
print(
    "GPU is", "available" if tf.config.list_physical_devices("GPU") else "NOT AVAILABLE"
)

train_ds, val_ds, test_ds = tfds.load(
    name="imdb_reviews",
    split=("train[:60%]", "train[60%:]", "test"),
    as_supervised=True,
)

train_examples_batch, train_labels_batch = next(iter(train_ds.batch(10)))
print(train_examples_batch)
print(train_labels_batch)

embedding = "https://tfhub.dev/google/nnlm-en-dim128-with-normalization/2"
hub_layer = hub.KerasLayer(embedding, input_shape=[], dtype=tf.string, trainable=True)
example_hub_layer = hub_layer(train_examples_batch[:3])
print(example_hub_layer)

model = tf.keras.Sequential()
model.add(hub_layer)
model.add(tf.keras.layers.Dense(16, activation="relu"))
model.add(tf.keras.layers.Dense(1))

print(model.summary())
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
    metrics=["accuracy"],
)

