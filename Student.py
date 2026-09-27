student_grades = {}

def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with grade {grade}")

def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} is updated with {grade}")
    else:
        print(f"{name} not found")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} is deleted")
    else:
        print(f"{name} not found")

def view_student():
    print(student_grades)


Action = input("Enter what do you want to do:\n1. Add\n2. Update\n3. Delete\n4. View\n")

if Action == "Add":
    name = input("Enter the Name: ")
    grade = input("Enter the Grade: ")
    add_student(name, grade)

elif Action == "Update":
    name = input("Enter the Name: ")
    grade = input("Enter the Grade: ")
    update_student(name, grade)

elif Action == "Delete":
    name = input("Enter the Name: ")
    delete_student(name)

elif Action == "View":
    view_student()

else:
    print("Invalid Action")