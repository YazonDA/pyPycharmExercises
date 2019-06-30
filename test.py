""" Testing for Number of People in the Bus
try Built-in Types - List
"""


def number(bus_stops):
    # s = 0
    # for i in bus_stops:
    #     s += i[0] - i[1]
    return sum(i[0] - i[1] for i in bus_stops)


a = [[10, 0], [3, 5], [5, 8]]
print(a)
print(number(a))


# +++
# This option is more elegant
# return sum(i - j for i, j in bus_stops)
