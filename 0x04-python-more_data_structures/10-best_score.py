#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        dict_values = list(a_dictionary.values())
        max_val = max(dict_values)
        for key, val in a_dictionary.items():
            if val == max_val:
                return key
    else:
        return None
