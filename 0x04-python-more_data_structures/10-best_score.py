#!/usr/bin/python3

def best_score(a_dictionary):
    count = 0
    max = ""
    if a_dictionary is None:
        return None

    for key, value in a_dictionary.items():
        if value > count:
            count = value
            max = key
    return max
