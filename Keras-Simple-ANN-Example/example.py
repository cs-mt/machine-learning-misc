import os 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from keras.utils import to_categorical
import tensorflow as tf
import numpy as np


X_train = []
y_train = []

f = open("train.txt")

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
one_hot = to_categorical(digits)

for line in f:
    data = line.strip().split(",")
    x1_encoded = one_hot[int(data[0])]
    x2_encoded = one_hot[int(data[1])]
    X_train.append(np.concatenate((x1_encoded, x2_encoded)))
    if(len(data[2]) == 1):
        y_train.append(np.concatenate((one_hot[0], one_hot[int(data[2])])))
    elif(len(data[2]) == 2):
        y_train.append(np.concatenate((one_hot[int(data[2][0])], one_hot[int(data[2][1])])))

X_train = np.array(X_train)
y_train = np.array(y_train)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(20, input_dim=20, activation="relu"))
model.add(tf.keras.layers.Dense(20, activation="relu"))
model.add(tf.keras.layers.Dense(20, activation="sigmoid"))

opt = tf.keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss="binary_crossentropy", optimizer=opt, metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=3, batch_size=1)

outputs = model.predict(X_train[-50:])
inputs = X_train[-50:]

accurate = 0

for x in range(len(inputs)):
    a = np.argmax(inputs[x][:-10])
    b = np.argmax(inputs[x][-10:])
    sum = str(np.argmax([outputs[x][:-10]])) + str(np.argmax([outputs[x][-10:]]))
    if int(a) + int(b) == int(sum):
        accurate+=1
    print("{} + {} = {}".format(a,b,sum))

print("Accuracy: {}/{}".format(accurate, len(outputs)))
