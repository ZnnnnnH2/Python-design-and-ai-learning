import turtle as tu
import random as rd

tu.setup(100000,10000,0,0)
color = ["red","green","blue","yellow","purple","orange","black","white"]
basicLength = 20.0
length = 20
tu.pensize(5)
tu.speed(0)
get_color = lambda :rd.randint(0,7)
for i in range(1000):
	for j in range(2):
		tu.pencolor(color[get_color()])
		tu.forward(length)
		tu.left(90)
	length = length + basicLength
	basicLength = basicLength * 0.99