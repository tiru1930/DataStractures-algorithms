
def fact(Num):
	if Num<=1:
		return 1
	else:
		return Num*fact(Num-1)

print fact(5)
