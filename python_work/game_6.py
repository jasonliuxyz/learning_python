from random import randint

def game6():
	answer = randint(1, 100)
	tag = True

	while tag:
		num = int(input('please input your guess num:'))
		if num > answer:
			print('too big')
		if num < answer:
			print('too small')
		if num == answer:
			print('equal')
			tag = False

game6()