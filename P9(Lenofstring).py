
str = "kjgfkjgkf"


def stringLength(str) :
	
	if str == '':
		return 0
	else :
		return 1 + stringLength(str[1:]) 
	

print (stringLength(str))


