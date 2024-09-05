#!/usr/bin/python3
def remove_char_at(str, n):
    text = []
    i = 0
    for s in str:
        text.append(s)
        i += 1

    if n >= 0 and len(text) >= n:
        del text[n]
    return "".join(text)
