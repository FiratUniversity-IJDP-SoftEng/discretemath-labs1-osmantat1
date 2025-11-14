"""
Exercise 6: Find all pseudoprimes to the base 2. That is, find composite integers n 
such that 2^(n-1) ≡ 1 (mod n), where n does not exceed 10000.

A pseudoprime to base 2 is a composite number n that satisfies Fermat's Little Theorem
for base 2, even though it's not prime.
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


def fast_modular_exponentiation(base, exponent, modulus):
    """
    Compute (base^exponent) mod modulus efficiently using binary exponentiation.
    
    Args:
        base (int): Base number
        exponent (int): Exponent
        modulus (int): Modulus
        
    Returns:
        int: Result of (base^exponent) mod modulus
    """
    result = 1
    base = base % modulus
    
    while exponent > 0:
        # If exponent is odd, multiply base with result
        if exponent % 2 == 1:
            result = (result * base) % modulus
        
        # exponent must be even now
        exponent = exponent >> 1  # exponent = exponent / 2
        base = (base * base) % modulus
    
    return result


def is_pseudoprime_base2(n):
    """
    Check if n is a pseudoprime to base 2.
    
    A number n is a pseudoprime to base 2 if:
    1. n is composite (not prime)
    2. 2^(n-1) ≡ 1 (mod n)
    
    Args:
        n (int): Number to test
        
    Returns:
        bool: True if n is a pseudoprime to base 2, False otherwise
    """
    # Must be composite
    if is_prime(n):
        return False
    
    # Must be odd (even composites can't be pseudoprimes to base 2)
    if n % 2 == 0:
        return False
    
    # Check if 2^(n-1) ≡ 1 (mod n)
    return fast_modular_exponentiation(2, n - 1, n) == 1


def find_pseudoprimes_base2(max_n):
    """
    Find all pseudoprimes to base 2 up to max_n.
    
    Args:
        max_n (int): Maximum value to check
        
    Returns:
        list: List of all pseudoprimes to base 2 ≤ max_n
    """
    pseudoprimes = []
    
    # Start from 9 (smallest odd composite > 2)
    for n in range(9, max_n + 1, 2):  # Check only odd numbers
        if is_pseudoprime_base2(n):
            pseudoprimes.append(n)
    
    return pseudoprimes


def factorize(n):
    """
    Find prime factorization of n.
    
    Args:
        n (int): Number to factorize
        
    Returns:
        list: List of prime factors
    """
    factors = []
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    
    if n > 1:
        factors.append(n)
    
    return factors


def main():
    """Find all pseudoprimes to base 2 up to 10000."""
    print("Exercise 6: Finding pseudoprimes to base 2")
    print("=" * 50)
    print("Looking for composite numbers n where 2^(n-1) ≡ 1 (mod n)")
    print("Range: n ≤ 10000")
    print()
    
    max_value = 10000
    
    print(f"Searching for pseudoprimes up to {max_value}...")
    pseudoprimes = find_pseudoprimes_base2(max_value)
    
    print(f"\nFound {len(pseudoprimes)} pseudoprimes to base 2:")
    print("=" * 50)
    
    # Display results with factorizations
    for i, n in enumerate(pseudoprimes, 1):
        factors = factorize(n)
        factor_str = ' × '.join(map(str, factors))
        
        # Verify the pseudoprime property
        verification = fast_modular_exponentiation(2, n - 1, n)
        
        print(f"{i:2d}. n = {n:4d} = {factor_str} (2^{n-1} mod {n} = {verification})")
    
    # Some analysis
    print(f"\nAnalysis:")
    print("=" * 30)
    print(f"Total pseudoprimes found: {len(pseudoprimes)}")
    
    if pseudoprimes:
        print(f"Smallest pseudoprime: {min(pseudoprimes)}")
        print(f"Largest pseudoprime: {max(pseudoprimes)}")
        
        # Show some statistics about the factorizations
        print(f"\nFactorization patterns:")
        factor_counts = {}
        
        for n in pseudoprimes:
            factors = factorize(n)
            num_distinct = len(set(factors))
            
            if num_distinct not in factor_counts:
                factor_counts[num_distinct] = 0
            factor_counts[num_distinct] += 1
        
        for num_factors in sorted(factor_counts.keys()):
            count = factor_counts[num_factors]
            print(f"  {count} pseudoprimes have {num_factors} distinct prime factor(s)")
    
    # Verify a few examples manually
    print(f"\nVerification examples:")
    print("=" * 30)
    
    examples = pseudoprimes[:3] if len(pseudoprimes) >= 3 else pseudoprimes
    
    for n in examples:
        factors = factorize(n)
        power_mod = fast_modular_exponentiation(2, n - 1, n)
        
        print(f"\nn = {n} = {' × '.join(map(str, factors))}")
        print(f"Is prime? {is_prime(n)}")
        print(f"2^{n-1} mod {n} = {power_mod}")
        print(f"Satisfies 2^(n-1) ≡ 1 (mod n)? {power_mod == 1}")
        print(f"Therefore, {n} is {'a pseudoprime' if power_mod == 1 and not is_prime(n) else 'not a pseudoprime'}")
    
    # Historical note
    print(f"\nNote: The smallest pseudoprime to base 2 is 341 = 11 × 31.")
    print(f"Found 341 in our list: {341 in pseudoprimes}")


if __name__ == "__main__":
    main()