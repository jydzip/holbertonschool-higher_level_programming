#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    if not roman_string or not isinstance(roman_string, str):
        return result

    _romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    for i in range(len(roman_string)):
        letter = roman_string[i]
        try:
            next_letter = roman_string[i + 1]
        except Exception:
            next_letter = None

        if letter == "I" and next_letter in ["V", "X"]:
            result += -2
        elif letter == "C" and next_letter in ["M"]:
            result += -200
        result += _romans.get(letter, 0)
    return result
