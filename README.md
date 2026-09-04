<div align="center">

# 🐍 Python — Learning Journey

### From Python Fundamentals to Data Science & AI Engineering

A structured and continuously evolving repository documenting my journey with **Python**, from programming fundamentals and Object-Oriented Programming to **NumPy, Pandas, data analysis, and eventually AI engineering**.

<br>

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/OOP-6A5ACD?style=for-the-badge)](#-object-oriented-programming)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge\&logo=numpy\&logoColor=white)](#-data-science)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge\&logo=pandas\&logoColor=white)](#-data-science)
[![Status](https://img.shields.io/badge/Status-Actively%20Learning-orange?style=for-the-badge)](#-learning-progress)

<br>

**Fundamentals → OOP → NumPy → Pandas → Data Analysis → AI Engineering**

</div>

---

## 📌 About This Repository

This repository documents my practical journey of learning **Python and its ecosystem**.

Rather than containing only completed projects, it includes the progression behind them:

* 📚 Concepts and fundamentals
* 🧠 Programming practice
* 🧩 Object-Oriented Programming
* 🛠️ Console-based projects
* 📊 Numerical and data analysis
* 📝 Documentation and learning notes
* 🚀 Gradually increasing project complexity

The purpose is to build a strong programming foundation before moving deeper into **Data Science, Machine Learning, and AI Engineering**.

---

## 🗺️ Learning Roadmap

My Python learning journey is organized into progressive stages:

```text
Python Fundamentals
        │
        ▼
Object-Oriented Programming
        │
        ▼
NumPy
        │
        ▼
Pandas
        │
        ▼
Data Analysis & Visualization
        │
        ▼
Machine Learning
        │
        ▼
AI Engineering
        │
        ▼
Agentic AI
```

Each stage builds upon the previous one rather than being studied independently.

---

# 📂 Repository Structure

```text
python/
│
├── python_fundamentals/
│   ├── README.md
│   │
│   ├── practice/
│   │   ├── README.md
│   │   ├── program_1.py
│   │   ├── program_2.py
│   │   ├── ...
│   │   ├── program_10.py
│   │   ├── program_11.py
│   │   └── program_12.py
│   │
│   └── projects/
│       ├── README.md
│       │
│       ├── bank_management_system/
│       │   ├── README.md
│       │   └── main.py
│       │
│       ├── movie_ticket_management_system/
│       │   ├── README.md
│       │   └── main.py
│       │
│       └── student_management_system/
│           ├── README.md
│           └── main.py
│
├── oop/
│   ├── README.md
│   └── student_management_system/
│       ├── README.md
│       └── main.py
│
├── numpy/
│   ├── README.md
│   │
│   ├── practice/
│   │   ├── README.md
│   │   ├── day1/
│   │   │   └── main.py
│   │   ├── day2/
│   │   │   └── main.py
│   │   └── day3/
│   │       └── main.py
│   │
│   └── projects/
│       └── finance_analyzer/
│           ├── README.md
│           └── main.py
│
├── pandas/
│   └── ...
│
├── .gitignore
└── README.md
```

> Each major module and project contains its own `README.md` with detailed explanations, concepts, features, and instructions.

---

# 🐍 Python Fundamentals

The `python_fundamentals/` module establishes the core programming foundation required for everything that follows.

### Topics Covered

* Variables and data types
* Operators
* Conditional statements
* Loops
* Functions
* Parameters and return values
* Scope
* Lists
* Tuples
* Sets
* Dictionaries
* Strings
* Exception handling
* Basic problem solving
* File handling
* Introductory OOP concepts

### 🧪 Practice

The `practice/` directory contains sequential programs designed to strengthen Python fundamentals through hands-on implementation.

The exercises gradually introduce concepts such as:

* Classes and objects
* Encapsulation
* Private attributes
* Getters and setters
* `@property`
* Basic validation logic

### 🛠️ Projects

The `projects/` directory contains small console-based applications built using the concepts learned throughout the fundamentals module.

| Project                           | Description                                 |
| --------------------------------- | ------------------------------------------- |
| 🏦 Bank Management System         | Basic banking operations using OOP          |
| 🎬 Movie Ticket Management System | Ticket booking and management               |
| 🎓 Student Management System      | Student information and academic management |

👉 **[Explore Python Fundamentals](python_fundamentals/)**

---

# 🧠 Object-Oriented Programming

The `oop/` module focuses specifically on designing programs using **Object-Oriented Programming principles**.

The goal is to move from writing simple scripts toward writing programs that are better organized, reusable, and easier to maintain.

### Topics Covered

* Classes and Objects
* Constructors — `__init__`
* Instance attributes and methods
* Encapsulation
* Private attributes
* Properties
* Abstraction
* Abstract Base Classes
* Inheritance
* Method overriding
* Polymorphism
* Runtime polymorphism
* `super()`
* Method Resolution Order (MRO)
* File handling
* Code organization

### ⭐ Featured Project

**Student Management System**

A more structured console application designed to apply OOP concepts in a practical environment.

Features include:

* Student profile management
* Subject and marks management
* Percentage calculation
* Academic status evaluation
* Object-oriented program structure

👉 **[Explore OOP](oop/)**

---

# 📊 Data Science

The `numpy/` module marks the beginning of my transition from general Python programming toward **Data Science and AI**.

## 🔢 NumPy

NumPy is being used to develop a strong understanding of numerical computing and array-based operations.

### Topics Covered

**Day 1**

* N-dimensional arrays
* Array creation
* Shape and dimensions
* Array metadata
* Indexing
* Slicing
* 2D and 3D arrays

**Day 2**

* `arange()`
* `linspace()`
* `zeros()`
* `ones()`
* `full()`
* Random number generation
* Random sampling

**Day 3**

* Vectorized operations
* Arithmetic operations
* Aggregations
* `axis=0`
* `axis=1`
* Reshaping
* Boolean masking
* Conditional filtering

### 📈 Featured Project

**Student Monthly Expense Analyzer**

A practical NumPy-based project that analyzes monthly student expenses and generates useful financial insights.

The project applies:

* NumPy arrays
* Vectorized calculations
* Aggregation functions
* Boolean filtering
* Statistical calculations
* Budget analysis
* Automated recommendations

👉 **[Explore NumPy](numpy/)**

---

# 🐼 Pandas

The `pandas/` module is the next stage of my Data Science learning path.

The focus is on understanding how real-world datasets are loaded, explored, cleaned, transformed, and analyzed.

### Planned Topics

* Series
* DataFrames
* Reading CSV files
* Dataset inspection
* Selecting rows and columns
* Filtering
* Missing values
* Data cleaning
* Sorting
* Grouping
* Aggregation
* Data transformation
* Basic Exploratory Data Analysis (EDA)

👉 **[Explore Pandas](pandas/)**

---

# 📈 Learning Progress

| Module                 | Focus                                                           |     Status     |
| ---------------------- | --------------------------------------------------------------- | :------------: |
| 🐍 Python Fundamentals | Core syntax, functions, data structures & practice              |  🟢 Completed  |
| 🧠 OOP                 | Classes, inheritance, abstraction, encapsulation & polymorphism |  🟢 Completed  |
| 🔢 NumPy               | Arrays, vectorization, aggregation & numerical analysis         |  🟢 Completed  |
| 🐼 Pandas              | DataFrames, cleaning & dataset analysis                         | 🟡 In Progress |
| 📊 Data Analysis       | EDA & visualization                                             |   ⏳ Upcoming   |
| 🤖 Machine Learning    | ML fundamentals & practical models                              |   ⏳ Upcoming   |
| 🧠 AI Engineering      | AI systems, APIs & frameworks                                   |    ⏳ Future    |
| 🤖 Agentic AI          | AI agents and autonomous workflows                              |    ⏳ Future    |

---

# 🎯 Current Focus

My current focus is strengthening my **Data Science foundation** before moving into Machine Learning and AI Engineering.

```text
Python
  ↓
NumPy
  ↓
Pandas
  ↓
Matplotlib
  ↓
Data Analysis
  ↓
Machine Learning
  ↓
AI Engineering
```

The goal is not simply to learn libraries, but to understand **why and when each tool is used**.

---

# 🚀 Future Goals

As this repository grows, I plan to add:

* Advanced Python concepts
* More OOP projects
* Pandas projects
* Data visualization with Matplotlib
* Exploratory Data Analysis projects
* Real-world datasets
* JSON and CSV data processing
* Unit testing with `pytest`
* Machine Learning projects
* API integration
* AI application development
* AI engineering frameworks
* Agentic AI projects

---

# 🧩 Learning Philosophy

> **Learn → Practice → Build → Document → Improve**

I believe programming is best learned by continuously applying concepts to real problems.

Therefore, this repository intentionally contains both **practice programs and projects**.

The progression is more important than simply collecting completed code.

---

# 📚 Documentation

Each major section contains its own documentation.

| Documentation                            | Purpose                                |
| ---------------------------------------- | -------------------------------------- |
| `README.md`                              | Complete repository overview           |
| `python_fundamentals/README.md`          | Python fundamentals documentation      |
| `python_fundamentals/practice/README.md` | Practice program documentation         |
| `python_fundamentals/projects/README.md` | Fundamentals project documentation     |
| `oop/README.md`                          | OOP concepts and project documentation |
| `numpy/README.md`                        | NumPy learning documentation           |
| `numpy/practice/README.md`               | NumPy practice documentation           |
| `numpy/projects/.../README.md`           | Detailed project documentation         |
| `pandas/README.md`                       | Pandas learning documentation          |

---

# 🛠️ Technologies & Tools

### Programming

* Python

### Python Libraries

* NumPy
* Pandas
* Matplotlib

### Development Tools

* Git
* GitHub
* VS Code

### Future Technologies

* Scikit-learn
* APIs
* Machine Learning frameworks
* AI Engineering frameworks
* Agentic AI tools

---

# 📬 Get in Touch

I'm continuously learning, building, and improving.

If you find something interesting in this repository, feel free to explore the projects, review the code, or open an issue with suggestions.

---

<div align="center">

### ⭐ Thanks for visiting my Python learning journey!

**Learning today. Building tomorrow.**

</div>
