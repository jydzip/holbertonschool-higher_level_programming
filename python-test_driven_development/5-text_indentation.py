#!/usr/bin/python3
"""
    Function file for text_indentation.
"""


def text_indentation(text):
    """
        Prints a text with 2 new lines after each characters
        `.`, `?`, `:`
        Arguments:
            text (str): Text to formated.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentences = []
    pos = 0
    for i in range(len(text)):
        letter = text[i]
        _delimit = False

        if letter in [".", "?", ":"]:
            _delimit = True

        try:
            sentences[pos]
        except Exception:
            sentences.append("")
        sentences[pos] += letter

        if _delimit:
            pos += 1
            i += 1

    size = len(sentences)
    for i in range(size):
        sentence = sentences[i]
        if i == size - 1:
            print(sentence.strip(), end="")
        else:
            print(sentence.strip(), end="\n\n")
