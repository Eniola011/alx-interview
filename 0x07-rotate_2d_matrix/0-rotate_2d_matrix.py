#!/usr/bin/python3
"""

Rotate 2D-Matrix.

"""


def rotate_2d_matrix(matrix):
    """
       >> Rotate 2D-Matrix 90 Degrees Clockwise.
    """
    number = len(matrix)
    # exchange the matrix. switch the rows and columns
    for i in range(number):
        for j in range(i, number):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse each row
    for row in matrix:
        row.reverse()
