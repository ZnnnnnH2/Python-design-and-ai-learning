from copy import deepcopy,copy

a = [1,2]
b = [a,30]
a.append(b) # a = [1, 2, [[...], 30]]
c = deepcopy(a) # c = [1, 2, [[...], 30]]
e = a.copy() # e = [1, 2, [[1, 2, [...]], 30]]
print(a)
print(c)
print(e)