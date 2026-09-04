"""
Visualization Utilities for Algorithm Performance Analysis

This module provides functions for creating graphical representations
of algorithm performance metrics using matplotlib.
"""

# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
import pandas as pd
import os


def ensure_output_dir():
    """Ensure output directories exist."""
    os.makedirs("graphs", exist_ok=True)


def save_plot(filename):
    """Save current plot to graphs/ directory."""
    plt.savefig(f"graphs/{filename}", dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: graphs/{filename}")


def plot_sorting_time_comparison(df):
    """
    Plot execution time comparison for sorting algorithms (log scale).
    """
    ensure_output_dir()
    input_types = df["Input Type"].unique()
    colors = {"Bubble Sort": "#c0392b", "Insertion Sort": "#d35400", "Merge Sort": "#27ae60", "Quick Sort": "#2980b9"}
    markers = {"Bubble Sort": "o", "Insertion Sort": "s", "Merge Sort": "^", "Quick Sort": "D"}
    linestyles = {"Bubble Sort": "-", "Insertion Sort": "--", "Merge Sort": "-.", "Quick Sort": ":"}

    fig, axes = plt.subplots(1, 3, figsize=(16, 5.5))
    fig.suptitle("Sorting Algorithm Performance: Execution Time vs Input Size", fontsize=14, fontweight="bold")

    for idx, input_type in enumerate(input_types):
        ax = axes[idx]
        subset = df[df["Input Type"] == input_type]

        for algo in subset["Algorithm"].unique():
            algo_data = subset[subset["Algorithm"] == algo]
            ax.plot(
                algo_data["Input Size"],
                algo_data["Execution Time (s)"],
                marker=markers.get(algo, "o"),
                linestyle=linestyles.get(algo, "-"),
                color=colors.get(algo, None),
                linewidth=2.2,
                markersize=6.5,
                label=algo,
            )

        ax.set_xlabel("Input Size (n)", fontsize=11, fontweight="medium")
        ax.set_ylabel("Execution Time (s) [Log Scale]", fontsize=11, fontweight="medium")
        ax.set_title(f"Input Pattern: {input_type.capitalize()}", fontsize=12, fontweight="bold")
        ax.set_yscale("log")
        ax.legend(frameon=True, facecolor="#ffffff", edgecolor="#cccccc")
        ax.grid(True, which="both", linestyle="--", alpha=0.5)

    plt.tight_layout()
    save_plot("sorting_time_comparison.png")


def plot_sorting_memory_comparison(df):
    """
    Plot memory usage comparison for sorting algorithms (log scale).
    """
    ensure_output_dir()
    input_types = df["Input Type"].unique()
    colors = {"Bubble Sort": "#c0392b", "Insertion Sort": "#d35400", "Merge Sort": "#27ae60", "Quick Sort": "#2980b9"}
    markers = {"Bubble Sort": "o", "Insertion Sort": "s", "Merge Sort": "^", "Quick Sort": "D"}
    linestyles = {"Bubble Sort": "-", "Insertion Sort": "--", "Merge Sort": "-.", "Quick Sort": ":"}

    fig, axes = plt.subplots(1, 3, figsize=(16, 5.5))
    fig.suptitle("Sorting Algorithm Resource Requirements: Peak Memory Usage", fontsize=14, fontweight="bold")

    for idx, input_type in enumerate(input_types):
        ax = axes[idx]
        subset = df[df["Input Type"] == input_type]

        for algo in subset["Algorithm"].unique():
            algo_data = subset[subset["Algorithm"] == algo]
            ax.plot(
                algo_data["Input Size"],
                algo_data["Memory Usage (KB)"],
                marker=markers.get(algo, "s"),
                linestyle=linestyles.get(algo, "-"),
                color=colors.get(algo, None),
                linewidth=2.2,
                markersize=6.5,
                label=algo,
            )

        ax.set_xlabel("Input Size (n)", fontsize=11, fontweight="medium")
        ax.set_ylabel("Peak Memory Allocation (KB)", fontsize=11, fontweight="medium")
        ax.set_title(f"Input Pattern: {input_type.capitalize()}", fontsize=12, fontweight="bold")
        ax.set_yscale("log")
        ax.legend(frameon=True, facecolor="#ffffff", edgecolor="#cccccc")
        ax.grid(True, which="both", linestyle="--", alpha=0.5)

    plt.tight_layout()
    save_plot("sorting_memory_comparison.png")


def plot_sorting_comparisons(df):
    """
    Plot comparison count for sorting algorithms (log scale).
    """
    ensure_output_dir()
    input_types = df["Input Type"].unique()
    colors = {"Bubble Sort": "#c0392b", "Insertion Sort": "#d35400", "Merge Sort": "#27ae60", "Quick Sort": "#2980b9"}
    markers = {"Bubble Sort": "o", "Insertion Sort": "s", "Merge Sort": "^", "Quick Sort": "D"}
    linestyles = {"Bubble Sort": "-", "Insertion Sort": "--", "Merge Sort": "-.", "Quick Sort": ":"}

    fig, axes = plt.subplots(1, 3, figsize=(16, 5.5))
    fig.suptitle("Sorting Algorithm Operation Counts: Key Comparisons", fontsize=14, fontweight="bold")

    for idx, input_type in enumerate(input_types):
        ax = axes[idx]
        subset = df[df["Input Type"] == input_type]

        for algo in subset["Algorithm"].unique():
            algo_data = subset[subset["Algorithm"] == algo]
            ax.plot(
                algo_data["Input Size"],
                algo_data["Comparisons"],
                marker=markers.get(algo, "^"),
                linestyle=linestyles.get(algo, "-"),
                color=colors.get(algo, None),
                linewidth=2.2,
                markersize=6.5,
                label=algo,
            )

        ax.set_xlabel("Input Size (n)", fontsize=11, fontweight="medium")
        ax.set_ylabel("Comparison Count [Log Scale]", fontsize=11, fontweight="medium")
        ax.set_title(f"Input Pattern: {input_type.capitalize()}", fontsize=12, fontweight="bold")
        ax.set_yscale("log")
        ax.legend(frameon=True, facecolor="#ffffff", edgecolor="#cccccc")
        ax.grid(True, which="both", linestyle="--", alpha=0.5)

    plt.tight_layout()
    save_plot("sorting_comparisons.png")


def plot_fibonacci_time_comparison(df):
    """
    Plot execution time comparison for Fibonacci algorithms.
    """
    ensure_output_dir()
    colors = {"Recursive": "#c0392b", "Iterative": "#2980b9", "Dynamic Programming": "#8e44ad"}
    markers = {"Recursive": "o", "Iterative": "s", "Dynamic Programming": "^"}
    linestyles = {"Recursive": "-", "Iterative": "--", "Dynamic Programming": "-."}

    plt.figure(figsize=(10, 6))

    for algo in df["Algorithm"].unique():
        algo_data = df[df["Algorithm"] == algo].dropna()
        plt.plot(
            algo_data["n"],
            algo_data["Execution Time (s)"],
            marker=markers.get(algo, "o"),
            linestyle=linestyles.get(algo, "-"),
            color=colors.get(algo, None),
            linewidth=2.2,
            markersize=7.5,
            label=algo,
        )

    plt.xlabel("Fibonacci Index (n)", fontsize=11, fontweight="medium")
    plt.ylabel("Execution Time (seconds)", fontsize=11, fontweight="medium")
    plt.title("Fibonacci Algorithm Execution Time Benchmark", fontsize=14, fontweight="bold")
    plt.legend(frameon=True, facecolor="#ffffff", edgecolor="#cccccc")
    plt.grid(True, linestyle="--", alpha=0.5)
    save_plot("fibonacci_time_comparison.png")


def plot_fibonacci_memory_comparison(df):
    """
    Plot memory usage comparison for Fibonacci algorithms.
    """
    ensure_output_dir()
    colors = {"Recursive": "#c0392b", "Iterative": "#2980b9", "Dynamic Programming": "#8e44ad"}
    markers = {"Recursive": "o", "Iterative": "s", "Dynamic Programming": "^"}
    linestyles = {"Recursive": "-", "Iterative": "--", "Dynamic Programming": "-."}

    plt.figure(figsize=(10, 6))

    for algo in df["Algorithm"].unique():
        algo_data = df[df["Algorithm"] == algo].dropna()
        plt.plot(
            algo_data["n"],
            algo_data["Memory Usage (KB)"],
            marker=markers.get(algo, "s"),
            linestyle=linestyles.get(algo, "-"),
            color=colors.get(algo, None),
            linewidth=2.2,
            markersize=7.5,
            label=algo,
        )

    plt.xlabel("Fibonacci Index (n)", fontsize=11, fontweight="medium")
    plt.ylabel("Peak Memory Usage (KB)", fontsize=11, fontweight="medium")
    plt.title("Fibonacci Algorithm Memory Consumption", fontsize=14, fontweight="bold")
    plt.legend(frameon=True, facecolor="#ffffff", edgecolor="#cccccc")
    plt.grid(True, linestyle="--", alpha=0.5)
    save_plot("fibonacci_memory_comparison.png")


def generate_all_plots(sorting_df, fibonacci_df):
    """
    Generate all performance comparison plots.

    Args:
        sorting_df: DataFrame with sorting algorithm performance data
        fibonacci_df: DataFrame with Fibonacci algorithm performance data
    """
    print("Generating sorting algorithm plots...")
    plot_sorting_time_comparison(sorting_df)
    plot_sorting_memory_comparison(sorting_df)
    plot_sorting_comparisons(sorting_df)

    print("Generating Fibonacci algorithm plots...")
    plot_fibonacci_time_comparison(fibonacci_df)
    plot_fibonacci_memory_comparison(fibonacci_df)

    print("\nAll plots saved to graphs/ directory")
