"""
Fibonacci Algorithm Implementations

This module provides three approaches to computing Fibonacci numbers:
- Naive Recursion (exponential time)
- Iterative approach (linear time)
- Dynamic Programming with Memoization (linear time)

Each algorithm includes:
- Description and documentation
- Input/output specifications
- Complexity analysis (time and space)
- Advantages and limitations
- Suitable application scenarios
"""


def fib_recursive(n):
    """
    Returns the n-th Fibonacci number using naive recursion.

    Algorithm Description:
    Directly implements the recurrence F(n) = F(n-1) + F(n-2).
    Simple but recomputes the same subproblems many times.

    Args:
        n (int): Non-negative integer index in Fibonacci sequence

    Returns:
        int: The n-th Fibonacci number

    Time Complexity:
        - O(2^n) - exponential time
        - Each call branches into two recursive calls

    Space Complexity:
        - O(n) - recursion stack depth

    Advantages:
        - Very simple and intuitive implementation
        - Directly mirrors mathematical definition

    Limitations:
        - Extremely slow for large n (e.g., n > 40)
        - Recomputes same subproblems exponentially many times
        - Risk of stack overflow for large n

    Application Scenarios:
        - Educational purposes (understanding recursion)
        - Very small values of n (n < 30)
        - Demonstrating exponential vs linear time complexity
    """
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    """
    Returns the n-th Fibonacci number using an iterative approach.

    Algorithm Description:
    Computes Fibonacci numbers bottom-up using a simple loop and two
    variables, avoiding recomputation entirely.

    Args:
        n (int): Non-negative integer index in Fibonacci sequence

    Returns:
        int: The n-th Fibonacci number

    Time Complexity:
        - O(n) - linear time
        - Single loop from 2 to n

    Space Complexity:
        - O(1) - constant space
        - Only two variables needed

    Advantages:
        - Very efficient - O(n) time, O(1) space
        - No recursion overhead
        - Can handle very large n (up to Python's integer limit)

    Limitations:
        - Slightly more code than recursive version
        - Not as intuitive as recursive definition

    Application Scenarios:
        - Production code where performance matters
        - Large values of n
        - When memory efficiency is important
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fib_dp(n, memo=None):
    """
    Returns the n-th Fibonacci number using memoized (top-down) Dynamic Programming.

    Algorithm Description:
    Stores previously computed Fibonacci values in a cache (dictionary)
    so each subproblem is solved only once - a top-down DP approach.

    Args:
        n (int): Non-negative integer index in Fibonacci sequence
        memo (dict, optional): Cache for memoization. Defaults to None.

    Returns:
        int: The n-th Fibonacci number

    Time Complexity:
        - O(n) - linear time
        - Each subproblem computed exactly once

    Space Complexity:
        - O(n) - for memoization cache and recursion stack

    Advantages:
        - Same O(n) time as iterative approach
        - Maintains recursive structure (closer to mathematical definition)
        - Cache can be reused for multiple queries

    Limitations:
        - Uses O(n) space for memoization
        - Recursion overhead (though mitigated by memoization)
        - Slightly slower than iterative due to dictionary lookups

    Application Scenarios:
        - When you need to compute multiple Fibonacci numbers
        - Educational purposes (understanding DP)
        - When recursive structure is preferred
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_dp(n - 1, memo) + fib_dp(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    # Test all Fibonacci algorithms
    print("Fibonacci sequence (first 10 numbers):")
    for n in range(10):
        print(f"n={n}: recursive={fib_recursive(n)}, "
              f"iterative={fib_iterative(n)}, "
              f"dp={fib_dp(n)}")

    # Performance comparison for larger n
    import time

    n = 35
    print(f"\nPerformance comparison for n={n}:")

    start = time.time()
    fib_recursive(n)
    print(f"Recursive: {time.time() - start:.6f}s")

    start = time.time()
    fib_iterative(n)
    print(f"Iterative: {time.time() - start:.6f}s")

    start = time.time()
    fib_dp(n)
    print(f"DP: {time.time() - start:.6f}s")
