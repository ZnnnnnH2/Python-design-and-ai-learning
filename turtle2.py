import io
import turtle as tu
from PIL import EpsImagePlugin

from PIL import Image

tu.setup(100000,10000,0,0)
EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs10.04.0\bin\gswin64c'
basicLength = 3.0
length = 3
tu.pensize(3)
tu.speed(0)
tu.colormode(255)
r,g,b = 255,255,255
k = -1
def get_color(aa, bb, cc):
	global k
	aa,bb,cc = aa+k, bb+k, cc+k
	if aa<=0 or aa>=255:
		k = -k
	return aa,bb,cc
tu.begin_fill()
for i in range(255):
	for j in range(2):
		r,g,b = get_color(r,g,b)
		tu.pencolor(r,g,b)
		tu.forward(length)
		tu.left(90)
	length = length + basicLength
tu.end_fill()

screen = tu.Screen()
canvas = screen.getcanvas()
ps = canvas.postscript(colormode='color')

image = Image.open(io.BytesIO(ps.encode('utf-8')))
image.save("turtle2.png")

tu.done()