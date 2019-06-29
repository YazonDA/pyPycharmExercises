""" Testing for How_Green_Is_My_Valley
another algorithm
"""


def make_valley(arr):
    arr = sorted(arr, reverse=True)
    return arr[::2] + arr[1::2][::-1]


a = [8, 12, 10, -1, 31, -4]

print(make_valley(a))
print(a)