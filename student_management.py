import json
import os

FILE_NAME = "students.json"


def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Error reading student records.")
        return []


def save_students(students):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)
    except OSError:
        print("Error saving student records.")


def add_student():
    students = load_students()

    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if any(s["id"] == student_id for s in students):
        print("Student ID already exists.")
        return

    name = input("Enter Student Name: ").strip()
    age_text = input("Enter Student Age: ").strip()
    course = input("Enter Course Name: ").strip()

    if not name or not course:
        print("Name and course cannot be empty.")
        return

    try:
        age = int(age_text)
        if age <= 0:
            print("Age must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid age.")
        return

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")


def view_students():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("-" * 30)
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])


def search_student():
    students = load_students()
    student_id = input("Enter Student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("Student Found:", student)
            return

    print("Student not found.")


def update_student():
    students = load_students()
    student_id = input("Enter Student ID to update: ").strip()

    for student in students:
        if student["id"] == student_id:
            name = input("Enter new name: ").strip()
            age_text = input("Enter new age: ").strip()
            course = input("Enter new course: ").strip()

            if not name or not course:
                print("Name and course cannot be empty.")
                return

            try:
                age = int(age_text)
                if age <= 0:
                    print("Age must be greater than zero.")
                    return
            except ValueError:
                print("Please enter a valid age.")
                return

            student["name"] = name
            student["age"] = age
            student["course"] = course

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    students = load_students()
    student_id = input("Enter Student ID to delete: ").strip()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()