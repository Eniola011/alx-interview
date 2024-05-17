#!/usr/bin/python3
"""

PrimeGame

"""

def primes_sieve(limit):
    """
    Sieve of Eratosthenes algorithm to find all primes up to limit.
    """
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes

def isWinner(x, nums):
    """
    Determines the winner of the game after x rounds.
    :param x: Number of rounds.
    :param nums: List of n values for each round.
    :return: Name of the player who won the most rounds, or None if there's a tie.
    """
    def can_win(n):
        """
        Determines if a player can win a game with the given n.
        :param n: Maximum number in the set of consecutive integers.
        :return: Name of the winning player.
        """
        primes = primes_sieve(n)
        total_primes = len(primes)
        if total_primes % 2 == 0:
            return "Ben"
        else:
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
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
