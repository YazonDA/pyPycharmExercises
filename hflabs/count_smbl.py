file_name = 'QAtest.txt'
with open(file_name) as arg_file:
	part = 1024
	count_a_rus = 0
	count_a_eng = 0
	count_s = 0
	# i = 0
	for portion in iter(lambda: arg_file.read(part), ''):
		count_a_rus += portion.count('а')
		count_a_eng += portion.count('a')
		count_s += portion.count('\n')
		# i += 1
		# print(i)

print(f'count_a_rus == {count_a_rus }')
print(f'count_a_eng == {count_a_eng }')
print(f'count_s == {count_s }')
