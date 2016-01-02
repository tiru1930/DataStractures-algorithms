from stack import Stack

def parChacker(SymbolString):
	stack = Stack()
	balanced = True
	index =0
	while index < len(SymbolString) and balanced:
		symbl= SymbolString[index]
	        if symbl in "{[(": 
			stack.push(symbl)
		else:
			if stack.isEmpty():
				balanced = False
			else:
				top=stack.pop()
				if not matches(top,symbl):
					balanced = False
	        index = index +1
	if balanced and stack.isEmpty():
		return True
	else:
		return False

def matches(open,close):
	openers="{[("
	closers="}])"
	return openers.index(open) == closers.index(close)
	

test1="((((()))))"
print parChacker(test1)

test2="(((())"
print parChacker(test2)

print(parChacker('{{([][])}()}'))
print(parChacker('[{()]'))
