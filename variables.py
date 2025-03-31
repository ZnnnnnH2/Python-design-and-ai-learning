from copy import copy, deepcopy

a = [10, 20]
b = [a, 30]
a.append(b)
print(a)
print(b)
print(id(a))
print(id(b[0]))
print(a[2][0][2][0][2][0][2][0][2])
print(a[2][0][2][0][2][0][2][0][2] is b)

c = deepcopy(a)
d = a.copy()
print(c)
print(id(c))
print(id(c[2][0]))
print(id(c[2][0][2][0]))
print(d)