<!-- Header Section -->
<div align="center">

# 📊 NumPy Practice & Core Concepts

**A structured 3-day deep dive into foundational NumPy operations, multi-dimensional array manipulation, and statistical computations.**

[![Language](https://img.shields.io/badge/Language-Python%203.x-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![Library](https://img.shields.io/badge/Library-NumPy-013243?style=for-the-badge&logo=numpy)](https://numpy.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Type](https://img.shields.io/badge/Project-Daily%20Practice-blue?style=for-the-badge)](#-daily-curriculum)

[Overview](#-overview) •
[Daily Curriculum](#-daily-curriculum) •
[Technical Skills Gained](#-technical-skills-gained) •
[Repository Structure](#-repository-structure) •
[Installation & Execution](#-installation--execution) •
[License](#-license)

---

</div>

## 📌 Overview

This directory contains a progressive, hands-on module covering fundamental to intermediate **NumPy** concepts. Designed as part of a daily practice framework, it transitions from basic array attributes and multi-dimensional slicing to standard mathematical generators, vectorization, axis-based statistical aggregations, dynamic reshaping, and boolean indexing.

---

## 📅 Daily Curriculum

### 🔹 Day 1: Array Basics, Attributes & Indexing
Focuses on initializing N-dimensional arrays, inspecting array metadata, and performing spatial slicing.
* **Array Instantiation:** Initializing 1D, 2D, and 3D arrays (`np.array()`) with custom data types.
* **Array Metadata:** Inspecting shapes, dimensions, element counts, and data types via `.shape`, `.ndim`, `.size`, and `.dtype`.
* **Multi-Dimensional Indexing:** Accessing specific coordinate elements (e.g., `arr[1, 2]`) and sub-grid slicing (e.g., `arr[0:2, 1:3]`).
* **Basic Vectorization:** Elementary scalar-array arithmetic.

### 🔹 Day 2: Array Generation Routines & Random Sampling
Explores standard built-in routines for dynamic array construction and probabilistic initialization.
* **Initialization Functions:** Creating structured zero, one, and constant arrays using `np.zeros()`, `np.ones()`, and `np.full()`.
* **Sequencing:** Generating uniform steps via `np.arange()` (with positive/negative steps) and linearly spaced points using `np.linspace()`.
* **Random Utilities:** Generating uniform float distributions (`np.random.rand()`) and discrete bounded integers (`np.random.randint()`).

### 🔹 Day 3: Vectorized Operations, Aggregations & Masking
Covers numerical computing paradigms, linear transformations, array reshaping, and conditional filtering.
* **Vectorized Arithmetic:** Performing element-wise operations between scalar values and multi-array pairs.
* **Axis-Based Aggregations:** Computing global and directional (`axis=0` vs `axis=1`) statistics: `sum`, `mean`, `median`, `min`, and `std`.
* **Reshaping Dynamics:** Restructuring array layouts via `.reshape()` (e.g., transforming 1D vectors into $2 \times 3$ or $3 \times 2$ matrices).
* **Boolean Filtering:** Evaluating boolean masks (`arr > 3`) to extract targeted conditional subsets.

---

## 🧠 Technical Skills Gained

* **Vectorized Numerical Execution:** Replacing explicit Python `for` loops with optimized C-level vectorized array operations.
* **Multi-Dimensional Spatial Awareness:** Navigating 1D, 2D, and 3D matrix coordinate structures and array strides.
* **Dimensional Axis Aggregation:** Performing matrix reductions along specific axes for data summary calculations.
* **Conditional Data Extraction:** Constructing boolean masks to isolate and evaluate complex datasets efficiently.

---

## 📁 Repository Structure

```text
numpy/practice/
├── day_1/
│   └── main.py    # Basic arrays, dimensions, indexing & slicing
├── day_2/
│   └── main.py    # Creation routines, sequences & random generation
└── day_3/
    └── main.py    # Arithmetic, aggregations, reshaping & masking
