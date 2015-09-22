import operator

def sortcat(n, *arg):

	if n > len(arg):
		raise ValueError()

	if n == -1:
		num = len(arg)
	else:
		num = n

	strCount = {}
	for s in arg:
		strCount[s] = len(s)

	sortedStrings = sorted(strCount.items(), key=operator.itemgetter(1))

	strConcat = []

	for i in range(num):
		key, value = sortedStrings[(i+1)*-1]
		strConcat.extend(key)

	print ''.join(strConcat)