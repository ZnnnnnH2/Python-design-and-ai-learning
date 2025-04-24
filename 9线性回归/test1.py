import numpy as np

x = np.array([[1, 2], [3, 4]])

t = range(0,2)

y = x[t,t]
z = x.flatten()

print(z)