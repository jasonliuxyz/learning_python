from random import randint

num=randint(1,100)
tag=True

while tag:
	answer=int(input('please input your guess num:'))
	if answer > num:
		print('too big')
	if answer < num:
		print('too small')
	if answer == num:
		print('equal')
		tag=False