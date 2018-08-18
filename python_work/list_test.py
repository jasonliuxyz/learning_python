# -*- coding:utf-8 -*-

#列表添加一个元素
list = ['a', 'b', 'c']

print('append|添加前id:%s ' %id(list))
list.append('d')
print('append|添加后id:%s ' %id(list), list)
print('-'*64 )

print('extend|添加前id:%s ' %id(list))
list.extend('d')
print('extend|添加后id:%s ' %id(list), list)
print('-'*64 )

print('+=|添加前id:%s ' %id(list))
list += 'd'
print('+=|添加后id:%s ' %id(list), list)
print('-'*64 )

print('+|添加前id:%s ' %id(list))
list + ['d']
print('+|添加后id:%s ' %id(list), list)
print('-'*64 )


#列表添加一个列表
a = ['a', 'b', 'c']
print('append|添加前id:%s ' %id(a))
a.append(['d'])
print('append|添加后id:%s ' %id(a), a)
print('-'*64 )

a = ['a', 'b', 'c']
print('extend|添加前id:%s ' %id(a))
a.extend(['d'])
print('extend|添加后id:%s ' %id(a), a)
print('-'*64 )

a = ['a', 'b', 'c']
a += ['d']
print('+=|添加后id:%s ' %id(a), a)
print('-'*64 )

a = ['a', 'b', 'c']
print('+|添加前id:%s ' %id(a))
list + ['d']
print('+|添加后id:%s ' %id(a), a)

