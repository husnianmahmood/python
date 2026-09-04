
<!-- Header Section -->
<div align="center">

# 🎓 Student Management System (OOP Project)

**An interactive CLI application built with Python using Object-Oriented principles to manage student records, subject marks, grade averages, and academic results.**

[![Language](https://img.shields.io/badge/Language-Python%203.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Paradigm](https://img.shields.io/badge/Paradigm-Object--Oriented-orange?style=for-the-badge)](https://docs.python.org/3/tutorial/classes.html)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Type](https://img.shields.io/badge/Project-Mini%20Project-blue?style=for-the-badge)](#-key-features)

[Overview](#-overview) •
[Key Features](#-key-features) •
[Technical Architecture](#-technical-architecture) •
[OOP Concepts Applied](#-oop-concepts-applied) •
[Execution & Sample Usage](#-execution--sample-usage) •
[License](#-license)

---

</div>

## 📌 Overview

The **Student Management System** is an interactive menu-driven console application designed to handle individual student academic profiles. Built using Object-Oriented Programming (OOP) in Python, it tracks profile metadata (Name, Roll Number, Department), manages dynamic subject-wise mark entries using Python dictionaries, and evaluates overall academic performance.

---

## ✨ Key Features

* **Interactive Menu Interface:** Terminal-based user workflow allowing seamless navigation through options.
* **Dynamic Mark Management:** Uses dictionary data structures to register multiple subjects alongside floating-point score values.
* **Academic Average Calculation:** Computes cumulative mean percentages across all added subjects automatically.
* **Automated Pass/Fail Status:** Evaluates average scores against a passing threshold ($\ge 50\%$) to present instant academic result checks.
* **Profile Overview:** Displays comprehensive summaries combining student metadata and complete mark breakdown listings.

---

## 🏗️ Technical Architecture

```text
+-------------------------------------------------------+
|                        Student                        |
+-------------------------------------------------------+
| - name: str                                           |
| - roll_number: int                                    |
| - department: str                                     |
| - marks: dict                                         |
+-------------------------------------------------------+
| + display_info(): None                                |
| + add_marks(): None                                   |
| + calculate_average(): float / None                   |
| + check_result(): None                                |
+-------------------------------------------------------+
