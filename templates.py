import tensorflow as tf

def classifier_small(in_shape, out_shape):
    return tf.keras.models.Sequential([
        tf.keras.layers.Input(in_shape),
        tf.keras.layers.Dense(10, activation="leaky_relu"),
        tf.keras.layers.Dense(out_shape, activation="sigmoid")
    ])

def classifier_large(in_shape, out_shape):
    return tf.keras.models.Sequential([
        tf.keras.layers.Input(in_shape),
        tf.keras.layers.Dense(64, activation="leaky_relu"),
        tf.keras.layers.Dense(32, activation="leaky_relu"),
        tf.keras.layers.Dense(32, activation="leaky_relu"),
        tf.keras.layers.Dense(out_shape, activation="sigmoid")
    ])