#!/usr/bin/python3
"""
MakeChange
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount.

    Parameters:
    coins (list): A list of the values of the coins in your possession.
    total (int): The total amount to make change for.

    Returns:
    int: The fewest number of coins needed to meet the total,
    or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    # Initialize the dp array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Process each coin
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # Return the result
    return dp[total] if dp[total] != float('inf') else -1
