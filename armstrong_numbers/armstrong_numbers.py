def is_armstrong(num):
	xp = len(str(num))
	val = sum([int(x)**xp for x in str(num)])
	return val == num
	
#print(is_armstrong(153))
