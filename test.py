""" Testing for Remove the minimum
try Built-in Types - List
"""
import random


def remove_smallest(numbers):
    s = numbers[:]
    if len(s) != 0: s.remove(min(s))
    return s


a = [random.randint(0, 1000) for i in range(10)]
# generates the list
b = list(a)
# makes a swallow copy

print(a)
print(remove_smallest(a))
print(b)


# I used the
# s = numbers
# ---
# but this`s wrong. This`s only a link to the input array
# +++
# right - like this
# s = numbers[:]
