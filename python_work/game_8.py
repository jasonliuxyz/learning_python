def isEqual(num1, num2):
	if num1 > num2:
		print('too big')
		return False;
	elif num1 < num2:
		print('too small')
		return False;
	else:
		print('equal')
		return True;