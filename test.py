""" Testing for Disemvowel Trolls
try Built-in Types - String
"""

def disemvowel(string):
    return ''.join(i for i in string if i not in 'euioaEUIOA')


a = "This website is for losers LOL!"

print(a)
print(disemvowel(a))


# ---
# I think this option is BETTER
# +++
# return ''.join(i for i in string.lower() if i not in 'euioa')
