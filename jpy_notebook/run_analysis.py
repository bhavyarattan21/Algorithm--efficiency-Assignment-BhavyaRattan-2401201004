#!/usr/bin/env python3
"""
DAA Lab 1: Algorithm Efficiency Analysis

This script runs the complete performance analysis for sorting and
Fibonacci algorithms, generating visualizations and tables.

Usage:
    python notebook/run_analysis.py
"""

import sys
import os

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.sorting import bubble_sort, insertion_sort, merge_sort, quick_sort
from algorithms.fibonacci import fib_recursive, fib_iterative, fib_dp
from analysis.performance import (
    measure_sorting_performance,
    measure_fibonacci_performance,
)
from analysis.visualizations import generate_all_plots
import pandas as pd


def print_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n")


def print_algorithm_info():
    """Print information about all implemented algorithms."""
    print_header("ALGORITHM INFORMATION")

    print("SORTING ALGORITHMS")
    print("-" * 40)
    print("""
1. Bubble Sort
   - Description: Repeatedly steps through list, compares adjacent elements
   - Time: O(n²) average/worst, O(n) best
   - Space: O(1)
   - Stable: Yes

2. Insertion Sort
   - Description: Builds sorted list one element at a time
   - Time: O(n²) average/worst, O(n) best
   - Space: O(1)
   - Stable: Yes

3. Merge Sort
   - Description: Divide and conquer - splits, sorts, merges
   - Time: O(n log n) all cases
   - Space: O(n)
   - Stable: Yes

4. Quick Sort
   - Description: Divide and conquer - partition around pivot
   - Time: O(n log n) average/best, O(n²) worst
   - Space: O(log n)
   - Stable: No
    """)

    print("FIBONACCI ALGORITHMS")
    print("-" * 40)
    print("""
1. Recursive
   - Description: Direct recurrence F(n) = F(n-1) + F(n-2)
   - Time: O(2ⁿ)
   - Space: O(n)

2. Iterative
   - Description: Bottom-up loop with two variables
   - Time: O(n)
   - Space: O(1)

3. Dynamic Programming (Memoization)
   - Description: Top-down with cache
   - Time: O(n)
   - Space: O(n)
    """)


def run_sorting_analysis():
    """Run sorting algorithm performance analysis."""
    print_header("SORTING ALGORITHM PERFORMANCE ANALYSIS")
    print("Testing input sizes: 80, 200, 500, 1200, 3000, 6000, 10000")
    print("Input types: sorted, reverse-sorted, random\n")

    df = measure_sorting_performance([80, 200, 500, 1200, 3000, 6000, 10000])

    # Display results
    print("\nResults Summary:")
    print("-" * 70)
    pivot_time = df.pivot_table(
        values="Execution Time (s)",
        index=["Algorithm", "Input Type"],
        columns="Input Size",
    )
    print(pivot_time.to_string())

    # Save to CSV
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/sorting_performance.csv", index=False)
    print("\nData saved to: data/sorting_performance.csv")

    return df


def run_fibonacci_analysis():
    """Run Fibonacci algorithm performance analysis."""
    print_header("FIBONACCI ALGORITHM PERFORMANCE ANALYSIS")
    print("Testing n values: 8, 14, 20, 26, 32, 36, 40\n")

    df = measure_fibonacci_performance([8, 14, 20, 26, 32, 36, 40])

    # Display results
    print("\nResults Summary:")
    print("-" * 70)
    print(df.to_string(index=False))

    # Save to CSV
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/fibonacci_performance.csv", index=False)
    print("\nData saved to: data/fibonacci_performance.csv")

    return df


def generate_visualizations(sorting_df, fibonacci_df):
    """Generate all performance visualizations."""
    print_header("GENERATING VISUALIZATIONS")
    generate_all_plots(sorting_df, fibonacci_df)


def print_conclusion():
    """Print conclusion and key findings."""
    print_header("CONCLUSION AND KEY FINDINGS")

    print("""
KEY FINDINGS:

1. SORTING ALGORITHMS:
   - Bubble Sort and Insertion Sort show O(n²) behavior - suitable only for small datasets
   - Merge Sort and Quick Sort show O(n log n) behavior - scalable for large datasets
   - Quick Sort has best average performance but worst-case O(n²)
   - Merge Sort provides consistent performance across all input types

2. FIBONACCI ALGORITHMS:
   - Recursive approach is impractical for n > 40 (exponential time)
   - Iterative approach is optimal: O(n) time, O(1) space
   - Dynamic Programming matches iterative time but uses O(n) space for memoization

3. RECOMMENDATIONS:
   - For small datasets (< 1000 elements): Any algorithm works
   - For large datasets: Use Merge Sort or Quick Sort
   - For Fibonacci: Always use Iterative or DP approach
   - For online/streaming data: Use Insertion Sort
    """)


def main():
    """Main function to run complete analysis."""
    print_header("DAA LAB 1: ALGORITHM EFFICIENCY ANALYSIS")
    print("Comparative Study of Algorithm Efficiency and Performance Analysis")
    print("\nThis script will:")
    print("1. Display algorithm information")
    print("2. Run performance experiments")
    print("3. Generate visualizations")
    print("4. Print conclusions")

    # Print algorithm information
    print_algorithm_info()

    # Run analyses
    sorting_df = run_sorting_analysis()
    fibonacci_df = run_fibonacci_analysis()

    # Generate visualizations
    generate_visualizations(sorting_df, fibonacci_df)

    # Print conclusion
    print_conclusion()

    print_header("ANALYSIS COMPLETE")
    print("Check the following directories for outputs:")
    print("  - data/       : CSV files with raw performance data")
    print("  - graphs/     : PNG files with visualizations")
    print("  - reports/    : Report files (algorithm_performance_case_study.md/pdf)")


if __name__ == "__main__":
    main()
