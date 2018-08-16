#print(%)字符串格式化输出
from random import randint

num=randint(1, 100)
tag=True

while tag:
	answer=int(input('pleas input your guess num:'))
	if answer > num:
		print('%d is too big' %answer)
	if answer < num:
		print('%d is too small' %answer)
	if answer == num:
		print('%d is equal' %answer)
		tag=False