#!/usr/bin/python3

""" Prime Game """


def is_prime(n):
    """
    Check if a number is a prime number.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def play_round(n):
    """
    Simulate a round of the game and determine the winner.
    """
    primes = [i for i in range(1, n + 1) if is_prime(i)]
    turn = 0  # Maria's turn if 0, Ben's turn if 1

    while primes:
        if len(primes) % 2 == 1:
            return "Maria" if turn == 0 else "Ben"
        first_prime = primes[0]
        primes = [p for p in primes if p % first_prime != 0]
        turn = 1 - turn  # Switch turn

    return "Ben" if turn == 0 else "Maria"


def isWinner(x, nums):
    """
    Determine the winner after x rounds.
    """
    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        winner = play_round(n)
        wins[winner] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    else:
        return None
