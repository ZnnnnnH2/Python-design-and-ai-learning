import math
import random

N = 1000000


def get_pi_1(n):
	pi = 0
	for i in range(0, n):
		pi += (-1) ** i / (2 * i + 1)
	return pi * 4


def get_pi_2(n):
	inside = 0
	for _ in range(0, n):
		x = random.uniform(-1, 1)
		y = random.uniform(-1, 1)
		if in_c(x, y):
			inside += 1
	return inside / n * 4


def in_c(x, y):
	return x ** 2 + y ** 2 <= 1


lbnc = get_pi_1(N)
mtkl = get_pi_2(N)
dif1 = math.fabs(lbnc - math.pi)
dif2 = math.fabs(mtkl - math.pi)

print(dif1, lbnc)
print(dif2, mtkl)

if dif1 < dif2:
	print("The first method is more accurate")
else:
	print("The second method is more accurate")
