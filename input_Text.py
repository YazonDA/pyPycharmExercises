import re


def txt2list(file_addr):
    """ Module for transform text
    from txt file to list of all words that make up the given text.

    :param file_addr: <string> file path and name
    :return: <tuple> set of all words from given text
    """

    with open(file_addr) as m_file:
        s_text = []
        # each line from the incoming file
        for line in m_file:
            # split into separate words
            # excluding non letters words
            s = [i for i in line.split() if (re.match(r'\W', i)) is None]
            # remove non letters char at the ends of words
            for i in range(len(s)):
                if re.match(r'\w', s[i][-1]) is None:
                    s[i] = s[i][:-1]
            # matching words add to returned dictionary
            s_text = s_text + s
        return tuple(s_text)


path_2_txt = 'text_2_process/'
target_file = path_2_txt + 'inputStruct.txt'
struct_text = txt2list(target_file)

with open(path_2_txt + 'outputStruct.txt', 'w') as my_file:
    for j in struct_text:
        my_file.write(j + ' ')

