from random import choice

score = [0, 0]
director = ['left', 'center', 'right']

def kick():
	print('====  You Kick! ====')
	you = input('Choose one side to shoot:left,center,right:')
	print('you kicked:' + you)
	com = choice(director)
	print('computer saved:' + com)

	if you != com:
		print('Goal!')
		score[0] += 1
	else:
		print('Oops...')
	print('Score: %d(you) - %d(com)\n' % (score[0], score[1]))

	print('====  You Save! ====')
	you = input('please one side to shoot:left,center,right: ')
	print('you saved: ' + you)
	com = choice(director)
	print('computer kicked:' + com)
	if you == com:
		print('Saved!')
	else:
		print('Oops...')
		score[1] += 1
	print('Score: %d(you) - %d(com)\n' % (score[0], score[1]))

for i in range(5):
	print('==== Round %d ====' %(i+1))
	kick()

while(score[0] == score[1]):
	i += 1
	print('==== Round %d ====' %(i+1))
	kick()

if score[0] > score[1]:
	print('you win!')
else:
	print('you Lose!')

