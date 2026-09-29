# Student Performance Management System

## Project Description

The **Student Performance Management System** is a menu-driven Python application developed to manage student information and academic performance.

The project allows users to add, view, search, update, and delete student records. It also provides options to enter marks, calculate student performance, generate a student performance report, and view class statistics.

The project is developed using basic Python concepts such as **variables, lists, dictionaries, functions, loops, conditional statements, modules, user input, and calculations**.

## Features

The system provides the following options:

1. **Add Student** – Add a new student using registration ID, name, and course.
2. **View All Students** – Display all stored student records.
3. **Search Student** – Search for a student using their registration ID.
4. **Update Student** – Update a student's name and course.
5. **Delete Student** – Delete a student record using their registration ID.
6. **Enter/Update Marks** – Enter marks for Python, Mathematics, English, and Physics.
7. **Calculate Performance** – Calculate total marks, percentage, and grade.
8. **Generate Student Report** – Display student information along with subject-wise marks and performance.
9. **Class Statistics** – Display the number of students with marks, average percentage, highest percentage, and lowest percentage.
10. **Exit** – Exit the application.

## Technologies Used

* **Python**
* Python built-in data structures:

  * Lists
  * Dictionaries
* Functions
* Loops
* Conditional statements
* User input
* Python modules

## Project Structure

```text
Student Performance Management System/
│
├── main.py
├── student.py
├── marks.py
├── README.md
└── .gitignore
```

### File Description

**main.py**

Contains the main menu of the application and connects the student management and marks management functions.

**student.py**

Contains functions for managing student records, including adding, viewing, searching, updating, and deleting students.

**marks.py**

Contains functions for entering marks, calculating performance, generating student reports, and calculating class statistics.

**README.md**

Contains information about the project, its features, structure, and instructions for running it.

**.gitignore**

Contains Python files and folders that should not be included in the Git repository, such as Python cache files.

## Subjects

The system currently accepts marks for four subjects:

* Python
* Mathematics
* English
* Physics

## Grading System

The performance is calculated using the average marks entered for the four subjects.

| Percentage   | Grade |
| ------------ | ----- |
| 90 and above | A+    |
| 80–89        | A     |
| 70–79        | B     |
| 60–69        | C     |
| 50–59        | D     |
| Below 50     | F     |

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

You can check the installation by running:

```bash
python --version
```

### 2. Open the Project Folder

Open the project folder in a terminal or in an editor such as Visual Studio Code.

### 3. Run the Program

Run the following command:

```bash
python main.py
```

### 4. Use the Menu

After running the program, the main menu will appear. Enter the number corresponding to the operation you want to perform.

## Example Menu

```text
===============================================
    Student Performance Management System
===============================================

1. Add Student
2. View all students
3. Search Students
4. Update Students
5. Delete Students
6. Enter/Update Marks
7. Calculate Performance
8. Generate Student Report
9. Class Statistics
10. Exit
```

## Concepts Used

This project was developed to practice basic Python programming concepts, including:

* Variables
* Lists
* Dictionaries
* Functions
* `for` loops
* `while` loops
* `if-elif-else` conditions
* User input
* Modules
* Basic calculations

## Limitations

* The student and marks data are stored in memory while the program is running.
* The project does not currently use a database.
* Data is not permanently saved after the program is closed.

## Purpose

The main purpose of this project is to practice Python programming fundamentals by building a simple menu-driven application for managing student information and academic performance.
