class Deque(object):

	def __init__(self):
		self.items = []

	def addfront(self,item):
		self.items.append(item)

	def addrare(self,item):
		self.items.insert(0,item)

	def removefront(self):
		return self.items.pop()
	
	def removerare(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return self.items == []
