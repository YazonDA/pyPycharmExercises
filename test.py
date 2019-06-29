""" Testing filter - function

"""


def f(x):
    if x >= 2:
        return True
    return False

a = [0, 1, 2, 3, -1, 5, -2, 6]
print(list(filter(f, a)))
