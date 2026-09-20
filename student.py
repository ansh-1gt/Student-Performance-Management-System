students = []

def add_student():
    registration_id = input("Enter Registration ID: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")

    student = {
        "id": registration_id,
        "name": name,
        "course": course
    }

    students.append(student)

    print("\nStudent Added Successfully!")

def view_students():
    if len(students) == 0:
        print("\nNo Students Found.")
        return

    print("\n========== STUDENT LIST ==========")

    for student in students:
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("----------------------------------")


def search_student():
    registration_id = input("Enter Registration ID to Search: ")

    for student in students:
         if student["id"] == registration_id:
             print("\nStudent Found!")
             print("ID:", student["id"])
             print("Name:", student["name"])
             print("Course:", student["course"])
             return

    print("\nStudent Not Found.")

def update_student():
    registration_id = input("Enter Registration ID to Update: ")

    for student in students:
        if student["id"] == registration_id:
            print("\nStudent Found!")

            new_name = input("Enter New Student Name: ")
            new_course = input("Enter New Course: ")

            student["name"] = new_name
            student["course"] = new_course

            print("\nStudent Updated Successfully!")
            return

    print("\nStudent Not Found.")

def delete_student():
    registration_id = input("Enter Registration ID to Delete: ")

    for student in students:
        if student["id"] == registration_id:
            students.remove(student)

            print("\nStudent Deleted Successfully!")
            return

    print("\nStudent Not Found.")