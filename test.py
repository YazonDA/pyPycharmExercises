""" Testing for Sort the odd
Tags - FUNDAMENTALS ARRAYS
"""
from collections import Counter


def stock_list(listOfArt, listOfCat):
    if not listOfArt:
        return ''
    codePos = listOfArt[0].index(' ') + 1
    cnt = Counter()
    for s in listOfArt:
        cnt[s[0]] += int(s[codePos:])
    return ' - '.join('({} : {})'.format(cat, cnt[cat]) for cat in listOfCat)


b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
# c = ["A", "B"]
c = ["V", "S", "N", "M"]

# print(a)
print(stock_list(b, c))

# this solutions is VERY GOOD (imho)
#   +++
# def sort_array(arr):
#   odds = sorted((x for x in arr if x%2 != 0), reverse=True)
#   return [x if x%2==0 else odds.pop() for x in arr]
#   +++
#   ---
#   my solution NOT OPTIMAL :((((
