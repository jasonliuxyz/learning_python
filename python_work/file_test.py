f1 = open('/Users/liucheng/Downloads/a')
l = f1.read()
f1.close

f2 = open('/Users/liucheng/Downloads/b', 'w')
f2.write(l)
f2.close


answer = input('what do you want to save in txt:')
f3 = open('/Users/liucheng/Downloads/c', 'w')
f3.write(answer)
f3.close