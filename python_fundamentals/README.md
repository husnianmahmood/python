<!-- Header Section -->
<div align="center">

# 🐍 Python Fundamentals & OOP Module

**A comprehensive core module combining a 15-program sequential practice track with 3 Object-Oriented mini-projects.**

[![Language](https://img.shields.io/badge/Language-Python%203.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Paradigm](https://img.shields.io/badge/Paradigm-Procedural%20%26%20OOP-orange?style=for-the-badge)](https://docs.python.org/3/tutorial/classes.html)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Track](https://img.shields.io/badge/Track-Fundamentals-blue?style=for-the-badge)](#-module-breakdown)

[Overview](#-overview) •
[Module Breakdown](#-module-breakdown) •
[Core Skills & Concepts](#-core-skills--concepts) •
[Repository Structure](#-repository-structure) •
[Execution & Usage](#-execution--usage) •
[License](#-license)

---

</div>

## 📌 Overview

This repository represents the foundational pillar of the Python curriculum. Designed to build proficiency from the ground up, it transitions from basic syntax, flow control, and functions into data encapsulation, object-oriented software design, and terminal-based applications.

---

## 📂 Module Breakdown

### 🔹 1. Sequential Core Practice (`practice/`)
A progressive curriculum of **15 core Python programs** focused on building strong syntax habits and object encapsulation:
* **Programs 1–9:** Fundamental syntax, data structures (lists, dictionaries, tuples), loops, and function implementations.
* **Programs 10–12:** Data encapsulation, private properties (`__attr`), custom setter validation, and modern `@property` decorators.
* **Programs 13–15:** Object interactions, class composition, and error handling mechanics.

---

### 🔹 2. Hands-On Mini-Projects (`projects/`)
Three domain-specific Object-Oriented terminal applications applying software design patterns:

* **[Bank Management System](./projects/bank_managment_system):** Demonstrates abstract base classes (`ABC`), polymorphic account behaviors, overdraft limits, and protected balance setters.
* **[Movie Ticket Management System](./projects/movie_ticket_managment_system):** Handles real-time theater seat inventory, capacity validation, and price calculations.
* **[Student Management System](./projects/student_managment_system):** An interactive menu-driven app managing student profiles, dynamic mark registration via dictionaries, and average percentage evaluations.

---

## 🧠 Core Skills & Concepts

* **Encapsulation & Protection:** Restricting direct state mutation using double-underscore private attributes (`__attr`) and Pythonic property decorators (`@property`, `@setter`).
* **Object-Oriented Abstraction:** Defining abstract interfaces with `@abstractmethod` to enforce consistent child-class implementation contracts.
* **Inheritance & Polymorphism:** Reusing base class functionality while overriding specialized behaviors (e.g., custom account withdrawal rules).
* **CLI System Architecture:** Designing interactive menu loops and input validation workflows.

---

## 🏗️ Repository Structure

```text
python_fundamentals/
├── README.md                            # Main module README (This file)
├── practice/                            # Sequential practice track
│   ├── program_1.py
│   ├── ...
│   ├── program_10.py                    # Encapsulation & private attributes
│   ├── program_11.py                    # Validation logic & getters/setters
│   └── program_12.py                    # Refactored with @property decorators
└── projects/                            # Mini-project implementations
    ├── README.md                        # Projects overview & matrix
    ├── bank_managment_system/           # Banking app with ABC & polymorphism
    ├── movie_ticket_managment_system/   # Real-time seating reservation system
    └── student_managment_system/        # Interactive menu grade analyzer
