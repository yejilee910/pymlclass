import numpy as np
from keras.utils import np_utils
print("#np_utils.to_categorical()")
# converting to floats
X_train = X_train / 225.0
X_test = X_test / 225.0

# reshaping before entering CNN
# one-hot encoding is used for the output
# we use channel-last odering (keras default)
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
Y_train = np.utilis.to_categoricall(Y_train, TOTAL_CLASS)
Y_test = np.utilis.to_categorical(Y_test, TOTAL_CLASS)

print('#n == DB SHAPING INFO ==')
print("X train shape:", X_train.shape)
print("Y train shape:", Y_train.shape)
print("X test shape:", X_test.shape)
print("Y test shape:", Y_test.shape)
