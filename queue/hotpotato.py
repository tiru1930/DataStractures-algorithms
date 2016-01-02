from queue import Queue

def hotpotato(namelist,num):
	circle = Queue()
	for name in namelist:
		circle.enqueue(name)

	while circle.size()>1:
		for i in range(num):
			circle.enqueue(circle.dequeue())


		circle.dequeue()

	return circle.dequeue()

print(hotpotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
