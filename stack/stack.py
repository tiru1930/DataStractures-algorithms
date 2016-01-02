
class Stack(object):

	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items ==[]

	def push(self,data):
		self.items.append(data)

	def pop(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def peek(self):
		return self.items[len(self.items)-1]
