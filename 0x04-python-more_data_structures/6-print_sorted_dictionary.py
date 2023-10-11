#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_list = list(a_dictionary)
    dict_list.sort()
    for i in dict_list:
        print(f"{i}: {a_dictionary.get(i)}")
