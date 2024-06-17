def isWinner(x, nums):
    if not nums or x <= 0:
        return None
    
    # Find the maximum value in nums to limit the Sieve of Eratosthenes
    max_n = max(nums)
    
    # Step 1: Sieve of Eratosthenes to find all primes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    p = 2
    while (p * p <= max_n):
        if (sieve[p] == True):
            for i in range(p * p, max_n + 1, p):
                sieve[i] = False
        p += 1
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    def play_game(n):
        if n < 2:
            return "Ben"  # Ben wins because Maria can't start the game
        
        # Track which numbers are available
        available = [True] * (n + 1)
        turn = 0  # 0 for Maria, 1 for Ben
        for prime in primes:
            if prime > n:
                break
            if available[prime]:
                # Remove prime and its multiples
                for multiple in range(prime, n + 1, prime):
                    available[multiple] = False
                turn = 1 - turn  # Switch turn
                
        # If turn is 0, it means Maria moved last, hence Ben wins
        return "Ben" if turn == 0 else "Maria"
    
    maria_wins = 0
    ben_wins = 0
    
    # Step 2: Determine the winner for each round
    for num in nums:
        winner = play_game(num)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1
    
    # Step 3: Determine who won the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
