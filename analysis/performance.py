"""
Performance Measurement Utilities

This module provides functions for measuring execution time, memory usage,
and other performance metrics of algorithms.
"""

import time
import tracemalloc
import random
import statistics
import pandas as pd
from algorithms.sorting import bubble_sort, insertion_sort, merge_sort, quick_sort
from algorithms.fibonacci import fib_recursive, fib_iterative, fib_dp


def measure_performance(func, *args, num_runs=3, **kwargs):
    """
    Runs func num_runs times, returns (result, median_time, median_memory).
    
    Using median reduces measurement noise from system effects.
    """
    # Optimize run count for large datasets on O(n^2) algorithms to speed up benchmarking
    if args and isinstance(args[0], list) and len(args[0]) >= 5000 and func.__name__ in ('bubble_sort', 'insertion_sort'):
        actual_runs = 1
    else:
        actual_runs = num_runs

    times = []
    memories = []
    result = None
    for _ in range(actual_runs):
        tracemalloc.start()
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        times.append(elapsed)
        memories.append(peak)
    return result, statistics.median(times), statistics.median(memories)


def generate_datasets(size, seed=2026):
    """
    Generate sorted, reverse-sorted, and random datasets of a given size.

    Args:
        size (int): Number of elements in each dataset
        seed (int): Random seed for reproducibility

    Returns:
        dict: Dictionary with keys 'sorted', 'reverse', 'random'
    """
    random.seed(seed)
    random_data = [random.randint(1, 500000) for _ in range(size)]
    sorted_data = sorted(random_data)
    reverse_data = sorted(random_data, reverse=True)
    return {
        "sorted": sorted_data,
        "reverse": reverse_data,
        "random": random_data,
    }


def measure_sorting_performance(sizes=[80, 200, 500, 1200, 3000, 6000, 10000]):
    """
    Measure performance of all sorting algorithms across different input sizes.

    Args:
        sizes (list): List of input sizes to test

    Returns:
        pandas.DataFrame: Results with columns:
            - Algorithm: Name of the sorting algorithm
            - Input Size: Number of elements
            - Input Type: sorted, reverse, or random
            - Comparisons: Number of comparisons made
            - Execution Time (s): Time in seconds
            - Memory Usage (bytes): Peak memory usage in bytes
            - Memory Usage (KB): Peak memory usage in kilobytes
    """
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
    }

    results = []

    for size in sizes:
        print(f"Testing input size: {size}")
        datasets = generate_datasets(size)

        for condition, data in datasets.items():
            for name, algo in algorithms.items():
                (sorted_arr, comparisons), t, mem = measure_performance(algo, data)
                results.append({
                    "Algorithm": name,
                    "Input Size": size,
                    "Input Type": condition,
                    "Comparisons": comparisons,
                    "Execution Time (s)": t,
                    "Memory Usage (bytes)": mem,
                    "Memory Usage (KB)": mem / 1024,
                })

    return pd.DataFrame(results)


def measure_fibonacci_performance(n_values=[8, 14, 20, 26, 32, 36, 40]):
    """
    Measure performance of all Fibonacci algorithms for different values of n.

    Args:
        n_values (list): List of n values to test

    Returns:
        pandas.DataFrame: Results with columns:
            - Algorithm: Name of the Fibonacci algorithm
            - n: Input value
            - Result: Fibonacci number computed
            - Execution Time (s): Time in seconds
            - Memory Usage (bytes): Peak memory usage in bytes
            - Memory Usage (KB): Peak memory usage in kilobytes
    """
    algorithms = {
        "Recursive": fib_recursive,
        "Iterative": fib_iterative,
        "Dynamic Programming": fib_dp,
    }

    results = []

    for n in n_values:
        print(f"Testing n = {n}")
        for name, algo in algorithms.items():
            try:
                result, t, mem = measure_performance(algo, n)
                results.append({
                    "Algorithm": name,
                    "n": n,
                    "Result": result,
                    "Execution Time (s)": t,
                    "Memory Usage (bytes)": mem,
                    "Memory Usage (KB)": mem / 1024,
                })
            except RecursionError:
                print(f"  {name}: RecursionError for n={n}")
                results.append({
                    "Algorithm": name,
                    "n": n,
                    "Result": None,
                    "Execution Time (s)": None,
                    "Memory Usage (bytes)": None,
                    "Memory Usage (KB)": None,
                })

    return pd.DataFrame(results)


if __name__ == "__main__":
    # Test performance measurement
    print("=" * 60)
    print("Sorting Algorithm Performance Analysis")
    print("=" * 60)
    sorting_df = measure_sorting_performance([100, 500, 1000])
    print("\nResults:")
    print(sorting_df.to_string(index=False))

    print("\n" + "=" * 60)
    print("Fibonacci Algorithm Performance Analysis")
    print("=" * 60)
    fib_df = measure_fibonacci_performance([10, 20, 30, 35])
    print("\nResults:")
    print(fib_df.to_string(index=False))
