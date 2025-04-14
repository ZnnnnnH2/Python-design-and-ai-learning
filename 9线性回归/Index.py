import numpy as np

x = np.random.permutation(10)
x.resize((2, 5))
print(x)

y = x[x>5]
print(y)