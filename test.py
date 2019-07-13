""" Testing for - Numbers that are a power of their sum of digits

find solutions
"""


def power_sumDigTerm(n):
    s = []
    s.extend(i ** p
             for p in range(2, 30)
             for i in range(7, 99)
             if sum(map(int, str(i ** p))) == i)
    s.sort()
    return s[n - 1]


a = 15
answer = power_sumDigTerm(a)
print(answer)
# print(len(answer))
