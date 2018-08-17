# -*- coding: utf-8 -*-
# Copyright 2018 jason


import random

def choice(n, m):
	if 1 <= int(m) <= int(n):
		return 	sorted(random.sample([i for i in range(1, int(n)+1)], int(m)))
	else:
		return "请确认 '1<=m<=n'!"

#从1-1000随机取99个数字.
print(choice(1000, 99))