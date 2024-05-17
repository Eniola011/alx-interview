#!/usr/bin/python3
"""

PrimeGame

"""


def primes_sieve(limit):
    # Sieve of Eratosthenes algorithm to find all primes up to limit
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    for num in range(int(limit**0.5) + 1, limit + 1):
        if sieve[num]:
            primes.append(num)
    return primes

def isWinner(x, nums):
    # Function to determine the winner of the game
    def can_win(n):
        # Function to determine if a player can win a game with given n
        primes = primes_sieve(n)
        total_primes = len(primes)
        if total_primes % 2 == 0:
            # If the total number of primes is even, Ben wins
            return "Ben"
        else:
            # If the total number of primes is odd, Maria wins
            return "Maria"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = can_win(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
