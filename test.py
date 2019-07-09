""" Testing for - Fibo akin

search sample test
"""



def make_list_u(n):
    l = [0, 1, 1]
    for i in range(n + 1)[3:]:
        l.append(l[i - l[i - 1]] + l[i - l[i - 2]])
    l.remove(0)
    return l


def length_sup_u_k(n, k):
    c = make_list_u(n)
    # print('it`s True\n', c)
    j = 0
    for i in range(len(c))[2:]:
        if c[i] >= k:
            j += 1
    return j


def length_sup_u_k_1(n, k):
    return len(list(filter(lambda x: x >= k, make_list_u(n))))


for i in range(3, 100):
    for j in range(3, 100):
        # print()
        d_1 = length_sup_u_k(j, i)
        d_2 = length_sup_u_k_1(j, i)
        if d_1 != d_2:
            print(f'for n = {j} and k = {i} answers are not equal')
            # print(f'correct u(n)')
            print(f'correct = {d_1} & wrong = {d_2}')
            print()

j = 3332
i = 973
d_1 = length_sup_u_k(j, i)
d_2 = length_sup_u_k_1(j, i)

print(f'for n = {j} and k = {i} answers are not equal')
# print(f'correct u(n)')
print(f'correct = {d_1} & wrong = {d_2}')
print()