<!-- Header Section -->
<div align="center">

# 🎬 Movie Ticket Management System (OOP Project)

**A lightweight, Object-Oriented Python application designed to handle movie screening inventory, automated ticket booking, dynamic seat updates, and total price calculations.**

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

The **Movie Ticket Management System** is a concise Object-Oriented program that models cinema ticket reservations. It encapsulates movie metadata (title, total seats, price per ticket) and provides real-time transaction methods to reserve seats, validate capacity constraints, calculate booking totals, and display live screening statistics.

---

## ✨ Key Features

* **Real-time Inventory Tracking:** Dynamically maintains available seats and booked seat counters upon every transaction.
* **Capacity Validation:** Checks requested ticket quantities against available seating before confirming bookings to prevent overbooking.
* **Automated Price Calculation:** Computes total payable amounts based on ticket quantity and base ticket pricing.
* **Status Monitoring:** Provides full visibility into available vs. booked capacity per movie title.

---

## 🏗️ Technical Architecture

```text
+------------------------------------------+
|                  Movie                   |
+------------------------------------------+
| - movie_name: str                        |
| - total_seats: int                       |
| - ticket_price: int                      |
| - booked_seats: int                      |
+------------------------------------------+
| + book_tickets(num_of_tickets: int)      |
| + show_status(): None                    |
+------------------------------------------+
