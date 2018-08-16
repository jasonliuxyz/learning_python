x = int(input('please input a x:'))
y = int(input('please input a y:'))


if x >= 0:
	if y >= 0:
		print('1')
if x < 0:
	if y >= 0:
		print('2')
if x < 0:
	if y < 0:
		print('3')
if x >= 0:
	if y < 0:
		print('4')

