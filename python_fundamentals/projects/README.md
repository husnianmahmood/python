<!-- Header Section -->
<div align="center">

# 🛠️ Python Fundamentals: Practice Projects

**A collection of Object-Oriented Python mini-projects demonstrating core OOP paradigms, state encapsulation, interactive CLI workflows, and domain-specific business logic.**

[![Language](https://img.shields.io/badge/Language-Python%203.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Paradigm](https://img.shields.io/badge/Paradigm-Object--Oriented-orange?style=for-the-badge)](https://docs.python.org/3/tutorial/classes.html)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Type](https://img.shields.io/badge/Type-Mini%20Projects-blue?style=for-the-badge)](#-project-directory)

[Overview](#-overview) •
[Project Directory](#-project-directory) •
[Core Architectural Concepts](#-core-architectural-concepts) •
[Repository Structure](#-repository-structure) •
[Getting Started](#-getting-started) •
[License](#-license)

---

</div>

## 📌 Overview

This directory houses practical **Object-Oriented Programming (OOP)** mini-projects built during the fundamentals track. Each project applies fundamental Python principles to solve domain-specific problems—ranging from abstract banking system architectures and interactive academic grading managers to cinema ticketing platforms.

---

## 📁 Project Directory

| Project Name | Primary Focus | Key Technical Features |
| :--- | :--- | :--- |
| **[Bank Management System](./bank_managment_system)** | Financial Operations & Abstraction | Abstract base classes (`ABC`), polymorphic account types, overdraft rules, and property-level balance encapsulation. |
| **[Movie Ticket Management System](./movie_ticket_managment_system)** | Real-time Seat Reservations | Seat inventory validation, price calculation algorithms, and capacity tracking. |
| **[Student Management System](./student_managment_system)** | Interactive Grade Analytics | Interactive CLI menu loop, dynamic dictionary mapping for subjects/marks, average percentage calculation, and result evaluation. |

---

## 🧠 Core Architectural Concepts

Across these mini-projects, key software engineering paradigms and Python features are implemented:

* **Abstraction (`abc.ABC` & `@abstractmethod`):** Establishing structural blueprints and interfaces that derived subclasses must fulfill (e.g., standardizing `BankAccount` actions).
* **Encapsulation & Validation:** Protecting instance state variables via double underscores (`__attr`) or protected properties (`_attr`), combined with modern Pythonic `@property` getters and setters.
* **Inheritance & Method Overriding:** Extending core behaviors into specialized entities (e.g., overriding withdrawal logic for `CurrentAccount` vs. `FixedDepositAccount`).
* **Polymorphism:** Invoking uniform interfaces on heterogeneous collections of objects dynamically at execution time.
* **CLI Control Flow:** Building structured terminal menu loops with input validation and error handling.

---

## 🏗️ Repository Structure

```text
python_fundamentals/projects/
├── README.md                           # Mini-projects overview (This file)
├── bank_managment_system/
│   ├── README.md                       # Project details & class architecture
│   └── main.py                         # Banking system application code
├── movie_ticket_managment_system/
│   ├── README.md                       # Project details & seating logic
│   └── main.py                         # Ticketing reservation system
└── student_managment_system/
    ├── README.md                       # Project details & menu workflow
    └── main.py                         # Student grade management application
