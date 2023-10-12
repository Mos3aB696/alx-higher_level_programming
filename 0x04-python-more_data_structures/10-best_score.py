#!/usr/bin/python3
def best_score(a_dictionary):
    # Way One
    if a_dictionary:
        dict_values = list(a_dictionary.values())
        max_val = max(dict_values)
        for key, val in a_dictionary.items():
            if val == max_val:
                return key
    else:
        return None

    # Way Two
    # if a_dictionary:
    #    return max(a_dictionary, key=a_dictionary.get)
    # else:
    #    return None
