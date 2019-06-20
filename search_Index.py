import re
import input_Text


def search_words(pref, s_text):
    """ Prefix match search and matching words list Module.
    Matches only at the beginning of the words.

    :param pref: string()
    :param s_text: tuple(words)
    :return: tuple(words)
    """

    s = [i for i in s_text if re.match(pref, i) is not None]
    return tuple(s)


struct_text = input_Text.txt2list('inputStruct.txt')


ans = search_words('ант', struct_text)
print(ans)


# simple comment for test git
