""" Testing for - Alphabetical Addition
find solutions
"""

#import pysnooper

#@pysnooper.snoop()
def add_letters(*l):
	letters = list(l)
	print(letters)
	l = list(map(lambda x: ord(x), letters))
	print(l)


a = [
["b", "o", "h", "y", "s", "r", "o", "j", "w"],
["d", "g", "z", "f", "i", "f", "q", "q", "t", "w"],
["n", "v", "v", "k", "e", "g", "u", "r", "o"],
["h", "t", "l", "a", "p", "e", "q", "r", "l"]
]
#'m' should equal 'e'
for i in a:
	print(i)
for i in a:
	print(list(map(lambda x: ord(x), i)))
for i in a:
	print(list(map(lambda x: ord(x)%96, i)))
for i in a:
	s1 = sum(list(map(lambda x: ord(x), i)))
	s2 = sum(list(map(lambda x: ord(x)%96, i)))
	print(s1, (s1%96)%26, s2, s2%26)

	

# add_letters('a', 'b', 'c') = 'f'
# add_letters('a', 'b') = 'c'
# add_letters('z') = 'z'
# add_letters('z', 'a') = 'a'
# add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
# add_letters() = 'z'
#add_letters("b", "o", "h", "y", "s", "r", "o", "j", "w")
#'m' should equal 'e'
#add_letters("z", "u", "l", "e", "l", "c", "p", "y")
#'x' should equal 'p'
'''
add_letters("b", "o", "h", "y", "s", "r", "o", "j", "w")
'm' should equal 'e'
add_letters("d", "g", "z", "f", "i", "f", "q", "q", "t", "w")
'm' should equal 'e'
add_letters("n", "v", "v", "k", "e", "g", "u", "r", "o")
'm' should equal 'e'
add_letters("h", "t", "l", "a", "p", "e", "q", "r", "l")
'm' should equal 'e'
'''