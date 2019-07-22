""" Testing for - Human readable duration format

find solutions
"""


seconds = 36620012
ans_dict = [60, 60, 24, 365, 365]
ans_dict_1 = [1, 60, 60*60, 24*3600, 365*24*3600, 1]
ans_list = [(seconds // (ans_dict_1[i])) % ans_dict[i] for i in range(5)]

print(ans_list)
ans_list = []

for i in range(5):
    a3 = ans_dict[i]
    a2 = ans_dict_1[i]
    a4 = seconds // a2
    a1 = a4 % a3
    ans_list.append(a1)
    # seconds = seconds // ans_dict[i]

print(ans_list)
print(seconds)
