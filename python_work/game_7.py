
from random import randint
from gam_8 import isEqual as iE

def isEqual(num1, num2):
	if num1 < num2:
		print('too small')
		return False;

	if num1 > num2:
		print('too big')
		return False;

	if num1 == num2:
		print('bingo')
		return True

num = randint(1, 100)
bingo = False
while bingo == False:
	answer = int(input('please input your guess num:'))
	bingo = iE(answer, num)