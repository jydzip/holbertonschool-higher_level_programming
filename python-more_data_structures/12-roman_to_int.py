#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    if not roman_string:
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
    for letter in roman_string:
        result += _romans.get(letter, 0)
    return result
