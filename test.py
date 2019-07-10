""" Testing for - Simple Fun #166: Best Match

diverse solutions
"""


def best_match(goals1, goals2):
    return min((a-b, -b, i) for i, (a, b) in enumerate(zip(goals1, goals2)))[2]


def my_best_match(goals1, goals2):
    res = [goals1[i] - goals2[i] for i in range(len(goals2))]
    ans_ind = [i for i in range(len(res)) if res[i] == min(res)]
    ans_goal = [goals2[i] for i in ans_ind]
    return ans_ind[ans_goal.index(max(ans_goal))]


a1, a2 = [2, 9, 14, 5, 16, 9, 9, 11, 10, 11, 11, 13, 14, 9, 12, 12, 10, 13],\
         [0, 0, 6, 1, 8, 7, 7, 6, 8, 5, 8, 9, 4, 7, 9, 2, 2, 4]

print(best_match(a1, a2))
print(my_best_match(a1, a2))
