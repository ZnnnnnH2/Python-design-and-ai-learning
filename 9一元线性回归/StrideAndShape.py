import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(x.shape)
print(x.strides)

y = x[:, 1:]
print(y.shape)
print(y.strides)

z = x[:, ::2]
print(z.shape)
print(z.strides)
