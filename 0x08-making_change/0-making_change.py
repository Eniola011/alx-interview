#!/usr/bin/python3
"""

MakeChange

"""


def makeChange(coins, total):
    """
       >> Determine the fewest number of coins needed
       ...to meet a given amount total.
       >> Args:
          > 'coins' is a list of the values of the coins in your possession.
       >> Return:
          > If total is 0 or less, return 0.
          > If total cannot be met by any number of coins you have, return -1.
    """
    # Base cases
    if total <= 0:
        return 0
    if len(coins) == 0:
        return -1

    # Create a table to store results of subproblems
    dp = [float('inf')] * (total + 1)

    # Base case (If given value is 0)
    dp[0] = 0

    # Compute minimum coins required for all values from 1 to total
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                subproblem = dp[i - coin]
                if subproblem != float('inf') and subproblem + 1 < dp[i]:
                    dp[i] = subproblem + 1

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
