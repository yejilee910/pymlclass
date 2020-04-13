import numpy as np
import pandas as pd
a = pd.DataFrame([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(a)

print(a.shape)

# ---------------------
print("-------a--------")
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))
print("------b-------")
b = np.array([6, 7, 8])
print(b)
print(b.shape)
print(b.ndim)
print(b.dtype.name)
print(b.itemsize)
print(b.size)
print(type(b))
