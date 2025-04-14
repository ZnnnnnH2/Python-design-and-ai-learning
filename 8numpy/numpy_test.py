import numpy as np

array = np.arange(12)
print(id(array))
print(array)

array1 = array.reshape(3,4)
array1[0, 0] = 100
print(array1)

array = array.reshape(3, 4)
print(id(array))
print(array)

array = array.flatten()
print(id(array))
print(array)

array.resize((3, 100))
print(id(array)) #not change 
print(array)