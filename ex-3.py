"""
Exercise 3: Use a loop and the function above to determine whether 2^p - 1 is prime 
for each prime number p not exceeding 100.

These are called Mersenne primes - primes of the form 2^p - 1 where p is also prime.
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
    
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    return [i for i in range(2, n + 1) if prime[i]]


def check_mersenne_primes(max_p):
    """
    Check if 2^p - 1 is prime for each prime p <= max_p.
    
    Args:
        max_p (int): Maximum value of p to check
        
    Returns:
        list: List of tuples (p, mersenne_number, is_prime)
    """
    primes = sieve_of_eratosthenes(max_p)
    results = []
    
    for p in primes:
        mersenne_number = (2 ** p) - 1
        is_mersenne_prime = is_prime(mersenne_number)
        results.append((p, mersenne_number, is_mersenne_prime))
    
    return results


def main():
    """Test Mersenne primes for p <= 100."""
    print("Checking Mersenne primes: 2^p - 1 for prime p <= 100")
    print("=" * 60)
    
    # Check for primes up to 100
    results = check_mersenne_primes(100)
    
    mersenne_primes = []
    
    print("Results:")
    for p, mersenne_num, is_prime_result in results:
        status = "PRIME" if is_prime_result else "composite"
        
        # For large numbers, show scientific notation
        if mersenne_num > 10**15:
            print(f"p = {p:2d}: 2^{p} - 1 = {mersenne_num:.3e} is {status}")
        else:
            print(f"p = {p:2d}: 2^{p} - 1 = {mersenne_num:>15} is {status}")
        
        if is_prime_result:
            mersenne_primes.append((p, mersenne_num))
    
    print(f"\nMersenne primes found (p <= 100):")
    print("=" * 40)
    for p, mersenne_num in mersenne_primes:
        if mersenne_num <= 10**15:
            print(f"M_{p} = 2^{p} - 1 = {mersenne_num}")
        else:
            print(f"M_{p} = 2^{p} - 1 = {mersenne_num:.3e}")
    
    print(f"\nTotal Mersenne primes found: {len(mersenne_primes)}")
    
    # Show the known Mersenne prime exponents for verification
    known_mersenne_exponents = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 97]  # up to 100
    found_exponents = [p for p, _ in mersenne_primes]
    
    print(f"\nKnown Mersenne prime exponents <= 100: {known_mersenne_exponents}")
    print(f"Found Mersenne prime exponents <= 100: {found_exponents}")
    print(f"Results match: {set(known_mersenne_exponents) == set(found_exponents)}")


if __name__ == "__main__":
    main()