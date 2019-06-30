""" Testing for Find the next perfect square!

"""

def find_next_square(sq):
    s = int(pow(sq, 0.5))
    if s ** 2 == sq:
        return int((s + 1) ** 2)
    return -1


a = 145

print(a)
print(find_next_square(a))


# ---
# this option is BETTER
#   +++
# x = sq**0.5
# return -1 if x % 1 else (x+1)**2
#   +++
# root = sq ** 0.5
# if root.is_integer():
#   return (root + 1)**2
# return -1
