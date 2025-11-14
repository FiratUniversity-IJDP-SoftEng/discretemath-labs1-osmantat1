"""
Exercise 5: Find 10 different prime numbers, each with 100 digits.

This task requires generating large random numbers and testing them for primality.
We'll use the Miller-Rabin primality test for efficiency with large numbers.
"""

import random
import time


def miller_rabin_test(n, k=10):
    """
    Miller-Rabin primality test for large numbers.
    
    Args:
        n (int): Number to test for primality
        k (int): Number of rounds of testing (higher k = more accurate)
        
    Returns:
        bool: True if n is probably prime, False if n is definitely composite
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as d * 2^r
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Witness loop
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)  # a^d mod n
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True


def is_prime_large(n):
    """
    Test if a large number is prime using Miller-Rabin test.
    
    Args:
        n (int): Number to test
        
    Returns:
        bool: True if probably prime, False if composite
    """
    return miller_rabin_test(n, k=20)  # 20 rounds for high confidence


def generate_random_odd_number(digits):
    """
    Generate a random odd number with exactly the specified number of digits.
    
    Args:
        digits (int): Number of digits in the generated number
        
    Returns:
        int: Random odd number with specified digits
    """
    if digits <= 0:
        raise ValueError("Number of digits must be positive")
    
    # Ensure the number has exactly 'digits' digits
    min_val = 10**(digits - 1)
    max_val = 10**digits - 1
    
    # Generate random number in range
    num = random.randint(min_val, max_val)
    
    # Make it odd
    if num % 2 == 0:
        num += 1
        # Ensure it still has the right number of digits
        if num > max_val:
            num = max_val if max_val % 2 == 1 else max_val - 1
    
    return num


def find_large_primes(digit_count, count=10):
    """
    Find prime numbers with exactly the specified number of digits.
    
    Args:
        digit_count (int): Number of digits in each prime
        count (int): Number of primes to find
        
    Returns:
        list: List of prime numbers with specified digit count
    """
    primes = []
    attempts = 0
    max_attempts = count * 1000  # Reasonable limit
    
    print(f"Searching for {count} prime numbers with {digit_count} digits...")
    print("This may take a while for large numbers.")
    
    start_time = time.time()
    
    while len(primes) < count and attempts < max_attempts:
        attempts += 1
        candidate = generate_random_odd_number(digit_count)
        
        if is_prime_large(candidate):
            primes.append(candidate)
            elapsed = time.time() - start_time
            print(f"Found prime #{len(primes)}: {str(candidate)[:20]}...{str(candidate)[-20:]} ({elapsed:.1f}s)")
    
    if len(primes) < count:
        print(f"Warning: Only found {len(primes)} primes after {attempts} attempts")
    
    return primes


def verify_prime_properties(primes, expected_digits):
    """
    Verify that found numbers are actually prime and have correct digit count.
    
    Args:
        primes (list): List of numbers to verify
        expected_digits (int): Expected number of digits
        
    Returns:
        bool: True if all numbers pass verification
    """
    print(f"\nVerifying {len(primes)} numbers...")
    
    all_valid = True
    for i, prime in enumerate(primes, 1):
        # Check digit count
        actual_digits = len(str(prime))
        digit_ok = actual_digits == expected_digits
        
        # Re-test primality with higher confidence
        prime_ok = miller_rabin_test(prime, k=50)
        
        status = "✓" if (digit_ok and prime_ok) else "✗"
        
        print(f"{status} Prime {i}: {actual_digits} digits, prime: {prime_ok}")
        
        if not (digit_ok and prime_ok):
            all_valid = False
    
    return all_valid


def main():
    """Find and verify 10 different 100-digit prime numbers."""
    print("Exercise 5: Finding 10 different prime numbers with 100 digits")
    print("=" * 60)
    
    # Set random seed for reproducible results (optional)
    # random.seed(42)
    
    target_digits = 100
    target_count = 10
    
    # Find the primes
    large_primes = find_large_primes(target_digits, target_count)
    
    if len(large_primes) == target_count:
        print(f"\nSuccessfully found {target_count} primes with {target_digits} digits!")
    else:
        print(f"\nFound {len(large_primes)} primes (target was {target_count})")
    
    # Display the primes
    print(f"\n{target_digits}-digit prime numbers:")
    print("=" * 60)
    
    for i, prime in enumerate(large_primes, 1):
        prime_str = str(prime)
        # Display first 20 and last 20 digits for readability
        if len(prime_str) > 50:
            display = f"{prime_str[:20]}...{prime_str[-20:]}"
        else:
            display = prime_str
        
        print(f"{i:2d}. {display} ({len(prime_str)} digits)")
    
    # Verify the results
    if large_primes:
        all_valid = verify_prime_properties(large_primes, target_digits)
        
        print(f"\nVerification: {'All primes are valid!' if all_valid else 'Some issues found!'}")
        
        # Additional statistics
        print(f"\nStatistics:")
        print(f"Target digit count: {target_digits}")
        print(f"Primes found: {len(large_primes)}")
        print(f"All unique: {len(set(large_primes)) == len(large_primes)}")
        
        if large_primes:
            # Show the actual full numbers (for smaller sets)
            print(f"\nComplete prime numbers:")
            for i, prime in enumerate(large_primes, 1):
                print(f"Prime {i}:")
                print(f"{prime}")
                print()


if __name__ == "__main__":
    main()