def smpl_nmbr(n):

	def check_mult(x):
		flag = True
		for z in sn:
			if x%z == 0:
				flag = False
				break
		if flag:
			sn.append(x)

	def create_list(x):
		suppose = []
		for k in k_sn:
			b = 30 * x + k
			# if suppose not in SimpleNumbers and not eq. 1
			if  b not in sn and b != 1:
				suppose.append(b)
		return suppose

	sn = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
	k_sn = [1, 7, 11, 13, 17, 19, 23, 29]
	i = 0

	while n > sn[-1]:
		for j in create_list(i):
			check_mult(j)
		i += 1
	sn.sort()
	return sn

a = 10000
#smpl_nmbr(a)
zz = smpl_nmbr(a)
for i in range(0, len(zz), 12):
	print(zz[i: i+12])