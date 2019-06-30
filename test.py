""" Testing for Vasya - Clerk
Tags - FUNDAMENTALS MATHEMATICS ALGORITHMS NUMBERS GAMES
"""


def tickets(people):
    cash_box = {25: 0,
                50: 0,
                100: 0}
    # This string for service print only
    # cash_sum = lambda s: sum(s[x] * x for x in s)
    for pay in people:
        change = pay - 25
        cash_box[pay] += 1
        if change == 25:
            cash_box[25] -= 1
        elif change == 75:
            cash_box[25] -= 1
            if cash_box[50] == 0:
                cash_box[25] -= 2
            else:
                cash_box[50] -= 1
        if cash_box[25] < 0 or cash_box[50] < 0:
            return "NO"
    return "YES"


# a = [25, 25, 50]
# a = [25, 100]
# a = [25, 25, 50, 100, 25, 100]
# a = [25, 25, 50, 50, 100, 25, 25, 25, 100]
a = [25, 25, 50, 25, 25, 100, 25, 25, 25, 100]

# print(a)
print(tickets(a))

# this solutions is CORRECT
#   +++
# def tickets(people):
#   till = {100.0:0, 50.0:0, 25.0:0}
#   for paid in people:
#     till[paid] += 1
#     change = paid-25.0
#     for bill in (50,25):
#       while (bill <= change and till[bill] > 0):
#         till[bill] -= 1
#         change -= bill
#     if change != 0:
#       return 'NO'
#   return 'YES'
#   +++
# def tickets(a):
#     n25 = n50 = n100 = 0
#     for e in a:
#         if   e==25            : n25+=1
#         elif e==50            : n25-=1; n50+=1
#         elif e==100 and n50>0 : n25-=1; n50-=1
#         elif e==100 and n50==0: n25-=3
#         if n25<0 or n50<0:
#             return 'NO'
#     return 'YES'
#   +++
#   ---
#   my solution NOT OPTIMAL :((((
