
def MoveToTower(height,fromPole,toPole,withPole):
	if height>=1:
		MoveToTower(height-1,fromPole,withPole,toPole)
		MoveDisk(fromPole,toPole)
		MoveToTower(height-1,fromPole,toPole,withPole)

def MoveDisk(fp,tp):
	print("moving disk from",fp,"to",tp)

MoveToTower(64,"A","B","C")
