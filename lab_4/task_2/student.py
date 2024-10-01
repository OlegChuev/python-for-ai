class Student:
    """
    A class to represent a student.

    Attributes:
        id (int): The unique identifier for the student.
        last_name (str): The student's last name.
        first_name (str): The student's first name.
        patronymic (str): The student's patronymic (middle name).
        year_of_birth (int): The year the student was born.
        year_of_entering (int): The year the student entered the school/university.
    """

    def __init__(
        self, id, last_name, first_name, patronymic, year_of_birth, year_of_entering
    ):
        """
        Initialize a new Student instance.

        Args:
            id (int): The unique identifier for the student.
            last_name (str): The student's last name.
            first_name (str): The student's first name.
            patronymic (str): The student's patronymic (middle name).
            year_of_birth (int): The year the student was born.
            year_of_entering (int): The year the student entered the school/university.
        """
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.year_of_birth = year_of_birth
        self.year_of_entering = year_of_entering

    def __str__(self):
        """
        Return a string representation of the student.

        Returns:
            str: A formatted string with the student's full name, year of birth, and year of entering.
        """
        return f"{self.last_name} {self.first_name} {self.patronymic}, Born: {self.year_of_birth}, Entered: {self.year_of_entering}"

    @staticmethod
    def from_dict(data):
        """
        Create a Student instance from a dictionary.

        Args:
            data (dict): A dictionary with keys corresponding to the Student attributes.

        Returns:
            Student: An instance of the Student class.
        """
        # Ensure all required keys are in the dictionary and handle missing keys gracefully
        required_keys = {
            "id",
            "last_name",
            "first_name",
            "patronymic",
            "year_of_birth",
            "year_of_entering",
        }
        if not required_keys.issubset(data.keys()):
            raise ValueError("Dictionary missing one or more required keys")

        return Student(**data)

    def to_dict(self):
        """
        Convert the Student instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        return {
            "id": self.id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "patronymic": self.patronymic,
            "year_of_birth": self.year_of_birth,
            "year_of_entering": self.year_of_entering,
        }
