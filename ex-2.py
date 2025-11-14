"""
Exercise 2: Write a function that lists all prime numbers less than or equal to a given positive integer.

This uses the Sieve of Eratosthenes algorithm for efficient prime generation.
"""

def is_prime(n):
    """
    Determines if a positive integer is prime.
    
    Args:
        n (int): A positive integer to check for primality
        
    Returns:
        bool: True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def sieve_of_eratosthenes(n):
    """
    Generate all prime numbers less than or equal to n using Sieve of Eratosthenes.
    
    Args:
        n (int): Upper bound for prime generation
        
    Returns:
        list: List of all prime numbers <= n
    """
    if n < 2:
        return []
    
    # Create a boolean array "prime[0..n]" and set all entries as true
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    # Collect all prime numbers
    return [i for i in range(2, n + 1) if prime[i]]


def list_primes_up_to(n):
    """
    Lists all prime numbers less than or equal to n.
    
    Args:
        n (int): Upper bound for prime listing
        
    Returns:
        list: List of all prime numbers <= n
    """
    return sieve_of_eratosthenes(n)


def main():
    """Test the prime listing functions."""
    test_values = [10, 20, 50, 100]
    
    print("Testing prime listing functions:")
    print("=" * 40)
    
    for n in test_values:
        primes = list_primes_up_to(n)
        print(f"\nPrimes <= {n}: {primes}")
        print(f"Count: {len(primes)}")
    
    # Compare with simple method for small numbers
    n = 30
    primes_sieve = sieve_of_eratosthenes(n)
    primes_simple = [i for i in range(2, n + 1) if is_prime(i)]
    
    print(f"\nComparison for n = {n}:")
    print(f"Sieve method: {primes_sieve}")
    print(f"Simple method: {primes_simple}")
    print(f"Results match: {primes_sieve == primes_simple}")


if __name__ == "__main__":
    main()