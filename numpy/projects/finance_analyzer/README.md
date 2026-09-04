<!-- Header Section -->
<div align="center">

# 📊 Student Monthly Expense Analyzer

**A practical Python & NumPy application designed to help students track expenses, analyze budget allocations, manage personal finances, and receive actionable financial advice.**

[![Language](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Library](https://img.shields.io/badge/Library-NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Storage](https://img.shields.io/badge/Data-JSON-000000?style=for-the-badge&logo=json&logoColor=white)](https://www.json.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)](#-features)

[Overview](#-overview) •
[Features](#-features) •
[Technical Highlights](#-technical-highlights) •
[Repository Structure](#-repository-structure) •
[Installation & Usage](#-installation--usage) •
[Future Roadmap](#-future-roadmap)

---

</div>

## 📖 Overview

The **Student Monthly Expense Analyzer** is a terminal-based financial management system built to assist students in tracking and controlling their daily expenses. Utilizing Object-Oriented Programming (OOP) and **NumPy** array operations, this tool offers statistical insights, spending breakdowns across 7 core categories, budget tracking, and real-time financial health advice.

All session data is persistently serialized into a structured JSON file, ensuring seamless data retrieval across application restarts.

---

## ✨ Features

* **Student Profile Integration:** Maintains student identity across sessions (Name, Department, Semester).
* **Income & Budget Tracking:** Set monthly income and define spending limits with input validation.
* **Categorized Expense Logging:** Track expenses across key categories: *Food, Transport, Education, Bills, Shopping, Entertainment,* and *Other*.
* **NumPy Fast Statistical Analysis:** Computes total, average, peak, and minimum expenditures using array operations.
* **Category Breakdown:** Aggregates overall spending per category and highlights the highest-spending domain.
* **Smart Financial Advisory:** Evaluates spending habits relative to total income and delivers automated actionable advice.
* **Comprehensive Monthly Report:** Summarizes overall financial health, budget performance, and total transactions in a single structured report.
* **Data Persistence:** Automatic JSON saving (`finance_data.json`) and loading upon execution.

---

## 🛠️ Technical Highlights

* **Object-Oriented Architecture:** Encapsulates student data and financial operations into dedicated `Student` and `FinanceManager` classes.
* **NumPy Vectorization:** Transforms basic Python lists into NumPy arrays for high-performance statistical computations (`np.sum`, `np.mean`, `np.max`, `np.min`).
* **Persistent File I/O:** Utilizes Python's `json` and `os` modules to read and write persistent local data safely.
* **Robust Input Validation:** Implements `try-except` blocks and logical boundary checks to prevent runtime invalid inputs or division-by-zero errors.

---

## 📁 Repository Structure

```text
python/
└── numpy/
    ├── README.md
    ├── practice/
    │   ├── day1/
    │   │   └── main.py
    │   ├── day2/
    │   │   └── main.py
    │   └── day3/
    │       └── main.py
    └── projects/
        └── finance_analyzer/
            ├── README.md
            └── main.py
