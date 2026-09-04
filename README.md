<!-- Header Section -->
<div align="center">

# 🐍 Python — A Learning Journey

**Documenting my evolution as a Python developer — from core fundamentals to Object-Oriented Programming, and now into Data Science.**

[![Language](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Fundamentals](https://img.shields.io/badge/Topic-Fundamentals-4CAF50?style=for-the-badge)](#-python-fundamentals)
[![OOP](https://img.shields.io/badge/Topic-OOP-6A5ACD?style=for-the-badge)](#-object-oriented-programming-oop)
[![Data Science](https://img.shields.io/badge/Next_Up-Data%20Science-FF6F00?style=for-the-badge&logo=numpy&logoColor=white)](#-data-science-in-progress)
[![Status](https://img.shields.io/badge/Status-Actively%20Learning-orange?style=for-the-badge)](#-learning-progress)

[Welcome](#-welcome) •
[Overview](#-overview) •
[Repository Structure](#-repository-structure) •
[Python Fundamentals](#-python-fundamentals) •
[OOP Module](#-object-oriented-programming-oop) •
[Data Science](#-data-science-in-progress) •
[Get in Touch](#-get-in-touch)

---

</div>

## 👋 Welcome

Thanks for stopping by! This repository is my personal log as I learn Python — every folder here represents a step in that process, from writing my first functions to building object-oriented console applications, and now branching into data science.

If you're a recruiter or fellow developer reviewing my profile: this repo is meant to show not just finished projects, but *how* I got there — the practice, the mistakes, the mini-projects, and the steady progression in complexity. Every section below has its own dedicated `README.md` with more detail, so feel free to dig in wherever interests you most.

---

## 📖 Overview

This repository is a structured, continuously growing record of my Python learning path. It's organized into clear stages that mirror how I've actually learned the language:

1. **Python Fundamentals** — syntax, functions, logic, sequential practice, and beginner mini-projects.
2. **Object-Oriented Programming (OOP)** — classes, objects, abstraction, encapsulation, and real-world console applications.
3. **Data Science** — NumPy arrays, vectorized computations, statistical analytics, and financial project tools.

The goal of this repository is to improve:

- Python programming fundamentals & syntax fluency
- Object-Oriented Programming & software design patterns
- Logical thinking & problem-solving
- Code organization & reusable design
- Data analysis skills (NumPy, Pandas)
- Git and GitHub workflow

---

## 🗂️ How This Repo Is Organized

> **Every section, practice program, and project has its own dedicated `README.md`.**

This root README gives you the big picture. For the specifics — what a program does, what concepts it demonstrates, how to run it — open the `README.md` inside that folder. This keeps the root page clean while still giving full detail exactly where it's needed.

| Level | What you'll find there |
|---|---|
| **Root `README.md` (this file)** | The overall journey, structure, and navigation |
| **Module `README.md`** (e.g., `python_fundamentals/README.md`) | What that topic covers and why it matters |
| **Program/Project `README.md`** (e.g., `numpy/projects/finance_analyzer/README.md`) | Purpose, features, architecture, and concepts for that specific file |

---

## 📂 Repository Structure

```text
python/
│
├── python_fundamentals/                   # Core language track
│   ├── README.md                          # Overview of fundamentals & OOP track
│   ├── practice/                          # Sequential core practice programs (1-15)
│   │   ├── README.md                      # Sequential practice documentation
│   │   ├── program_1.py
│   │   ├── ...
│   │   ├── program_10.py                  # Encapsulation & private attributes
│   │   ├── program_11.py                  # Custom setter validation logic
│   │   └── program_12.py                  # Refactored @property decorators
│   └── projects/                          # Fundamentals mini-projects
│       ├── README.md                      # Mini-projects directory overview
│       ├── bank_managment_system/         # Banking system (ABC, OOP)
│       │   ├── README.md
│       │   └── main.py
│       ├── movie_ticket_managment_system/ # Real-time ticket booking system
│       │   ├── README.md
│       │   └── main.py
│       └── student_managment_system/      # Interactive grade manager app
│           ├── README.md
│           └── main.py
│
├── oop/                                   # Specialized Object-Oriented track
│   ├── README.md                          # Overview of OOP concepts
│   └── student_management_system/         # Advanced OOP Student System
│       ├── README.md
│       └── main.py
│
├── numpy/                                 # Data Science & Numerical Computing
│   ├── README.md                          # Combined NumPy practice & project guide
│   ├── practice/                          # Daily structured NumPy practice
│   │   ├── README.md                      # Practice modules documentation (Days 1-3)
│   │   ├── day1/
│   │   │   └── main.py                    # Array creation, metadata & slicing
│   │   ├── day2/
│   │   │   └── main.py                    # Array generators & random sampling
│   │   └── day3/
│   │       └── main.py                    # Vectorized math, aggregations & masking
│   └── projects/                          # NumPy-based projects
│       └── finance_analyzer/              # Financial Data Analysis project
│           ├── README.md                  # Project details & setup guide
│           └── main.py                    # Expense analyzer execution script
│
├── .gitignore
└── README.md                              # Root repository README


## 🧮 Python Fundamentals

The `python_fundamentals/` folder is where the foundation is laid — the building blocks everything else in this repo relies on.

**Covers:**
- Variables, data types, and operators
- Conditionals and loops
- Functions — defining, calling, parameters, return values, scope
- Lists, dictionaries, tuples, and sets
- String manipulation & error handling

**Sequential Practice (`practice/`):** 15 core programs introducing encapsulation, private variables (`__attr`), and `@property` decorators.

**Mini-Projects (`projects/`):** Real-world console apps applying core fundamentals:
- 🏦 Bank Management System
- 🎬 Movie Ticket Management System
- 🎓 Student Management System

👉 [View Python Fundamentals Module](python_fundamentals/)

---

## 🧠 Object-Oriented Programming (OOP)

The `oop/` folder builds on the fundamentals, introducing how to design scalable software using classes and objects rather than plain procedural scripts.

**Covers (introduced progressively):**
- Classes, Objects & Constructors (`__init__`)
- Encapsulation & Access Modifiers
- Abstract Base Classes (ABC) & Interfaces
- Inheritance & Method Overriding
- Dynamic Runtime Polymorphism
- Code Organization & File Handling

**Featured Project:**
- 🎓 **Student Management System** — A comprehensive console application managing student profiles, subject marks, percentage calculations, and academic status evaluations.

👉 [View OOP Module](oop/)

---

## 📊 Data Science (In Progress)

This is the newest chapter in the journey. The `numpy/` folder currently holds structured, day-by-day practice and practical analytics tools:

- **Day 1:** N-dimensional array creation, shape inspection, metadata, and 2D/3D matrix slicing.
- **Day 2:** Built-in sequence generators (`arange`, `linspace`), filled arrays (`zeros`, `ones`, `full`), and random sampling utilities.
- **Day 3:** Vectorized arithmetic, axis-wise aggregations (`axis=0` vs `axis=1`), dynamic reshaping, and boolean filtering.

**Featured Project:**
- 📊 **Student Monthly Expense Analyzer** — A numerical financial analyzer computing spending statistics, monthly budget breakdowns, and automated advisory reports.

👉 [View NumPy Module](numpy/)

---

## 📈 Learning Progress

| Module | Focus | Status |
|---|---|---|
| `python_fundamentals/` | Core syntax, functions, practice programs (1-15), 3 mini-projects | 🟢 Completed |
| `oop/` | Classes, objects, abstract classes, polymorphism | 🟢 Completed |
| `numpy/` | N-D arrays, vectorized computing, axis aggregations, finance analyzer | 🟢 Completed |
| `pandas/` | DataFrames, data cleaning, dataset transformations | ⏳ Planned |

---

## 🔮 Future Improvements

- Continue expanding `python_fundamentals/` with advanced data structure practices
- Add design patterns (Factory, Singleton) to `oop/`
- Introduce real dataset imports (CSV/JSON) into the `numpy/` financial analyzer
- Launch a dedicated `pandas/` module for data cleaning and EDA
- Incorporate unit testing (`unittest` / `pytest`) across existing projects
- Maintain up-to-date sub-`README.md` files as new modules are added

---

## 📬 Get in Touch

Feel free to explore the folders above, open an issue, or reach out if you'd like to chat about any of the projects here.
