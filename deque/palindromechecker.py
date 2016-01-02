from deque import Deque

def palchecker(astring):
	indeque = Deque()
	isstillEqual = True

	for ch in astring:
		indeque.addfront(ch)

	while indeque.size() > 1 and isstillEqual:
		first = indeque.removefront()
		last  = indeque.removerare()
		if first != last:
			isstillEqual = False

	return isstillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
