#!/usr/bin/python3
""" Pascal Triangle """


def pascal_triangle(n):
    pascal = []

    if n <= 0:
        return pascal
    pascal = [[1]]

    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        for j in range(len(pascal[i - 1]) - 1):
            row.append(pascal[i - 1][j] + pascal[i - 1][j + 1])         
        row.append(1)
        pascal.append(row)

    return pascal
