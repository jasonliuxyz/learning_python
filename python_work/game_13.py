from random import randint

f = open('./game.txt')
score = f.read().split()
f.close()

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])

if game_times != 0:
	avg_times = float(total_times) / game_times
else:
	avg_times = 0

print('你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' % (game_times, min_times, avg_times))

num=randint(1,100)
times = 0
tag=True

while tag:
	times += 1
	answer=int(input('please input your guess num:'))
	if answer > num:
		print('too big')
	if answer < num:
		print('too small')
	if answer == num:
		print('equal')
		tag=False

if game_times == 0 or times < min_times:
	min_times = times

total_times += times
game_times += 1
result = '%d %d %d' % (game_times, min_times, total_times)

f = open('./game.txt', 'w')
f.write(result)
f.close()