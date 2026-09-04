<!-- Header Section -->
<div align="center">

# 🐍 Python Fundamentals: Sequential Core Practice

**A structured series of 15 sequential Python programs covering core syntax, control flow, functions, and object-oriented encapsulation techniques.**

[![Language](https://img.shields.io/badge/Language-Python%203.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Topic](https://img.shields.io/badge/Topic-Fundamentals%20%26%20OOP-green?style=for-the-badge)](https://docs.python.org/3/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Type](https://img.shields.io/badge/Type-Sequential%20Practice-orange?style=for-the-badge)](#-curriculum-overview)

[Overview](#-overview) •
[Curriculum Overview](#-curriculum-overview) •
[Key Technical Concepts](#-key-technical-concepts) •
[Repository Structure](#-repository-structure) •
[Execution Guide](#-execution-guide) •
[License](#-license)

---

</div>

## 📌 Overview

This directory contains a hands-on, sequential practice curriculum consisting of **15 core Python programs**. Designed to build solid fundamental coding habits, the sequence progresses from basic Python constructs and functions to object-oriented encapsulation, private attribute protection, custom setter validation, and modern Pythonic `@property` decorators.

---

## 📅 Curriculum Overview

### 🔹 Programs 1–9: Language Fundamentals & Logic
* Core data types, conditional branching, and loop iterations.
* Function definitions, argument handling, and return values.
* List, dictionary, and tuple manipulations.

### 🔹 Programs 10–12: Encapsulation & Data Protection
* **Program 10 (Bank Account Encapsulation):** Introduces private instance attributes (`__balance`) and getter/setter validation functions (`get_balance()`, `set_balance()`) to enforce non-negative balances.
* **Program 11 (Student Marks & Validation):** Demonstrates strict attribute validation (`0 <= marks <= 100`) using type-hinted methods and private variables (`__marks`).
* **Program 12 (Pythonic Decorators):** Refactors traditional getter/setter methods into clean, modern Python properties using `@property` and `@marks.setter`.

### 🔹 Programs 13–15: Advanced Practice & Applications
* Practical object interaction and class composition.
* Advanced error handling and input sanitation.
* Modular program design in preparations for mini-projects.

---

## 🧠 Key Technical Concepts

* **Private Attributes (`__attribute`):** Utilizing double-underscore name mangling to restrict direct external access to sensitive object data.
* **Encapsulation & Validation:** Guarding data mutation through explicit logic checks before updating internal state.
* **Property Decorators (`@property`):** Writing clean, interface-friendly getters and setters that allow natural attribute assignment (`obj.attr = val`) while maintaining backend validation.
* **Type Annotations:** Applying standard Python type hints (`name: str`, `marks: int`) for better readability and static code analysis.

---

## 📁 Repository Structure

```text
python_fundamentals/practice/
├── program_1.py
├── program_2.py
├── ...
├── program_10.py    # BankAccount class with private balance & encapsulation
├── program_11.py    # Student class with validation methods (0-100 range checks)
├── program_12.py    # Student class refactored with @property & @setter decorators
├── program_13.py
├── program_14.py
└── program_15.py
