# ⚡ Empirical Evaluation of Sorting & Fibonacci Algorithms
### *Design and Analysis of Algorithms — Case Study & Empirical Analysis*

---

> **Student Details**
> - **Student Name:** Bhavya Rattan
> - **Roll Number:** 2401201004
> - **Program:** BCA (AI & Data Science) — Section B (Semester 5)
> - **Institution:** K.R. Mangalam University
> - **Submitted To:** Dr. Aarti Sangwan

---

## 📌 Executive Summary

This repository presents an empirical benchmarking study comparing the execution runtime, peak memory allocation, and operational comparison counts of four classic sorting algorithms (Bubble, Insertion, Merge, Quick) and three Fibonacci sequence computation strategies (Naive Recursive, Iterative, Memoized Dynamic Programming). 

All algorithms are evaluated across 7 dataset scales ranging from small arrays ($n=80$) up to large scale inputs ($n=10,000$), testing **random**, **sorted**, and **reverse-sorted** initial conditions.

---

## 📁 Repository Structure

```
├── algorithms/
│   ├── sorting.py          # Implementations: Bubble, Insertion, Merge, Quick Sort
│   └── fibonacci.py        # Implementations: Recursive, Iterative, DP Memoization
├── analysis/
│   ├── performance.py      # Wall-clock timing & tracemalloc memory profiling engine
│   └── visualizations.py   # Customized Matplotlib chart rendering engine
├── data/
│   ├── sorting_performance.csv    # Raw benchmark dataset for sorting algorithms
│   └── fibonacci_performance.csv  # Raw benchmark dataset for Fibonacci sequence
├── graphs/                 # Visual benchmark charts (PNG format)
├── notebook/
│   ├── run_analysis.py            # Automated execution script for full pipeline
│   └── algorithm_efficiency_analysis.ipynb # Interactive Jupyter analysis notebook
├── reports/
│   ├── algorithm_performance_case_study.md   # Complete analytical report (Markdown)
│   ├── algorithm_performance_case_study.pdf  # Final compiled report (PDF)
│   └── graphs/                            # Report embedded charts
├── requirements.txt        # Python dependency specifications
└── README.md               # Project documentation
```

---

## ⚙️ Experimental Parameters & Setup

* **Runtime Environment:** Python 3.14 running on Windows 11 (x86_64 architecture).
* **Timing Precision:** Standard high-resolution wall-clock timer (`time.perf_counter()`), reporting 3-run medians to eliminate background system variance.
* **Memory Tracking:** Python standard library `tracemalloc` measuring peak heap memory allocation per run.
* **Data Scale Range:**
  * **Sorting:** $n \in \{80, 200, 500, 1200, 3000, 6000, 10000\}$
  * **Fibonacci:** $n \in \{8, 14, 20, 26, 32, 36, 40\}$
* **Random Seed:** Set to `2026` with integer values drawn from $[1, 500000]$.

---

## 🚀 Execution & Reproduction Guide

### 1. Environment Setup
```bash
pip install -r requirements.txt
```

### 2. Run Benchmarks & Regenerate All Assets
Execute the master analysis pipeline to generate fresh CSV datasets and visual charts:
```bash
python notebook/run_analysis.py
```

### 3. Interactive Analysis
Launch the Jupyter notebook to inspect algorithm logic step-by-step:
```bash
jupyter notebook notebook/algorithm_efficiency_analysis.ipynb
```

---

## 📊 Benchmark Visual Gallery

### Sorting Algorithms Analysis
| Execution Time (Log Scale) | Memory Allocation | Operational Comparisons |
| :---: | :---: | :---: |
| ![Sorting Time](graphs/sorting_time_comparison.png) | ![Sorting Memory](graphs/sorting_memory_comparison.png) | ![Sorting Comparisons](graphs/sorting_comparisons.png) |

### Fibonacci Sequence Analysis
| Runtime vs $n$ | Memory Utilization vs $n$ |
| :---: | :---: |
| ![Fibonacci Time](graphs/fibonacci_time_comparison.png) | ![Fibonacci Memory](graphs/fibonacci_memory_comparison.png) |

---

## 📄 Final Reports
- **Markdown Report:** [`reports/algorithm_performance_case_study.md`](reports/algorithm_performance_case_study.md)
- **PDF Deliverable:** [`reports/algorithm_performance_case_study.pdf`](reports/algorithm_performance_case_study.pdf)
