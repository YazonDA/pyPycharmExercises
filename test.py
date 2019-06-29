""" Testing Once_and_Zero
with another algorithm
"""


def binary_array_to_number(arr):
    s = int(''.join(str(e) for e in arr), 2)
    return s


mass = [1, 0, 0, 1]
print('new answer = ', binary_array_to_number(mass))
