""" Testing for Sum of two lowest positive integers
try Built-in Types - List
"""

def sum_two_smallest_numbers(numbers):
    # numbers = []
    numbers.sort()
    return numbers.pop(0) + numbers.pop(0)


a = [5, 8, 12, 18, 22]

print(a)
print(sum_two_smallest_numbers(a))


# ---
# this option is BETTER
# +++
# return sum(sorted(numbers)[:2])
