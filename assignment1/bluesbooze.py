f = open("states.txt", "r")

stateDict = {}

for l in f:
    d = l.split(",")
    stateDict[d[1][:-1]] = d[0]

f.close()

# If the function is called with a string of states separated by a comma,
# it will convert each to an abbreviation.

def stateToAbbrev(stateString):
	stateFound = False
	stateSplit = stateString.split(",")
	for i in range(len(stateSplit)):
		for ab, state in stateDict.iteritems():
			if state == stateSplit[i]:
				print ab
				stateFound = True
				break
		if not stateFound:
			print "This is not a state!"

stateToAbbrev("Pennsylvania")