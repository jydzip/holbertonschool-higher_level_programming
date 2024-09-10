#!/usr/bin/python3
def best_score(a_dictionary):
    score = None
    key_score = None
    if a_dictionary:
        for key in a_dictionary:
            if score is None or a_dictionary[key] > score:
                score = a_dictionary[key]
                key_score = key
    return key_score
