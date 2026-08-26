class Student:

    def __init__(self, name: str, roll_number: str, department: str):
        self.name = name
        self.roll_number = roll_number
        self.department = department
        self.marks = {}

    def display_info(self):
        print("\n===== Student Information =====")
        print(f"Student     : {self.name}")
        print(f"Roll Number : {self.roll_number}")
        print(f"Department  : {self.department}")

        if self.marks:
            print("\n===== Marks =====")

            for subject, mark in self.marks.items():
                print(f"{subject}: {mark}")

        else:
            print("\nNo marks added yet.")

    def add_marks(self):
        number_of_subjects = int(
            input("How many subjects do you want to add? ")
        )

        for i in range(number_of_subjects):

            print(f"\nSubject {i + 1}")

            subject = input("Enter subject name: ")
            mark = float(input("Enter marks: "))

            self.marks[subject] = mark

        print("\nAll marks added successfully.")

    def calculate_average(self):

        if not self.marks:
            return None

        total = sum(self.marks.values())
        average = total / len(self.marks)

        return average

    def show_result(self):

        if not self.marks:
            print("\nNo marks available.")
            return

        print("\n===== Result =====")

        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")

        average = self.calculate_average()

        print(f"\nAverage: {average:.2f}")

        if average >= 50:
            print("Result: PASS")
        else:
            print("Result: FAIL")


def main():

    print("\n===== Student Management System =====")

    name = input("Enter Student Name: ")
    roll_number = input("Enter Student Roll Number: ")
    department = input("Enter Student Department: ")

    student = Student(name, roll_number, department)

    while True:

        print("\n===== Menu =====")
        print("1. Display Student Information")
        print("2. Add Marks")
        print("3. Show Result")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            student.display_info()

        elif choice == "2":
            student.add_marks()

        elif choice == "3":
            student.show_result()

        elif choice == "4":
            print("\nThank you for using Student Management System.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
