#!/usr/bin/python3
# returns a list of lists of integers representing the Pascal’s triangle of n


def pascal_triangle(n):
    if n <= 0:
        return []
    pascal = []
    for i in range(n):
        row = [1]  # first element of each row is 1
        if i > 0:
            prev = pascal[-1]  # previous row
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
            row.append(1)  # last element of each row is 1
        pascal.append(row)
    return pascal
