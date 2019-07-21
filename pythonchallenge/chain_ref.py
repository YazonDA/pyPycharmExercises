import requests
import re


# s = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php')
# print(s.text)
#
# a = re.findall(r'[0-9]{5}', s.text)
# print(a)
#
# <a href="linkedlist.php?nothing=12345"><img src="chainsaw.jpg" border="0"></a>
# <body>and the next nothing is 44827</body>

ref_const = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
ref_var = '93781'
# print(ref_const + ref_var)
# ref_str = ref_const + ref_var
# print(ref_str)

for i in range(100):
    # ref_str = ref_const + ref_var
    s = requests.get(ref_const + ref_var)
    ref_var = re.findall(r'\d{1,}', s.text)[0]
    print(ref_var)
