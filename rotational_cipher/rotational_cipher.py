def rotate(val, num):
	return "".join([chr(shift_one_char(x,num)) for x in val])	

def shift_one_char(char,num):
	if ord(char) >= 97 and ord(char) <= 122:
		return ord(char)+num if ord(char)+num <= 122 else ((ord(char)+num)-123)+97
	elif ord(char) >= 65 and ord(char) <= 90:
		return ord(char)+num if ord(char)+num <= 90 else ((ord(char)+num)-91)+65
	else:
		return ord(char)