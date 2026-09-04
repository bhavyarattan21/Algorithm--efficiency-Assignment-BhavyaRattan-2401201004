"""
Sorting Algorithm Implementations

This module provides four classic sorting algorithms:
- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort

Each algorithm includes:
- Description and documentation
- Input/output specifications
- Complexity analysis (best, average, worst case, space)
- Advantages and limitations
- Suitable application scenarios
"""

import random


def bubble_sort(arr):
    """
    Sorts a list in ascending order using Bubble Sort.

    Algorithm Description:
    Repeatedly steps through the list, compares adjacent elements and swaps
    them if they are in the wrong order. The largest unsorted element
    'bubbles up' to its correct position on each pass.

    Args:
        arr: List of comparable elements

    Returns:
        (sorted_list, comparisons) - New sorted list and comparison count

    Time Complexity:
        - Best Case: O(n) - already sorted (with early exit optimization)
        - Average Case: O(n²)
        - Worst Case: O(n²) - reverse sorted

    Space Complexity: O(1) - in-place sorting

    Advantages:
        - Simple to understand and implement
        - Stable sorting algorithm
        - Adaptive - performs well on nearly sorted data

    Limitations:
        - Very slow for large datasets
        - O(n²) in average and worst cases

    Application Scenarios:
        - Educational purposes
        - Small datasets
        - Nearly sorted data
    """
    a = arr.copy()
    n = len(a)
    comparisons = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:  # already sorted -> stop early
            break
    return a, comparisons


def insertion_sort(arr):
    """
    Sorts a list in ascending order using Insertion Sort.

    Algorithm Description:
    Builds the sorted list one element at a time by taking each element
    and inserting it into its correct position among the already-sorted
    elements to its left.

    Args:
        arr: List of comparable elements

    Returns:
        (sorted_list, comparisons) - New sorted list and comparison count

    Time Complexity:
        - Best Case: O(n) - already sorted
        - Average Case: O(n²)
        - Worst Case: O(n²) - reverse sorted

    Space Complexity: O(1) - in-place sorting

    Advantages:
        - Simple implementation
        - Stable sorting algorithm
        - Adaptive - efficient for nearly sorted data
        - In-place sorting (minimal extra memory)
        - Online algorithm - can sort as elements are received

    Limitations:
        - O(n²) for large datasets
        - Not efficient for general-purpose sorting

    Application Scenarios:
        - Small datasets
        - Nearly sorted data
        - Online sorting (data arriving one element at a time)
    """
    a = arr.copy()
    comparisons = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = key
    return a, comparisons


def _merge(left, right, comps):
    """Helper function for merge sort - merges two sorted lists."""
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        comps[0] += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def _merge_sort_helper(a, comps):
    """Helper function for merge sort with comparison counting."""
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = _merge_sort_helper(a[:mid], comps)
    right = _merge_sort_helper(a[mid:], comps)
    return _merge(left, right, comps)


def merge_sort(arr):
    """
    Sorts a list in ascending order using Merge Sort (Divide and Conquer).

    Algorithm Description:
    Recursively splits the list into two halves, sorts each half,
    and merges the two sorted halves into a single sorted list.

    Args:
        arr: List of comparable elements

    Returns:
        (sorted_list, comparisons) - New sorted list and comparison count

    Time Complexity:
        - Best Case: O(n log n)
        - Average Case: O(n log n)
        - Worst Case: O(n log n)

    Space Complexity: O(n) - requires temporary arrays

    Advantages:
        - Guaranteed O(n log n) performance
        - Stable sorting algorithm
        - Predictable performance regardless of input

    Limitations:
        - Requires O(n) additional space
        - Slightly slower than Quick Sort in practice due to memory allocation

    Application Scenarios:
        - Large datasets where consistent performance is critical
        - External sorting (sorting data that doesn't fit in memory)
        - When stability is required
    """
    a = arr.copy()
    comps = [0]
    result = _merge_sort_helper(a, comps)
    return result, comps[0]


def _partition(a, low, high, comps):
    """Helper function for quick sort - partitions array around pivot."""
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        comps[0] += 1
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def _randomized_partition(a, low, high, comps):
    """Randomized partition to avoid worst-case on sorted input."""
    rand_idx = random.randint(low, high)
    a[rand_idx], a[high] = a[high], a[rand_idx]
    return _partition(a, low, high, comps)


def _quick_sort(a, low, high, comps):
    """Helper function for quick sort - recursive implementation."""
    if low < high:
        p = _randomized_partition(a, low, high, comps)
        _quick_sort(a, low, p - 1, comps)
        _quick_sort(a, p + 1, high, comps)


def quick_sort(arr):
    """
    Sorts a list in ascending order using Quick Sort (Divide and Conquer).

    Algorithm Description:
    Selects a pivot element and partitions the list so elements smaller
    than the pivot go left and larger elements go right, then recursively
    sorts each partition.

    Args:
        arr: List of comparable elements

    Returns:
        (sorted_list, comparisons) - New sorted list and comparison count

    Time Complexity:
        - Best Case: O(n log n) - good pivot choices
        - Average Case: O(n log n)
        - Worst Case: O(n²) - poor pivot choices (already sorted data)

    Space Complexity: O(log n) - recursion stack space

    Advantages:
        - Fast in practice (cache-friendly)
        - In-place sorting (minimal extra memory)
        - Average case O(n log n)

    Limitations:
        - Unstable sorting algorithm
        - Worst case O(n²) with poor pivot selection
        - Recursive implementation may cause stack overflow for very large arrays

    Application Scenarios:
        - General-purpose sorting
        - Large datasets where average-case performance matters
        - When memory is a concern
    """
    a = arr.copy()
    comps = [0]
    _quick_sort(a, 0, len(a) - 1, comps)
    return a, comps[0]


if __name__ == "__main__":
    # Test all sorting algorithms
    sample = [64, 34, 25, 12, 22, 11, 90]

    print("Original:", sample)
    for name, algo in [("Bubble Sort", bubble_sort), ("Insertion Sort", insertion_sort),
                       ("Merge Sort", merge_sort), ("Quick Sort", quick_sort)]:
        result, comps = algo(sample)
        print(f"{name}: {result}, Comparisons: {comps}")
