=================================
# simple
# number ==> string ==> list
s = list(str(n))

=================================
# simple
# reverse string
n = str(n)[::-1]

=================================
# simple
# GCD (greatest common divisor)
while a!=0:
	a,b = b%a, a
# where 'b' is the answer

=================================
# simple
# sum of all digits of a number
sum(map(int, str(c)))

=================================
# nice
# open/close file
with open('path', 'r') as reader:
    # Further file processing goes here

=================================
# simple
# measure speed in prog
from timeit import Timer
t1 = Timer(lambda: min(w_arr))
print(f'TIME max - {t1.timeit(number=1000)}')
# min(w_arr) - whose speed

=================================
# simple
# delete all duble
# var 1
dict.keys(dict.fromkeys(z, 1))
# var 2 ( 25~30% faster)
list(set(a))

=================================
# simple
# logging/debuging
import pysnooper
@pysnooper.snoop()
def something():
	pass