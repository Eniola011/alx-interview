#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
        Calculate the fewest number of operations needed to result...
        in exactly n H characters in the file.
        Args:
            n: number of H characters.
        Return:
            An integer
            0 if n is impossible to achieve.
    """
    res = 0
    idx = 2

    if n < 2:
        return 0

    while (idx < n + 1):
        while n % idx == 0:
            res += idx
            n /= idx
        idx += 1

    return res
