"""storage.py - handles saving and loading student data (JSON) and CSV export."""

import csv
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, "students.json")
CSV_FILE = os.path.join(BASE_DIR, "students_export.csv")


def load_data():
    """Return the list of students from the JSON file.
    Returns an empty list if the file is missing or corrupted."""
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Warning: could not read data file. Starting with an empty list.")
        return []


def save_data(students):
    """Write the list of students to the JSON file."""
    try:
        with open(FILE, "w") as f:
            json.dump(students, f, indent=4)
    except OSError as e:
        print(f"Error: could not save data ({e}).")


def export_csv(students, subjects):
    """Export all students to a CSV file."""
    try:
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Roll No", "Name", "Age", "Course"] + subjects)
            for s in students:
                marks = [s["marks"].get(sub, 0) for sub in subjects]
                writer.writerow([s["roll_no"], s["name"], s["age"], s["course"]] + marks)
        print(f"Exported {len(students)} record(s) to {CSV_FILE}")
    except OSError as e:
        print(f"Error: could not export CSV ({e}).")
