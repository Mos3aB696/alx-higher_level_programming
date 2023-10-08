#!/usr/bin/python3
def multiple_returns(sentence):  # test
    if len(sentence) > 0:
        n = len(sentence)
        f_char = sentence[0]
        return n, f_char
    else:
        return 0, None
