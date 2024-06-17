#!/usr/bin/python3
"""Prime game module"""


def isWinner(x, nums):
    """Function that performs prime game"""
    if not nums or x < 1:
        return None

    n = max(nums)
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False  # 0 and 1 are not primes

    # Implement Sieve of Eratosthenes to find all primes up to n
    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1

    # Precompute the number of primes up to each index
    prime_count = [0] * (n + 1)
    count = 0
    for i in range(2, n + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count

    maria_wins = 0

    # Determine the winner for each game based on the number of primes
    for num in nums:
        if prime_count[num] % 2 == 1:
            maria_wins += 1

    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
