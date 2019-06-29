""" Testing Once_and_Zero
with another algorithm
"""


def binary_array_to_number(arr):
    s = sum(d * 2 ** i for i, d in enumerate(reversed(arr)))
    return s


mass = [1, 1, 0, 1]
print('new answer = ', binary_array_to_number(mass))
