<!-- Header Section -->
<div align="center">

# 🧮 NumPy Module: Core Practice & Financial Analytics

**A comprehensive hands-on repository containing structured daily foundational practice and a full-featured Student Monthly Expense Analyzer.**

[![Language](https://img.shields.io/badge/Language-Python%203.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Library](https://img.shields.io/badge/Library-NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Storage](https://img.shields.io/badge/Data-JSON-000000?style=for-the-badge&logo=json&logoColor=white)](https://www.json.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

[Overview](#-overview) •
[Daily Practice Track](#-daily-practice-track) •
[Featured Project](#-featured-project) •
[Technical Skills Gained](#-technical-skills-gained) •
[Repository Structure](#-repository-structure) •
[Installation & Usage](#-installation--usage) •
[License](#-license)

---

</div>

## 📌 Overview

This repository represents the entire **NumPy** learning path within the Python curriculum. It bridges theoretical fundamentals and practical real-world application by combining a progressive 3-day core practice curriculum with an Object-Oriented **Student Monthly Expense Analyzer** terminal app.

---

## 📅 Daily Practice Track

The practice section focuses on building fundamental competencies in N-dimensional array manipulation, mathematical vectorization, and logical data filtering.

### 🔹 Day 1: Array Basics, Attributes & Indexing
* **Array Instantiation:** Initializing 1D, 2D, and 3D arrays (`np.array()`) with explicit data typing.
* **Metadata Inspection:** Querying shapes, dimensions, sizes, and data types via `.shape`, `.ndim`, `.size`, and `.dtype`.
* **Spatial Slicing:** Accessing specific element coordinates (e.g., `arr[1, 2]`) and multi-dimensional sub-grids (`arr[0:2, 1:3]`).
* **Basic Vectorization:** Performing scalar multiplication and basic element transformations.

### 🔹 Day 2: Creation Routines & Random Sampling
* **Initialization Functions:** Generating zero, one, and constant arrays via `np.zeros()`, `np.ones()`, and `np.full()`.
* **Sequencing Routines:** Constructing uniform step arrays with `np.arange()` and linearly spaced vectors with `np.linspace()`.
* **Random Utilities:** Producing uniform continuous values (`np.random.rand()`) and bounded random integers (`np.random.randint()`).

### 🔹 Day 3: Operations, Aggregations & Masking
* **Vectorized Arithmetic:** Executing element-wise arithmetic between scalars and multi-array pairs.
* **Axis-Based Statistics:** Computing global and directional (`axis=0` vs `axis=1`) operations (`sum`, `mean`, `median`, `min`, `std`).
* **Reshaping Dynamics:** Restructuring array layouts using `.reshape()`.
* **Boolean Filtering:** Evaluating boolean arrays (`arr > 3`) to extract conditional data subsets dynamically.

---

## 🚀 Featured Project: Student Monthly Expense Analyzer

Located in `projects/finance_analyzer/`, this terminal application applies NumPy numerical computations to real-world financial tracking and budget analysis.

### ✨ Key Features
* **Student Profile Integration:** Manages profile identity across sessions (Name, Department, Semester).
* **Income & Budget Tracking:** Sets monthly income and spending limits with boundary checks.
* **Categorized Expense Logging:** Tracks transactions across 7 categories (*Food, Transport, Education, Bills, Shopping, Entertainment, Other*).
* **NumPy Vectorized Analytics:** Computes total, mean, peak, and minimum expenditures using fast array reductions (`np.sum`, `np.mean`, `np.max`, `np.min`).
* **Smart Financial Advisory:** Generates automated spending advice by analyzing expense ratios against total income.
* **JSON Data Persistence:** Automatically serializes and loads user records (`finance_data.json`).

---

## 🧠 Technical Skills Gained

* **Vectorized Computation:** Replacing slow Python loops with C-optimized NumPy array operations.
* **Axis-Based Reductions:** Summarizing columnar and row-wise metrics across multidimensional matrices.
* **Data Masking & Filtering:** Extracting target data points using logical boolean indices.
* **Object-Oriented Integration:** Combining NumPy arrays with standard Python OOP architectures and persistent JSON storage.

---

## 📁 Repository Structure

```text
numpy/
├── README.md                          # Combined module README
├── practice/
│   ├── day_1/
│   │   └── main.py                    # Arrays, metadata, indexing & slicing
│   ├── day_2/
│   │   └── main.py                    # Generators, sequences & random sampling
│   └── day_3/
│       └── main.py                    # Arithmetic, axis aggregations & masking
└── projects/
    └── finance_analyzer/
        ├── README.md                  # Project-specific documentation
        └── main.py                    # Expense analyzer application code
