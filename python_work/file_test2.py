
f = open('/Users/liucheng/Downloads/score.txt')
lines = f.readlines()
f.close
print(lines)

results = []

for line in lines:
	data=line.split()
	sum = 0
	print(data)
	for score in data[1:]:
		sum += int(score)
	result = '%s\t: %d\n' % (data[0], sum)
	results.append(result)

	output = open('/Users/liucheng/Downloads/result.txt', 'w')
	output.writelines(results)
	output.close


