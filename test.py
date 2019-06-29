""" Testing for Square(n) Sum

"""


def square_sum(numbers):
    return sum(list(map(lambda x: x ** 2, numbers)))


a = [0, 3, 4, 5]

print(square_sum(a))
print(a)


# --- This is not understood enough ---
# +++
# this algorithm is more simple
# +++
# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)
