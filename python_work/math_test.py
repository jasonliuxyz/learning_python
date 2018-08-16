import math

def fun():
	a = int(input('please input a:'))
	b = int(input('please input b:'))
	c = int(input('please input c:'))

	b2 = math.pow(b, 2)

	x1 = (-b + (math.sqrt(b2 - 4*a*c))) / (2*a)
	x2 = (-b - (math.sqrt(b2 - 4*a*c))) / (2*a)

	print(x1)
	print(x2)

fun()