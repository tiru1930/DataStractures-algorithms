
def recMc(coinList,change):

	mincoins = change
	if change in coinList:
		return 1
	else:
		for i in[c for c in coinList if c<=change]:
			numcoins = 1 + recMc(coinList,change-i)
			if numcoins <= mincoins:
				mincoins = numcoins
	
	return mincoins


def recDec(coinList,change,knowresult):

	mincoins = change
	if change in coinList:
		knowresult[change]=1
		return 1
	elif knowresult[change]>0:
		return knowresult[change]
	else:
		for i in[c for c in coinList if c<=change]:
			numcoins = 1 + recDec(coinList,chage-i,knowresult)
			if numcoins <= mincoins:
				mincoins = numcoins
				knowresult[change]=mincoins
	return mincoins



print recMc([1,5,10,25],63)
