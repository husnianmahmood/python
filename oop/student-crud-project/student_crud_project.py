
class Student:
    def __init__(self, name: str, age: int, roll_no: str, email: str, course: str):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.email = email
        self.course = course

    def show_details(self):
        print(f"Student Name = {self.name}")
        print(f"Student Age = {self.age}")
        print(f"Student Roll No = {self.roll_no}")
        print(f"Student Email = {self.email}")
        print(f"Student Course = {self.course}")


class StudentManagement:
    def __init__(self):
        self.students = {}
        self.student_id = 1

    def add_student(self):
        print("----- Add Student -----")
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        roll_no = input("Enter Student Roll No: ")
        email = input("Enter Student Email: ")
        course = input("Enter Student Course: ")

        student = Student(name, age, roll_no, email, course)

        self.students[self.student_id] = student

        print(f"Student added successfully! ID = {self.student_id}")
        self.student_id += 1
        print()

    def view_students(self):
        print("----- View Student -----")
        if len(self.students) == 0:
            print("No student records available")
        else:
            for student_id, student in self.students.items():
                print()
                print(f"Student ID = {student_id}")
                student.show_details()
                print()

    def update_student(self):
        print("----- Update Student -----")
        student_id = int(input("Enter Student ID to update: "))

        if student_id in self.students:
            student = self.students[student_id]

            name = input(f"Enter New Name [{student.name}]: ")
            age = input(f"Enter New Age [{student.age}]: ")
            roll_no = input(f"Enter New Roll No [{student.roll_no}]: ")
            email = input(f"Enter New Email [{student.email}]: ")
            course = input(f"Enter New Course [{student.course}]: ")

            if name:
                student.name = name

            if age:
                student.age = int(age)

            if roll_no:
                student.roll_no = roll_no

            if email:
                student.email = email

            if course:
                student.course = course

            print("Student updated successfully!")
        else:
            print("Student not found")

    def delete_student(self):
        print("----- Delete Student -----")
        student_id = int(input("Enter Student ID to delete: "))

        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully!")
        else:
            print("Student not found")


students = StudentManagement()

while True:
    print()
    print("----- STUDENT MANAGEMENT SYSTEM -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        students.add_student()

    elif choice == "2":
        students.view_students()

    elif choice == "3":
        students.update_student()

    elif choice == "4":
        students.delete_student()

    elif choice == "5":
        print("Program closed")
        break

    else:
        print("Invalid choice")
