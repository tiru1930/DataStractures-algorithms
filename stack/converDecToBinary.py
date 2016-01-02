from stack import Stack

def DecToBinary(DecNum):
	s=Stack()
	while DecNum>0:
		rem = DecNum%2
		s.push(rem)
		DecNum = DecNum / 2

	BinaryNum=""
 	while not s.isEmpty():
		BinaryNum = BinaryNum + str(s.pop())

	return BinaryNum

print DecToBinary(42)
		
