""" Testing for Beginner Series #3 Sum of Numbers
try Built-in Types - Range
"""


# def get_sum(a, b):
#     s = 0
#     if a > b:
#         a, b = b, a
#     for i in range(a, b + 1):
#         s += i
#     return s


def get_sum(a, b):
    if a > b: a, b = b, a
    return sum(i for i in range(a, b + 1))


x = 2
y = 1

print(get_sum(x, y))
