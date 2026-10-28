# Student Record System

A menu-driven command-line application in Python to manage student records,
with persistent storage in a JSON file.

## Features
- Add, view, search, update and delete student records
- Input validation (unique roll number, valid name, age and marks range)
- Automatic total, percentage and grade calculation
- Sort by name, roll number or total marks
- Class report (average, topper, students above 75%)
- Data saved in `students.json`, export to CSV

## Project structure
| File | Purpose |
|------|---------|
| `main.py` | Menu and program flow |
| `student.py` | Validation and student operations |
| `storage.py` | JSON load/save and CSV export |

## How to run
```
python main.py
```
Requires Python 3.8+. No external libraries needed.

## Concepts used
Functions, dictionaries and lists, file handling (JSON, CSV), exception
handling, input validation, modular programming, lambda and sorting.

## Future improvements
SQLite database, Flask web interface, login for admin/teacher.
