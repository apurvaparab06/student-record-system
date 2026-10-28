"""student.py - input validation and all student operations (CRUD, sort, report)."""

from storage import save_data

SUBJECTS = ["Python", "DSA", "Maths"]
MAX_MARKS = 100


# ---------- Input helpers (validation) ----------

def get_int(prompt, low, high):
    """Keep asking until the user enters an integer between low and high."""
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            print(f"  Enter a number between {low} and {high}.")
        except ValueError:
            print("  Invalid input. Please enter a number.")


def get_name(prompt):
    """Name must contain only letters and spaces."""
    while True:
        name = input(prompt).strip()
        if name and name.replace(" ", "").isalpha():
            return name.title()
        print("  Name must contain only letters and spaces.")


def get_text(prompt):
    """Text must not be empty."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("  This field cannot be empty.")


def get_marks():
    """Ask for marks in every subject."""
    return {sub: get_int(f"  Marks in {sub} (0-{MAX_MARKS}): ", 0, MAX_MARKS)
            for sub in SUBJECTS}


# ---------- Helpers ----------

def find_student(students, roll_no):
    """Return the student dict with this roll number, or None."""
    for s in students:
        if s["roll_no"] == roll_no:
            return s
    return None


def calculate_result(student):
    """Return (total, percentage, grade) for a student."""
    total = sum(student["marks"].values())
    percentage = total / (MAX_MARKS * len(SUBJECTS)) * 100
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "F"
    return total, round(percentage, 2), grade


def print_table(students):
    """Print students in a neat table."""
    if not students:
        print("No records to show.")
        return
    header = f"{'Roll No':<10}{'Name':<22}{'Age':<6}{'Course':<24}{'Total':<8}{'%':<8}{'Grade'}"
    print("\n" + header)
    print("-" * len(header))
    for s in students:
        total, pct, grade = calculate_result(s)
        print(f"{s['roll_no']:<10}{s['name']:<22}{s['age']:<6}{s['course']:<24}"
              f"{total:<8}{pct:<8}{grade}")


def print_student(s):
    """Print full details of one student."""
    total, pct, grade = calculate_result(s)
    print(f"\nRoll No : {s['roll_no']}")
    print(f"Name    : {s['name']}")
    print(f"Age     : {s['age']}")
    print(f"Course  : {s['course']}")
    for sub, m in s["marks"].items():
        print(f"  {sub:<8}: {m}")
    print(f"Total   : {total}/{MAX_MARKS * len(SUBJECTS)}  ({pct}%)  Grade: {grade}")


# ---------- CRUD operations ----------

def add_student(students):
    print("\n--- Add Student ---")
    roll_no = get_text("Roll number: ").upper()
    if find_student(students, roll_no):
        print("A student with this roll number already exists.")
        return
    student = {
        "roll_no": roll_no,
        "name": get_name("Name: "),
        "age": get_int("Age (15-60): ", 15, 60),
        "course": get_text("Course: "),
        "marks": get_marks(),
    }
    students.append(student)
    save_data(students)
    print("Student added successfully.")


def view_students(students):
    print("\n--- All Students ---")
    print_table(students)


def search_student(students):
    print("\n--- Search Student ---")
    query = get_text("Enter roll number or part of the name: ").lower()
    matches = [s for s in students
               if query == s["roll_no"].lower() or query in s["name"].lower()]
    if not matches:
        print("No student found.")
        return
    for s in matches:
        print_student(s)


def update_student(students):
    print("\n--- Update Student ---")
    roll_no = get_text("Roll number of student to update: ").upper()
    student = find_student(students, roll_no)
    if not student:
        print("Student not found.")
        return

    print("What do you want to update?")
    print("1. Name   2. Age   3. Course   4. Marks")
    choice = input("Choice: ").strip()
    if choice == "1":
        student["name"] = get_name("New name: ")
    elif choice == "2":
        student["age"] = get_int("New age (15-60): ", 15, 60)
    elif choice == "3":
        student["course"] = get_text("New course: ")
    elif choice == "4":
        student["marks"] = get_marks()
    else:
        print("Invalid choice. Nothing changed.")
        return
    save_data(students)
    print("Student updated successfully.")


def delete_student(students):
    print("\n--- Delete Student ---")
    roll_no = get_text("Roll number of student to delete: ").upper()
    student = find_student(students, roll_no)
    if not student:
        print("Student not found.")
        return
    confirm = input(f"Delete {student['name']}? (y/n): ").strip().lower()
    if confirm == "y":
        students.remove(student)
        save_data(students)
        print("Student deleted.")
    else:
        print("Deletion cancelled.")


# ---------- Extras ----------

def sort_students(students):
    print("\n--- Sort Students ---")
    print("1. By name   2. By roll number   3. By total marks (high to low)")
    choice = input("Choice: ").strip()
    if choice == "1":
        result = sorted(students, key=lambda s: s["name"].lower())
    elif choice == "2":
        result = sorted(students, key=lambda s: s["roll_no"])
    elif choice == "3":
        result = sorted(students, key=lambda s: calculate_result(s)[0], reverse=True)
    else:
        print("Invalid choice.")
        return
    print_table(result)


def report(students):
    print("\n--- Class Report ---")
    if not students:
        print("No records to report on.")
        return
    results = [(s, calculate_result(s)) for s in students]
    topper, (t_total, t_pct, _) = max(results, key=lambda r: r[1][0])
    avg = sum(r[1][1] for r in results) / len(results)
    above_75 = sum(1 for r in results if r[1][1] >= 75)
    failed = sum(1 for r in results if r[1][2] == "F")
    print(f"Total students     : {len(students)}")
    print(f"Class average      : {avg:.2f}%")
    print(f"Topper             : {topper['name']} ({topper['roll_no']}) - {t_pct}%")
    print(f"Students above 75% : {above_75}")
    print(f"Students with F    : {failed}")
