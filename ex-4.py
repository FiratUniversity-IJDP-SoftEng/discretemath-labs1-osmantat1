"""
Exercise 4: Show (test with code) that n² + n + 41 is prime for all integers n 
with 0 ≤ n ≤ 39. But also show that it is not prime when n = 40.

This is testing Euler's prime-generating polynomial.
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


def euler_polynomial(n):
    """
    Evaluate Euler's polynomial: n² + n + 41
    
    Args:
        n (int): Input value
        
    Returns:
        int: Value of n² + n + 41
    """
    return n * n + n + 41


def test_euler_polynomial(start_n, end_n):
    """
    Test Euler's polynomial for primality over a range of n values.
    
    Args:
        start_n (int): Starting value of n
        end_n (int): Ending value of n (inclusive)
        
    Returns:
        list: List of tuples (n, polynomial_value, is_prime, factors_if_composite)
    """
    results = []
    
    for n in range(start_n, end_n + 1):
        value = euler_polynomial(n)
        is_prime_result = is_prime(value)
        
        factors = None
        if not is_prime_result and value > 1:
            # Find factors for composite numbers
            factors = []
            temp = value
            d = 2
            while d * d <= temp:
                while temp % d == 0:
                    factors.append(d)
                    temp //= d
                d += 1
            if temp > 1:
                factors.append(temp)
        
        results.append((n, value, is_prime_result, factors))
    
    return results


def main():
    """Test Euler's polynomial n² + n + 41."""
    print("Testing Euler's polynomial: f(n) = n² + n + 41")
    print("=" * 50)
    
    # Test for n = 0 to 39 (should all be prime)
    print("Testing for n = 0 to 39 (expecting all primes):")
    print("-" * 50)
    
    results_0_to_39 = test_euler_polynomial(0, 39)
    all_prime = True
    
    for n, value, is_prime_result, factors in results_0_to_39:
        status = "PRIME" if is_prime_result else "COMPOSITE"
        print(f"n = {n:2d}: f({n:2d}) = {n:2d}² + {n:2d} + 41 = {value:4d} is {status}")
        
        if not is_prime_result:
            all_prime = False
            if factors:
                print(f"         Factors: {' × '.join(map(str, factors))}")
    
    print(f"\nAll values prime for n ∈ [0, 39]: {all_prime}")
    
    # Test for n = 40 (should not be prime)
    print("\nTesting for n = 40 (expecting composite):")
    print("-" * 50)
    
    results_40 = test_euler_polynomial(40, 40)
    n, value, is_prime_result, factors = results_40[0]
    
    status = "PRIME" if is_prime_result else "COMPOSITE"
    print(f"n = {n:2d}: f({n:2d}) = {n:2d}² + {n:2d} + 41 = {value:4d} is {status}")
    
    if factors:
        print(f"         Factors: {' × '.join(map(str, factors))}")
        print(f"         Verification: {' × '.join(map(str, factors))} = {eval('*'.join(map(str, factors)))}")
    
    # Test a few more values to see the pattern break
    print("\nTesting for n = 41 to 45 (checking pattern continuation):")
    print("-" * 50)
    
    results_41_to_45 = test_euler_polynomial(41, 45)
    
    for n, value, is_prime_result, factors in results_41_to_45:
        status = "PRIME" if is_prime_result else "COMPOSITE"
        print(f"n = {n:2d}: f({n:2d}) = {n:2d}² + {n:2d} + 41 = {value:4d} is {status}")
        
        if factors:
            print(f"         Factors: {' × '.join(map(str, factors))}")
    
    # Summary statistics
    all_results = results_0_to_39 + results_40 + results_41_to_45
    prime_count = sum(1 for _, _, is_prime_result, _ in all_results if is_prime_result)
    total_count = len(all_results)
    
    print(f"\nSummary for n ∈ [0, 45]:")
    print(f"Total values tested: {total_count}")
    print(f"Prime values: {prime_count}")
    print(f"Composite values: {total_count - prime_count}")
    print(f"Prime percentage: {prime_count / total_count * 100:.1f}%")
    
    # Show why n=40 gives a composite number
    print(f"\nWhy f(40) is composite:")
    print(f"f(40) = 40² + 40 + 41 = 1600 + 40 + 41 = 1681")
    print(f"1681 = 41² = 41 × 41")
    print(f"This happens because 40² + 40 + 41 = 40(40 + 1) + 41 = 40 × 41 + 41 = 41(40 + 1) = 41 × 41")


if __name__ == "__main__":
    main()