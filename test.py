""" Testing for - Next bigger number with the same digits

GOOD solution
"""


import itertools


def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            assa = list(filter(lambda x: x>t[0], t))
            m = min(assa)
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1


a = 4834333331
# ==> 687731708236

answer = next_bigger(a)
print(f'{a} => {answer}')