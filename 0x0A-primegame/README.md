# Prime Game

## Description
- Maria and Ben are playing a game with a set of consecutive integers starting from 1 up to and including `n`.
- They take turns choosing a prime number from the set, removing that number and all its multiples from the set.
- The player who cannot make a move loses the game. Maria always goes first.
- This repository contains a function to determine the winner of multiple rounds of this game, assuming both players play optimally.

## Function Prototype

```python
def isWinner(x, nums):
    """
    Determines the winner of multiple rounds of the Prime Game.

    Parameters:
    x (int): The number of rounds to be played.
    nums (list of int): List containing the upper bound `n` for each round.

    Returns:
    str: The name of the player who won the most rounds ("Maria" or "Ben").
         If the winner cannot be determined, returns None.
    """
