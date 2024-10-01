from database import Database
from budget_student import BudgetStudent

def interactive_shell():
    db = Database("data.json")

    while True:
        print("\nInteractive Shell")
        print("1. Print Group List")
        print("2. Print List of Disciplines")
        print("3. Print List of Teachers")
        print("4. Show Students in a Group")
        print("5. Show Students and Their Disciplines in a Group")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            db.print_groups()
        elif choice == "2":
            db.print_disciplines()
        elif choice == "3":
            db.print_teachers()
        elif choice == "4":
            group_number = input("Enter the group number: ")
            group = db.find_group_by_number(group_number)
            if group:
                students = group.get_students(db.students)
                print(f"Students in Group {group.group_number}:")
                for student in students:
                    print(student)
            else:
                print(f"Group {group_number} not found.")
        elif choice == "5":
            group_number = input("Enter the group number: ")
            group = db.find_group_by_number(group_number)
            if group:
                students = group.get_students(db.students)
                print(f"Students and their disciplines in Group {group.group_number}:")
                for student in students:
                    print(f"\nStudent: {student}")
                    print("Disciplines:")
                    if isinstance(student, BudgetStudent):
                        disciplines = db.find_disciplines_for_student(student, db.teachers)
                    else:
                        disciplines = db.find_disciplines_for_student(student, db.teachers)
                    for discipline in disciplines:
                        print(discipline)
            else:
                print(f"Group {group_number} not found.")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    interactive_shell()