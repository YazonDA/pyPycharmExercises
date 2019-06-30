""" Testing for Regex validate PIN code
try Built-in Types - Bool
"""


def validate_pin(pin):
    # return (len(pin) == 4 or len(pin) == 6)
    return pin.isdecimal() and (len(pin) == 4 or len(pin) == 6)


x = '1456'
print(validate_pin(x))


# This is a GOOD option
# +++
# def validate_pin(pin):
#     return len(pin) in (4, 6) and pin.isdigit()
