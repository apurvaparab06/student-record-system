"""main.py - menu-driven Student Record System. Run with: python main.py"""

from storage import load_data, export_csv
from student import (SUBJECTS, add_student, view_students, search_student,
                     update_student, delete_student, sort_students, report)

MENU = """
========== STUDENT RECORD SYSTEM ==========
1. Add student
2. View all students
3. Search student
4. Update student
5. Delete student
6. Sort students
7. Class report
8. Export to CSV
9. Exit
==========================================="""


def main():
    students = load_data()
    print(f"Loaded {len(students)} record(s).")

    while True:
        print(MENU)
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            sort_students(students)
        elif choice == "7":
            report(students)
        elif choice == "8":
            export_csv(students, SUBJECTS)
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()
