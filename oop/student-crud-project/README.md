<!-- Header Section -->

<div align="center">

🎓 Student CRUD Project

A Python-based Student Management System that demonstrates Object-Oriented Programming concepts through CRUD operations — Create, Read, Update, and Delete student records.

![Language](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Concept](https://img.shields.io/badge/Concept-CRUD%20Operations-6A5ACD?style=for-the-badge) ![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

Overview • Features • Key Concepts • Project Structure • How to Run • Future Improvements

</div>

📖 Overview

The Student CRUD Project is a console-based Python application designed to manage student records using Object-Oriented Programming principles.

The application allows users to add new students, view existing records, update student information, and delete student records through an interactive menu.

Each student is represented as an object of the Student class, while the StudentManagement class handles the operations required to manage student records.

This project focuses on applying OOP concepts to a practical application while improving programming logic, code organization, and data management skills.

The main goals of this project are to improve:

Python programming
Object-Oriented Programming
CRUD operations
Class and object design
Data management using dictionaries
User input handling
Problem-solving skills
Code organization and readability
✨ Features

The application provides the following functionality:

Add Student: Create a new student record with a name, age, roll number, email, and course.
View Students: Display all stored student records, including their unique IDs and personal information.
Update Student: Modify existing student details while keeping unchanged fields intact.
Delete Student: Remove a student record using its unique student ID.
Unique Student IDs: Automatically assign an incremental ID to each newly added student.
Interactive Menu: Navigate through the available operations using a simple console-based menu.
Record Validation: Check whether a student ID exists before updating or deleting a record.
Exit Option: Close the application through the menu.
🧠 Key Concepts

This project applies the following Python and Object-Oriented Programming concepts:

Classes & Objects: Using Student and StudentManagement classes to organize application functionality.
Constructors: Initializing student attributes with the __init__() method.
Instance Attributes: Storing student information using self.
Instance Methods: Defining methods to display details and perform student management operations.
Encapsulation: Organizing student data and related operations within classes.
Dictionaries: Storing student objects using unique student IDs as dictionary keys.
CRUD Operations: Implementing Create, Read, Update, and Delete functionality.
Conditional Statements: Checking menu choices and verifying whether student records exist.
Loops: Using a while loop to keep the application running until the user exits.
User Input: Collecting student information and menu selections using input().
Formatted Strings: Displaying student information and messages using f-strings.
Type Hints: Specifying expected parameter types in the Student constructor.
📂 Project Structure
text
student-crud-project/
├── README.md       # Project documentation
└── main.py         # Application source code

Main Components

1. Student Class

Represents an individual student and stores the following attributes:

name
age
roll_no
email
course

It also includes the show_details() method to display the student's information.

2. StudentManagement Class

Manages the student records and implements the core CRUD operations:

add_student() — Adds a new student.
view_students() — Displays all student records.
update_student() — Updates the details of an existing student.
delete_student() — Deletes a student record.

The class uses a dictionary to store student objects and a counter to generate unique student IDs.

3. Main Program

The main program creates a StudentManagement object and displays a menu that allows users to perform operations until they choose to exit.

▶️ How to Run
Prerequisites
Python 3 installed on your system.
A code editor or terminal.
Step 1: Clone the Repository
bash
git clone https://github.com/husnianmahmood/python_projects.git

Step 2: Navigate to the Project Directory
bash
cd python_projects/oop/student-crud-project

Step 3: Run the Application
bash
python main.py


If your system uses python3 to run Python, use:

bash
python3 main.py

💻 Example Menu
text
----- STUDENT MANAGEMENT SYSTEM -----
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit

Choose an option:


Users can select an option to manage student records or exit the program.

📈 Learning Progress

This project demonstrates practical experience with:

Creating classes and objects
Initializing objects with constructors
Organizing student data using instance attributes
Implementing CRUD operations
Managing objects in a dictionary
Updating selected fields without replacing unchanged values
Using loops and conditional statements
Building an interactive console application

Status: ✅ Completed

🚀 Future Improvements

The project can be extended with the following enhancements:

Add input validation for age and other student details.
Handle invalid numeric input using exception handling.
Prevent duplicate roll numbers and email addresses.
Store student records in a JSON file or database.
Load saved records when the application starts.
Add search functionality by student ID, name, or roll number.
Introduce unit tests for CRUD operations.
Separate classes into individual Python modules.
Add a graphical user interface or web-based interface.
These improvements can make the application more robust, scalable, and suitable for practical use.
🎯 Conclusion

The Student CRUD Project provides practical experience in building a Python application using Object-Oriented Programming principles.

By implementing Create, Read, Update, and Delete operations, the project demonstrates how classes, objects, dictionaries, methods, loops, and conditional statements work together to manage data in a structured way.

It serves as a foundation for more advanced student management applications involving persistent storage, validation, testing, databases, and user interfaces.
