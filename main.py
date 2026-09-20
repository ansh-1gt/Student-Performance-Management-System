import student
import marks

while True:
    print("\n===============================================")
    print("    Student Performance Management System")
    print("===============================================")

    print()
    print("1. Add Student")
    print("2. View all students")
    print("3. Search Students")
    print("4. Update Students")
    print("5. Delete Students")
    print("6. Enter/Update Marks")
    print("7. Calculate Performance")
    print("8. Generate Student Report")
    print("9. Class Statistics")
    print("10. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        student.add_student()
    elif choice == "2":
        student.view_students()
    elif choice == "3":
        student.search_student()
    elif choice == "4":
        student.update_student()
    elif choice == "5":
        student.delete_student()    
    elif choice == "6":
        marks.enter_marks()
    elif choice == "7":
        marks.calculate_performance()
    elif choice == "8":
        marks.generate_report()
    elif choice == "9":
        marks.class_statistics()
    elif choice == "10":
        print("\nThank You For Using The System!")
        break

    else:
        print("\nInvalid Choice Try Again.")