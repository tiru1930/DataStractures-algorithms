
class Node(object):

	def __init__(self,datafield):
		self.data = datafield
		self.next = None

	def getData(self):
		return self.data
	
	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data = newdata

	def setNext(self,newnext):
		self.next = newnext

class unorderedlist(object):

	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp
	
	def size(self):
		current = self.head
		count =0;
		while current != None:
			count = count +1
			current = current.getNext()

		return count

	def search(self,item):
		current = self.head
		found = False
		while current != None and found != True:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self,item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext=(current.getNext())


mylist = unorderedlist()
for i in range(0,12,2):
	mylist.add(i)
print mylist.size()
mylist.add(20)
print mylist.size()
print mylist.search(2)
print mylist.search(20)
mylist.remove(20)
print mylist.size()
print mylist.head.getData()	
