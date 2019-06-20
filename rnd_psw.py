import random
import string


def sr_psw(count, long):
    """ Module create string for pass.

    Charset for string includes letters, numbers and special characters. It`s variable my_dict
    :param count: <int> the number of strings
    :param long: <int> string length
    :return: <tuple> set of different string
    """
    my_dict = '!#$%&()*+,-.:;<=>?@[]^_{|}~' + string.ascii_lowercase + string.ascii_uppercase + \
              string.digits + string.digits + string.digits

    out_set = []
    for j in range(count):
        my_var_s = my_dict
        s = random.sample(my_var_s, long)

        for i in range(random.randint(1, 10)):
            random.shuffle(s)

        lm = ''.join(s)
        out_set.append(lm)

    return tuple(out_set)
