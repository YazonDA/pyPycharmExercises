a = [[
[3, 5, 7, 9], [4, 5, 7, 9], [6], [1], [2, 3, 4], [3, 4, 7], [2, 7, 9], [2, 5, 7, 9], [8]
], [
[5, 7], [8], [1, 4, 5], [2, 6, 7], [9], [4, 6, 7], [1, 2, 6, 7], [3], [1, 2, 5, 7]
], [
[2], [1, 7, 9], [1, 3, 9], [3, 6, 7, 8], [3, 6, 8], [5], [4], [1, 6, 7, 9], [1, 7, 9]
], [
[4], [5, 6, 9], [2, 5, 9], [2, 3, 5, 6], [2, 3, 6], [1], [8], [2, 5, 6, 7, 9], [2, 5, 7, 9]
], [
[5, 6, 8, 9], [3], [1, 2, 5, 9], [2, 5, 6, 8], [7], [6, 8], [1, 2, 6, 9], [4], [1, 2, 5, 9]
], [
[5, 6, 8], [1, 5, 6], [7], [9], [2, 4, 6, 8], [4, 6, 8], [1, 2, 6], [1, 2, 5, 6], [3]
], [
[3, 5, 7, 9], [5, 7, 9], [8], [4], [1], [3, 7, 9], [2, 3, 7, 9], [2, 7, 9], [6]
], [
[3, 6, 7, 9], [2], [3, 4, 9], [3, 6, 7], [5], [3, 6, 7, 9], [1, 3, 7, 9], [8], [1, 4, 7, 9]
], [
[1], [4, 6, 7, 9], [3, 4, 9], [3, 6, 7, 8], [3, 6, 8], [2], [5], [7, 9], [4, 7, 9]
]]


#for row in range(9):
for row in range(9):
	ss = a[row]
	for column in range(0,9,3):
		st = ss[column:]+ss[:column]
		print(f'row = {row}, column = {column}')
		print(st)
		print()
print(a[0][6:9])