""" Testing for - Square into Squares. Protect trees

"""


def decompose(n):
    ans = n[:]
    sq_unit = lambda x: x ** 2
    sq_arr = lambda x: sum(map(sq_unit, x))
    test_unit = int(((8 ** 2 - ans[1] ** 2) ** 0.5) // 1)
    print(test_unit)
    return sq_arr(n)


a = [1, 2, 3]

print(decompose(a))
