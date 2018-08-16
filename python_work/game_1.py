
num=10
print('input your guess num')
answer=int(input())

result = answer > num
print('too big')
print(result)

result = answer < num
print('too small')
print(result)

result = answer == result
print('equal')
print(result)
