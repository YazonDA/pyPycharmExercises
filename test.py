""" Testing for Sort the odd
Tags - FUNDAMENTALS ARRAYS
"""


def sort_array(source_array):
    odd_arr = sorted(x for x in source_array if x % 2)
    j = 0
    for i in range(len(source_array)):
        if source_array[i] % 2:
            source_array[i] = odd_arr[j]
            j += 1
    return source_array


a = [5, 3, 2, 8, 1, 4]      #[1, 3, 2, 8, 5, 4]
# a = [5, 3, 1, 8, 0]         #[1, 3, 5, 8, 0]

# print(a)
print(sort_array(a))

# this solutions is VERY GOOD (imho)
#   +++
# def sort_array(arr):
#   odds = sorted((x for x in arr if x%2 != 0), reverse=True)
#   return [x if x%2==0 else odds.pop() for x in arr]
#   +++
#   ---
#   my solution NOT OPTIMAL :((((
