#!/usr/bin/python3
def uppercase(str):
    formated_str = []

    for i in range(len(str)):
        s = str[i]
        unicode = ord(s)
        if unicode >= 97 and unicode <= 122:
            s = chr(unicode - 32)
        formated_str.append(s)

    new_str = ''.join(formated_str)
    print(new_str)
    return new_str
