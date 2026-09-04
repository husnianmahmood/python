<!-- Header Section -->
<div align="center">

# 🏦 Bank Management System (OOP Project)

**A Python-based banking application demonstrating core Object-Oriented Programming principles including abstraction, inheritance, polymorphism, and dynamic method overriding.**

[![Language](https://img.shields.io/badge/Language-Python%203.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Paradigm](https://img.shields.io/badge/Paradigm-Object--Oriented-orange?style=for-the-badge)](https://docs.python.org/3/tutorial/classes.html)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Type](https://img.shields.io/badge/Project-Mini%20Project-blue?style=for-the-badge)](#-architecture--class-hierarchy)

[Overview](#-overview) •
[Key Features](#-key-features) •
[Architecture & Class Hierarchy](#-architecture--class-hierarchy) •
[OOP Concepts Applied](#-oop-concepts-applied) •
[Execution & Sample Output](#-execution--sample-output) •
[License](#-license)

---

</div>

## 📌 Overview

The **Bank Management System** is a modular Python program designed to simulate basic banking operations across distinct account types. Built using Python's native `abc` (Abstract Base Class) module, this project serves as a practical implementation of fundamental and advanced Object-Oriented Programming (OOP) concepts such as abstract interfaces, encapsulation via `@property` getters/setters, subclass inheritance, and runtime polymorphism.

---

## ✨ Key Features

* **Abstract Banking Blueprint:** Enforces a standardized structure across all derived account classes using abstract methods (`account_type` and `show_details`).
* **Encapsulated Balance Protection:** Utilizes protected attributes (`_balance`) guarded by `@property` getters and `@balance.setter` logic to reject negative values.
* **Savings Account Operations:** Handles standard deposits, withdrawals, interest calculations, and account state displays.
* **Current Account Overdraft Protection:** Custom withdrawal rules leveraging overdraft limits (`balance + overdraft_limit`) to process transactions safely.
* **Fixed Deposit Lock-In Logic:** Prevents early withdrawals prior to maturity (`is_matured`) and calculates total interest over multi-year terms.
* **Polymorphic Account Processing:** Iterates through collections of varying account objects to invoke common interfaces dynamically.

---

## 🏗️ Architecture & Class Hierarchy

```text
               +-----------------------+
               |  BankAccount (ABC)    |  <-- Abstract Base Class
               +-----------------------+
               | - account_number      |
               | - account_holder      |
               | - _balance            |
               +-----------------------+
               | + deposit()           |
               | + withdraw()          |
               | + account_type()*     |
               | + show_details()*     |
               +-----------+-----------+
                           |
        +------------------+------------------+
        |                  |                  |
+-------v-------+  +-------v-------+  +-------v-------+
| SavingAccount |  | CurrentAccount|  |  FixedDeposit |
+---------------+  +---------------+  +---------------+
| + interest_rate| | + overdraft   |  | + maturity_yrs|
|               |  |   _limit      |  | + is_matured  |
+---------------+  +---------------+  +---------------+
