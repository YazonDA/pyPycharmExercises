""" Testing for - Alphabetical Addition
find solutions
"""

import pysnooper

@pysnooper.snoop()
def add_letters(*l):
	letters = l # ist(l)
	if len(letters) == 0:
		return 'z'
	y08 = map(lambda x: ord(x)%96, letters)
	y09 = list(y08)
	y10 = sum(y09)%26 + 96
	ans = chr(y10)
	return ans


a = ['a', 'b', 'c']
asnwer = add_letters(a)
print(asnwer)
