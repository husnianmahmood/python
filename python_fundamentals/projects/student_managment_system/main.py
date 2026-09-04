class Student:
  def __init__(self,name:str,roll_number:int,department:str):
    self.name = name
    self.roll_number = roll_number
    self.department = department
    self.marks = {}
  def display_info(self):
    print("\n===== Student Information =====")
    print(f"Student : {self.name}")
    print(f"Roll Number : {self.roll_number}")
    print(f"Department : {self.department}")
    if self.marks:
      print("\n===Marks===:")
      for subject, mark in self.marks.items():
        print(f"{subject}: {mark}")
    else:
      print("\n No marks added yet.")

  def add_marks(self):
    subject = input("Enter the name of the subject: ")
    mark = float(input("Enter the marks of the subject: "))

    self.marks[subject] = mark
    print(f"{subject} marks added successfully.")

  def calculate_average(self):
    if not self.marks:
      print("No Marks available. ")
      return
    total = sum(self.marks.values())
    average = total/len(self.marks)
    return average
  def check_result(self):
    average = self.calculate_average()
    if average is None:
      return
    print(f"Average: {average:.2f}")
    if average >= 50:
      print("Result: Pass")
    else:
      print("Result: Fail")

def main():
  print("\n===== Student Information =====")

  name = input("Enter Student Name: ")
  roll_number = input("Enter Student Roll Number: ")
  department = input("Enter Student Department: ")

  student = Student(name, roll_number, department)

  while True:
    print("\n===== Menu =====")
    print("1. Display Student Information")
    print("2. Add Marks")
    print("3. Calculate Average")
    print("4. Check Result")
    print("5. Exit")

    choice = input("Enter your choice(1-5): ")

    if choice == "1":
      student.display_info()
    elif choice == "2":
      student.add_marks()
    elif choice == "3":
      student.calculate_average()
    elif choice == "4":
      student.check_result()
    elif choice == "5":
      print("Thank you for using Student Management System.")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
