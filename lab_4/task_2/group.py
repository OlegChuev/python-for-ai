from student import Student
from budget_student import BudgetStudent


class Group:
    """
    A class to represent a group of students.

    Attributes:
        id (int): The unique identifier for the group.
        group_number (str): The group's number or name.
        student_ids (list of str): List of student IDs in the group.
    """

    def __init__(self, id, group_number, student_ids):
        """
        Initialize a new Group instance.

        Args:
            id (int): The unique identifier for the group.
            group_number (str): The group's number or name.
            student_ids (list of str): List of student IDs in the group.
        """
        self.id = id
        self.group_number = group_number
        self.student_ids = student_ids

    def get_students(self, students_db):
        """
        Retrieve the list of Student and BudgetStudent objects for this group using their IDs.

        Args:
            students_db (dict): A dictionary mapping student IDs to Student or BudgetStudent objects.

        Returns:
            list: A list of Student or BudgetStudent objects corresponding to the IDs in the group.
        """
        return [students_db[s_id] for s_id in self.student_ids]

    def __str__(self):
        """
        Return a string representation of the group.

        Returns:
            str: A formatted string with the group's number and a comma-separated list of student IDs.
        """
        return f"Group {self.group_number}, Students: {', '.join(self.student_ids)}"

    @staticmethod
    def from_dict(data):
        """
        Create a Group instance from a dictionary.

        Args:
            data (dict): A dictionary with keys corresponding to the Group attributes.

        Returns:
            Group: An instance of the Group class.
        """
        # Ensure all required keys are present in the dictionary and handle missing keys gracefully
        required_keys = {"id", "group_number", "student_ids"}
        if not required_keys.issubset(data.keys()):
            raise ValueError("Dictionary missing one or more required keys")

        return Group(
            data["id"],
            data["group_number"],
            data["student_ids"],
        )

    def to_dict(self):
        """
        Convert the Group instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Group instance.
        """
        return {
            "id": self.id,
            "group_number": self.group_number,
            "student_ids": self.student_ids,
        }
