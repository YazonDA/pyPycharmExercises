from timeit import Timer


def assa(m):

	def create_l_l(x):
		suppose = []
		for k in k_sn:
			b = 30 * x + k
			# if suppose not in SimpleNumbers and not eq. 1
			if  b not in sn and b != 1:
				suppose.append(b)

	def create_l_s(n):
		suppose = [30 * n + k for k in k_sn if (30 * n + k) not in sn and (30 * i + k) != 1]


	sn = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
	k_sn = [1, 7, 11, 13, 17, 19, 23, 29]
	i = 0

	while m > sn[-1]:
		input()
		print('===========================================')
		
		t1 = Timer(lambda: create_l_s(i))
		t2 = Timer(lambda: create_l_l(i))
		t3 = 100
		t_s = t1.timeit(number=t3)
		t_l = t2.timeit(number=t3)
		print(f'check_mult_s = {t_s:.5f} || check_mult_l = {t_l:.5f}')
		print(f'delta = {t_s / t_l:.2f}')

		i += 1

a = 50
print(assa(a))