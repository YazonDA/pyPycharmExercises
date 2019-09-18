def prime_(n):
	a = list(range(n+1))
	a[1] = 0
	lst = []
	i = 2
	while i <= n:
	    if a[i] != 0:
	        lst.append(a[i])
	        for j in range(i, n+1, i):
	            a[j] = 0
	    i += 1
	return lst


a = 10000
zz = prime_(a)
for i in range(0, len(zz), 12):
	print(zz[i: i+12])

'''
a = 10000
for i in range(1000, a+1, 1000):
	print('-------------')
	t1 = Timer(lambda: smpl_nmbr(i))
	print(f'TIME smpl_nmbr({i}) - {int((t1.timeit(number=100))*1000)}')
	t2 = Timer(lambda: prime_(i))
	print(f'TIME prime_({i}) - {int((t2.timeit(number=100))*1000)}')

TIME smpl_nmbr(30) - 1374
TIME prime_(30) - 985
-------------
TIME smpl_nmbr(35) - 1385
TIME prime_(35) - 1110
-------------
TIME smpl_nmbr(40) - 1369
TIME prime_(40) - 1224
-------------
TIME smpl_nmbr(45) - 1375
TIME prime_(45) - 1397
-------------
TIME smpl_nmbr(50) - 1386
TIME prime_(50) - 1520
-------------
TIME smpl_nmbr(55) - 1371
TIME prime_(55) - 1640
-------------
TIME smpl_nmbr(60) - 2818
TIME prime_(60) - 1796
-------------
TIME smpl_nmbr(65) - 2800
TIME prime_(65) - 1917
-------------
TIME smpl_nmbr(70) - 2791
TIME prime_(70) - 2066
-------------
TIME smpl_nmbr(75) - 2788
TIME prime_(75) - 2237
-------------
TIME smpl_nmbr(80) - 2791
TIME prime_(80) - 2321
-------------
TIME smpl_nmbr(85) - 2824
TIME prime_(85) - 2467
-------------
TIME smpl_nmbr(90) - 4398
TIME prime_(90) - 2576
-------------
TIME smpl_nmbr(95) - 4417
TIME prime_(95) - 2692
-------------
TIME smpl_nmbr(100) - 4409
TIME prime_(100) - 2790
-------------
TIME smpl_nmbr(1000) - 145
TIME prime_(1000) - 35
-------------
TIME smpl_nmbr(2000) - 482
TIME prime_(2000) - 70
-------------
TIME smpl_nmbr(3000) - 1018
TIME prime_(3000) - 105
-------------
TIME smpl_nmbr(4000) - 1702
TIME prime_(4000) - 140
-------------
TIME smpl_nmbr(5000) - 2545
TIME prime_(5000) - 176
-------------
TIME smpl_nmbr(6000) - 3539
TIME prime_(6000) - 210
-------------
TIME smpl_nmbr(7000) - 4716
TIME prime_(7000) - 247
-------------
TIME smpl_nmbr(8000) - 5940
TIME prime_(8000) - 279
-------------
TIME smpl_nmbr(9000) - 7402
TIME prime_(9000) - 317
-------------
TIME smpl_nmbr(10000) - 8999
TIME prime_(10000) - 351

def smpl_nmbr(n):

	def check_mult(x):
		for z in sn:
			if x%z == 0:
				return
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


'''