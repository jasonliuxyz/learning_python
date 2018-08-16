#点球游戏
from random import choice

you = input('Choose one side to shoot: left,center,right: ')
direction = ['left', 'center', 'right']
computer = choice(direction)

print('you kicked:' + you)
print('computer kicked:' + computer)

if you == computer:
	print('Oops...')
else:
	print('Goal!')
