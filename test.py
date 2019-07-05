""" Testing for - Square into Squares. Protect trees
Tag`s - FUNDAMENTALS MATHEMATICS ALGORITHMS NUMBERS SEQUENCES ARRAYS
4 kyu
"""


a = 'kjsbdvo'

b = ''.join(i for i in a if i.isdecimal())

len_b = len(b)

if len_b == 0:
    b = '0'
    len_b += 1

b = a[:-len_b] + str(int(b) + 1).zfill(len_b)

print(b, '- number')
print(len_b, '- number of digits')
