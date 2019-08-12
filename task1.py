'''
Input arg:
	
'''

import sys
import numpy

# in_arg scheme is worked
file_path = '/home/yazonda/Documents/PL_IV_TT/test_data/td_for_task1_001'
# sys.argv[1]

with open(file_path, 'r') as in_arg_file:
	a = numpy.array([float(i) for i in in_arg_file.read().splitlines()])

a1 = numpy.percentile(a, q=90)
a2 = numpy.percentile(a, q=50), numpy.median(a)
a3 = max(a)
a4 = min(a)
a5 = numpy.mean(a)
# print(numpy.get_printoptions())
# numpy.set_printoptions(precision=3, floatmode='fixed')
numpy.set_printoptions(precision=3, floatmode='fixed')
print(float(0.4565789))
# print(numpy.get_printoptions())
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(float(0.4565789))
