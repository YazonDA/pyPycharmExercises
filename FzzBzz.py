def fb(lst):
	for i in range(len(lst)):
		n = lst[i]
		lst[i] = "Fizz"*(n%3==0) + "Buzz"*(n%5==0) or n
'''
		if lst[i]%3 == 0 and lst[i] != 0:
			if lst[i]%5 == 0:
				lst[i] = 'FizzBuzz'
			else:
				lst[i] = 'Fizz'
		elif lst[i]%5 == 0 and lst[i] != 0:
			lst[i] = 'Buzz'
'''
a = list(range(1, 51))
print(a)
fb(a)
print(a)
