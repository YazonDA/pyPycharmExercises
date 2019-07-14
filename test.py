""" Testing for - The Millionth Fibonacci Kata

find solutions
"""


def fib(n):
    def power(m1, n, m2, mult_m):
        if n == 0:
            ans = m2
        elif n == 1:
            ans = m1
        else:
            y = power(m1, n // 2, m2, mult_m)
            y = mult_m(y, y)
            if n % 2:
                y = mult_m(m1, y)
            ans = y
        return ans

    def make_matr(n):
        return [[1 if i == j else 0 for i in range(n)]
                for j in range(n)]

    def mult_matr(a, b):
        return [[sum(i * j for i, j in zip(Ya, Xb))
                for Xb in list(zip(*b))] for Ya in a]

    return power([[1, 1], [1, 0]], n, make_matr(2), mult_matr)[0][1]

a = 14
for i in range(a):
    print(fib(i))
# print(len(answer))
