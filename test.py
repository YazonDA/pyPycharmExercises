""" Testing atrr of object

"""
import string


def f(x):
    if x[:2] == '__':
        return True
    return False


# def f(x):
#     pass
#     return x


print(list(filter(f, [atr for atr in dir(string)])))
