from collections import Counter

def swapchars(s):

	charCount = Counter()

	for c in s:
		if (c.isalpha()):
			charCount[c.lower()] += 1

	cmax, x = charCount.most_common(len(charCount))[0]
	cmin, y = charCount.most_common(len(charCount))[-1]

	strMod = list(s)

	for i in range(len(strMod)):
		if strMod[i].lower() == cmax:
			strMod[i] = cmin
		elif strMod[i].lower() == cmin:
			strMod[i] = cmax

	return ''.join(strMod)