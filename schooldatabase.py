# School Database Simulation

students = []
teachers = []
homeroom_teachers = []

def show_main_menu():
    print("\nAvailable commands:")
    print("1. create")
    print("2. manage")
    print("3. end")

def show_create_menu():
    print("\nUser types to create:")
    print("1. student")
    print("2. teacher")
    print("3. homeroom teacher")
    print("4. end")

def show_manage_menu():
    print("\nManage options:")
    print("1. class")
    print("2. student")
    print("3. teacher")
    print("4. homeroom teacher")
    print("5. end")

def create_user():
    while True:
        show_create_menu()
        choice = input("Enter user type to create: ").strip().lower()
        if choice == "student":
            first = input("Student's first name: ").strip()
            last = input("Student's last name: ").strip()
            class_name = input("Class name (e.g., 3C): ").strip()
            students.append({"first": first, "last": last, "class": class_name})
            print(f"Student {first} {last} added to class {class_name}.")
        elif choice == "teacher":
            first = input("Teacher's first name: ").strip()
            last = input("Teacher's last name: ").strip()
            subject = input("Subject taught: ").strip()
            classes = []
            print("Enter class names taught (empty line to finish):")
            while True:
                class_name = input("Class name: ").strip()
                if class_name == "":
                    break
                classes.append(class_name)
            teachers.append({"first": first, "last": last, "subject": subject, "classes": classes})
            print(f"Teacher {first} {last} added, teaches {subject} to classes: {', '.join(classes)}.")
        elif choice == "homeroom teacher":
            first = input("Homeroom teacher's first name: ").strip()
            last = input("Homeroom teacher's last name: ").strip()
            class_name = input("Class led: ").strip()
            homeroom_teachers.append({"first": first, "last": last, "class": class_name})
            print(f"Homeroom teacher {first} {last} leads class {class_name}.")
        elif choice == "end":
            break
        else:
            print("Invalid option. Try again.")

def manage_users():
    while True:
        show_manage_menu()
        choice = input("Enter option to manage: ").strip().lower()
        if choice == "class":
            class_name = input("Enter class name: ").strip()
            class_students = [s for s in students if s["class"] == class_name]
            hr_teacher = next((t for t in homeroom_teachers if t["class"] == class_name), None)
            print(f"\nStudents in class {class_name}:")
            for s in class_students:
                print(f"- {s['first']} {s['last']}")
            if hr_teacher:
                print(f"Homeroom teacher: {hr_teacher['first']} {hr_teacher['last']}")
            else:
                print("No homeroom teacher assigned.")
        elif choice == "student":
            first = input("Student's first name: ").strip()
            last = input("Student's last name: ").strip()
            student = next((s for s in students if s["first"] == first and s["last"] == last), None)
            if not student:
                print("Student not found.")
                continue
            print(f"\n{first} {last} attends class: {student['class']}")
            print("Teachers for this class:")
            for t in teachers:
                if student["class"] in t["classes"]:
                    print(f"- {t['first']} {t['last']} ({t['subject']})")
        elif choice == "teacher":
            first = input("Teacher's first name: ").strip()
            last = input("Teacher's last name: ").strip()
            teacher = next((t for t in teachers if t["first"] == first and t["last"] == last), None)
            if not teacher:
                print("Teacher not found.")
                continue
            print(f"\n{first} {last} teaches classes: {', '.join(teacher['classes'])}")
        elif choice == "homeroom teacher":
            first = input("Homeroom teacher's first name: ").strip()
            last = input("Homeroom teacher's last name: ").strip()
            hr_teacher = next((t for t in homeroom_teachers if t["first"] == first and t["last"] == last), None)
            if not hr_teacher:
                print("Homeroom teacher not found.")
                continue
            class_name = hr_teacher["class"]
            class_students = [s for s in students if s["class"] == class_name]
            print(f"\nStudents led by {first} {last} in class {class_name}:")
            for s in class_students:
                print(f"- {s['first']} {s['last']}")
        elif choice == "end":
            break
        else:
            print("Invalid option. Try again.")

def main():
    print("Welcome to the School Database!")
    while True:
        show_main_menu()
        command = input("Enter command: ").strip().lower()
        if command == "create":
            create_user()
        elif command == "manage":
            manage_users()
        elif command == "end":
            print("Exiting program.")
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()