num=10
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