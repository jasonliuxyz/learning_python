from random import choice

score_you = 0
score_com = 0
direction = ['left', 'center', 'right']

for i in range(5):
	print('==== Round %d - You Kick! ====' %(i+1))
	you = input('Choose one side to shoot:left,center,right:')
	print('you kicked:' + you)
	com = choice(direction)
	print('computer saved:' + com)

	if you != com:
		print('Goal!')
		score_you += 1
	else:
		print('Oops...')
	print('Score: %d(you) - %d(com)\n' % (score_you, score_com))

	print('==== Round %d - You Save! ====' % (i+1))
	you = input('please one side to shoot:left,center,right: ')
	print('you saved: ' + you)
	com = choice(direction)
	print('computer kicked:' + com)
	if you == com:
		print('Saved!')
	else:
		print('Oops...')
		score_com += 1
	print('Score: %d(you) - %d(com)\n' % (score[0], score[1]))