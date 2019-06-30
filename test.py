""" Testing for Who likes it?
Tags - FUNDAMENTALS FORMATTING ALGORITHMS STRINGS
"""

def likes(names):
    count_more = str(len(names) - 2)
    ln = len(names) if len(names) <= 4 else 4
    names.extend([''] * (4 - ln))
    end_answer_1 = 'likes this'
    end_answer_2 = 'like this'
    my_dict = {0: ['no one', end_answer_1],
               1: [names[0], end_answer_1],
               2: [names[0] + ' and ' + names[1], end_answer_2],
               3: [names[0] + ', ' + names[1] + ' and ' + names[2], end_answer_2],
               4: [names[0] + ', ' + names[1] + ' and ' + count_more + ' others', end_answer_2]}
    return F'{my_dict[ln][0]} {my_dict[ln][1]}'


# a = []
# a = ['Peter']
# a = ['Jacob', 'Alex']
# a = ['Max', 'John', 'Mark']
# a = ['Alex', 'Jacob', 'Mark', 'Max']
a = ['Alex', 'Jacob', 'Mark', 'Max', 'Peter']

print(a)
print(likes(a))

# this solution is CORRECT
#   +++
# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this',
#         2: '{} and {} like this',
#         3: '{}, {} and {} like this',
#         4: '{}, {} and {others} others like this'
#         }[min(4, n)].format(*names[:3], others=n-2)
#   ---
#   my solution difficult :((((
