from student import Student


class BudgetStudent(Student):
    """
    A class to represent a budget student who receives a scholarship.

    Inherits from:
        Student: Base class representing a general student.

    Attributes:
        id (int): The unique identifier for the student.
        last_name (str): The student's last name.
        first_name (str): The student's first name.
        patronymic (str): The student's patronymic (middle name).
        year_of_birth (int): The year the student was born.
        year_of_entering (int): The year the student entered the institution.
        scholarship (float): The amount of the scholarship the student receives.
    """

    def __init__(
        self,
        id,
        last_name,
        first_name,
        patronymic,
        year_of_birth,
        year_of_entering,
        scholarship,
    ):
        """
        Initialize a new BudgetStudent instance.

        Args:
            id (int): The unique identifier for the student.
            last_name (str): The student's last name.
            first_name (str): The student's first name.
            patronymic (str): The student's patronymic (middle name).
            year_of_birth (int): The year the student was born.
            year_of_entering (int): The year the student entered the institution.
            scholarship (float): The amount of the scholarship the student receives.
        """
        super().__init__(
            id, last_name, first_name, patronymic, year_of_birth, year_of_entering
        )
        self.scholarship = scholarship

    def __str__(self):
        """
        Return a string representation of the budget student.

        Returns:
            str: A formatted string with the student's details and scholarship amount.
        """
        return super().__str__() + f", Scholarship: {self.scholarship}"

    @staticmethod
    def from_dict(data):
        """
        Create a BudgetStudent instance from a dictionary.

        Args:
            data (dict): A dictionary with keys corresponding to the BudgetStudent attributes.

        Returns:
            BudgetStudent: An instance of the BudgetStudent class.
        """
        # Ensure all required keys are present in the dictionary and handle missing keys gracefully
        required_keys = {
            "id",
            "last_name",
            "first_name",
            "patronymic",
            "year_of_birth",
            "year_of_entering",
            "scholarship",
        }
        if not required_keys.issubset(data.keys()):
            raise ValueError("Dictionary missing one or more required keys")

        return BudgetStudent(**data)

    def to_dict(self):
        """
        Convert the BudgetStudent instance to a dictionary.

        Returns:
            dict: A dictionary representation of the BudgetStudent instance.
        """
        data = super().to_dict()
        data["scholarship"] = self.scholarship
        return data
