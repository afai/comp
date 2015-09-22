f = open("states.txt", "r")

stateDict = {}

for l in f:
    d = l.split(",")
    stateDict[d[1][:-1]] = d[0]

f.close()

def abbrevToState(ab):
	if stateDict[ab] == None:
		print "This is not a state abbreviation!"
	else:
		print stateDict[ab]

abbrevToState("PA")