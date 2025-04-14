import numpy as np

array = np.zeros((4,4),dtype=int)
array[0,1] = 1
array[1,2] = 1
array[2,3] = 1
array[1,3] = 1

print(array)
array2 = np.matmul(array, array)
print(array2)
array3 = np.matmul(array, array2)
print(array3)
array4 = np.matmul(array, array3)
print(array4)
array5 = array4+array3+array2+array
print(array5)

print(type(array.data))