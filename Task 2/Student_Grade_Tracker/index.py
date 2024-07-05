class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}
    
    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]
    
    def calculate_average(self):
        total_grades = 0
        total_subjects = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            total_subjects += len(grades)
        return total_grades / total_subjects if total_subjects > 0 else 0

def main():
    students = {}

    while True:
        print("\nStudent Grade Tracker")
        print("1. Add a new student")
        print("2. Add a grade for a student")
        print("3. Calculate average grade for a student")
        print("4. Display all students and their grades")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter the student's name: ")
            if name not in students:
                students[name] = Student(name)
                print(f"Student {name} added.")
            else:
                print("Student already exists.")
        
        elif choice == '2':
            name = input("Enter the student's name: ")
            if name in students:
                subject = input("Enter the subject: ")
                grade = float(input("Enter the grade: "))
                students[name].add_grade(subject, grade)
                print(f"Grade {grade} added for {name} in {subject}.")
            else:
                print("Student not found.")
        
        elif choice == '3':
            name = input("Enter the student's name: ")
            if name in students:
                average = students[name].calculate_average()
                print(f"The average grade for {name} is {average:.2f}.")
            else:
                print("Student not found.")
        
        elif choice == '4':
            if students:
                for name, student in students.items():
                    print(f"\nStudent: {name}")
                    for subject, grades in student.grades.items():
                        print(f"  {subject}: {grades}")
                    print(f"  Average: {student.calculate_average():.2f}")
            else:
                print("No students found.")
        
        elif choice == '5':
            print("Exiting the program.....")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()