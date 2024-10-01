import json
import os
from student import Student
from budget_student import BudgetStudent
from discipline import Discipline
from teacher import Teacher
from group import Group


class Database:
    """
    A class to manage a database of students, budget students, disciplines, teachers, and groups.

    Attributes:
        file_path (str): The path to the JSON file where the database is stored.
        data (dict): The data loaded from the JSON file.
        students (dict): A dictionary mapping student IDs to Student instances.
        budget_students (dict): A dictionary mapping budget student IDs to BudgetStudent instances.
        disciplines (dict): A dictionary mapping discipline IDs to Discipline instances.
        teachers (dict): A dictionary mapping teacher IDs to Teacher instances.
        groups (dict): A dictionary mapping group IDs to Group instances.
    """

    def __init__(self, file_path: str):
        """
        Initialize the Database instance by loading data from the specified file.

        Args:
            file_path (str): The path to the JSON file where the database is stored.
        """
        self.file_path = file_path
        self.data = self.load_data()

        # Create a combined dictionary of students and budget students
        self.students = {
            s["id"]: Student.from_dict(s) for s in self.data.get("students", [])
        }
        # Merge budget students into the same dictionary
        self.students.update({
            s["id"]: BudgetStudent.from_dict(s) for s in self.data.get("budget_students", [])
        })

        # Create Disciplines
        self.disciplines = {
            d["id"]: Discipline.from_dict(d) for d in self.data["disciplines"]
        }

        # Create Teachers
        self.teachers = {
          t["id"]: Teacher.from_dict(t) for t in self.data["teachers"]
        }

        # Create Groups
        self.groups = {
          g["id"]: Group.from_dict(g) for g in self.data["groups"]
        }

    def load_data(self):
        """
        Load data from the JSON file. If the file does not exist or contains invalid JSON, initialize with an empty database.

        Returns:
            dict: The data loaded from the JSON file or an empty database if the file is missing or corrupted.
        """
        if not os.path.exists(self.file_path):
            print("Database file not found. Creating a new file...")
            self.save_data(
                {
                    "students": [],
                    "budget_students": [],
                    "disciplines": [],
                    "teachers": [],
                    "groups": [],
                }
            )
            return {
                "students": [],
                "budget_students": [],
                "disciplines": [],
                "teachers": [],
                "groups": [],
            }

        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(
                "Error decoding JSON from the database file. Initializing with an empty database."
            )
            return {
                "students": [],
                "budget_students": [],
                "disciplines": [],
                "teachers": [],
                "groups": [],
            }

    def save_data(self, data):
        """
        Save data to the JSON file.

        Args:
            data (dict): The data to be saved to the file.
        """
        try:
            with open(self.file_path, "w") as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error saving data to file: {e}")

    def print_groups(self):
        """
        Print all groups in the database.
        """
        for group in self.groups.values():
            print(group)

    def print_disciplines(self):
        """
        Print all disciplines in the database.
        """
        for discipline in self.disciplines.values():
            print(discipline)

    def print_teachers(self):
        """
        Print all teachers in the database.
        """
        for teacher in self.teachers.values():
            print(teacher)

    def find_group_by_number(self, group_number: str) -> Group:
        """Find and return a group by its group number."""
        for group in self.groups.values():
            if group.group_number == group_number:
                return group
        return None

    def find_disciplines_for_student(self, student, teachers):
        """
        Find all disciplines for a student by looking at the teachers who teach the subjects.
        For simplicity, we assume every student has access to all the teacher's disciplines.
        """
        disciplines = []
        for teacher in teachers.values():
            for discipline_id in teacher.discipline_ids:
                disciplines.append(self.disciplines[discipline_id])
        return disciplines