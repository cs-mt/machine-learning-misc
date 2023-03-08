import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf

# Inputs and outputs of the XOR function.
X_train = [[0,0], [0,1], [1,0], [1,1]]
y_train = [0,1,1,0]

# Inputs and outputs of the OR function
"""
X_train = [[0,0], [0,1], [1,0], [1,1]]
y_train = [0,1,1,1]
"""

model = tf.keras.Sequential()

# Single layer perceptron (input -> output) cannot learn the XOR function due to XOR outputs not being linearly separable.
# On the contrary multi layer perceptron (input -> hidden layer -> output) can easily learn it.
# https://en.wikipedia.org/wiki/Perceptron

# This creates an input layer with 2 neurons, and a hidden layer with 4 neurons. (Multi layer perceptron)
# The hidden layer requires at least 4 neurons for the model to accurately predict all 4 of the outputs of the XOR function according to my observations.

model.add(tf.keras.layers.Dense(4, input_dim=2, activation="relu"))

# This creates an output layer with 1 neuron.
model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

#tf.keras.utils.plot_model(model, to_file='multi-layer.png', show_shapes=True, show_layer_names=True)


# This creates an input layer with 2 neurons, and a single output neuron. (Single layer perceptron)
# XOR is impossible with this model, but OR can easily be predicted.
"""
model.add(tf.keras.layers.Dense(1, input_dim=2, activation="sigmoid"))
"""

#tf.keras.utils.plot_model(model, to_file='single-layer.png', show_shapes=True, show_layer_names=True)

opt = tf.keras.optimizers.Adam(learning_rate=0.002)
model.compile(loss="binary_crossentropy", optimizer=opt, metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=1000, batch_size=1)

print(model.predict(X_train))

