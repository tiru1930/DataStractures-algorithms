def listSum(listNum):
	if len(listNum)==1:
		return listNum[0]
	else:
		return listNum[0]+listSum(listNum[1:])


print (listSum([1,2,3,4,5]))
