#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_row = list(map(lambda num: pow(num, 2), i))
        new_matrix.append(new_row)
    return new_matrix
