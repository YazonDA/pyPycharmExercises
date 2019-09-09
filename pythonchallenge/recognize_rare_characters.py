import re
import string

files_name = 'ocr_text_01'
chars_dict = {}
chars_list = []
with open(files_name, 'r') as inp_string:
    for someth in inp_string:
        chars_list.append(someth)

a1 = []
chars_str = ''.join(chars_list)
ans = re.findall(r'[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}', chars_str)


for i in ans:
    print(i[4], end='')
