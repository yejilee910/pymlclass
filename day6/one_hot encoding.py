print("#np_utils.to_categorical()")
from keras.utils import np_utils
import numpy as np
encodingbitsize = 3
my_array = [0, 2, 1, 2, 0]
print("my_array = [0, 2, 1, 2, 0]")
#one-hot encoding
one_hot = np_utils.to_categorical(my_array, encodingbitsize)
print("to_categorical(my_array,3)")
print(one_hot)