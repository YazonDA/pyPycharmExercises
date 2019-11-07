import numpy as np


class cell(object):
	# create cell with:
	#	number: int, unique;
	#	row: int, calculate;
	#	column: int, calculate;
	def __init__(self, ind):
		self.ind = ind
		self.suppose = list(range(1,10))

	def suppose(self,suppose):
		self.suppose = suppose


# init nine row
w_arr = np.array([cell(i) for i in range(81)])

print(f'len(w_arr) == {len(w_arr)}')
print(f'w_arr shape {w_arr.shape}')
print(f'ndim {w_arr.ndim}')
w_arr.resize(9,9)
print(f'after resize')
print(f'len(w_arr) == {len(w_arr)}')
print(f'w_arr shape {w_arr.shape}')
print(f'ndim {w_arr.ndim}')
for row in range(w_arr.shape[0]):
	for column in range(w_arr.shape[1]):
		print(w_arr[row, column].ind, w_arr[row, column].suppose)
