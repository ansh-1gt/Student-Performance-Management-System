import student

marks = {}

def enter_marks():
    registration_id = input("Enter Registration ID: ")

    python = int(input("Enter Python Marks: "))
    mathematics = int(input("Enter Mathematics Marks: "))
    english = int(input("Enter English Marks: "))
    Physics = int(input("Enter Physics Marks: "))

    marks[registration_id] = {
        "Python": python,
        "Mathematics": mathematics,
        "English": english,
        "Physics": Physics 
    }

    print("\nMarks Added Successfully!")

def calculate_performance():
    registration_id  = input("Enter Registration ID: ")

    if registration_id not in marks:
        print("\nStudent Marks Not Found.")
        return

    student_marks = marks[registration_id]

    total = sum(student_marks.values())
    percentage = total / len(student_marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    print("\n========== STUDENT PERFORMANCE ==========")
    print("Registration ID:", registration_id)
    print("Total Marks:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)

def generate_report():
    registration_id = input("Enter Registration ID: ")

    #Find the student information
    student_info = None

    for s in student.students:
        if s["id"] == registration_id:
            student_info = s 
            break

    if student_info is None:
        print("\nStudent Not Found!")
        return

    #check is marks exist 
    if registration_id not in marks:
        print("\nMarks Not Found For This Student!")
        return

    student_marks = marks[registration_id]

    total = sum(student_marks.values())
    percentage = total / len(student_marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    print("\n===============================================")
    print("            STUDENT PERFORMANCE REPORT")
    print("\n===============================================")
    print("Registration ID:", student_info["id"])
    print("Name:", student_info["name"])
    print("Course:", student_info["course"])
    print("------------------------------------------------")
    print("Python:", student_marks["Python"])
    print("Mathematics:", student_marks["Mathematics"])
    print("English:", student_marks["English"])
    print("Physics:", student_marks["Physics"])
    print("------------------------------------------------")
    print("Total Marks:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)
    print("===============================================")

def class_statistics():
    if len(marks) == 0:
        print("\nNo Marks Available!")
        return

    total_students = len(marks)
    total_percentage = 0
    highest_percentage = -1
    lowest_percentage = 101

    for registration_id, student_marks in marks.items():
        total = sum(student_marks.values())
        percentage = total / len(student_marks)

        total_percentage += percentage

        if percentage > highest_percentage:
            highest_percentage = percentage

        if percentage < lowest_percentage:
            lowest_percentage = percentage

    average_percentage = total_percentage / total_students

    print("\n=================================================")
    print("            CLASS STATISTICS")
    print("=================================================")
    print("Students With Marks:", total_students)
    print("Average Percentage:", round(average_percentage, 2))
    print("Highest Percentage:", round(highest_percentage, 2))
    print("Lowest Percentage:", round(lowest_percentage, 2))
    print("=================================================")