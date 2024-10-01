from discipline import Discipline


class Teacher:
    """
    A class to represent a teacher.

    Attributes:
        id (int): The unique identifier for the teacher.
        last_name (str): The teacher's last name.
        first_name (str): The teacher's first name.
        patronymic (str): The teacher's patronymic (middle name).
        year_of_birth (int): The year the teacher was born.
        teaching_experience (int): The number of years the teacher has been teaching.
        discipline_ids (list of int): List of discipline IDs that the teacher is responsible for.
    """

    def __init__(
        self,
        id,
        last_name,
        first_name,
        patronymic,
        year_of_birth,
        teaching_experience,
        discipline_ids,
    ):
        """
        Initialize a new Teacher instance.

        Args:
            id (int): The unique identifier for the teacher.
            last_name (str): The teacher's last name.
            first_name (str): The teacher's first name.
            patronymic (str): The teacher's patronymic (middle name).
            year_of_birth (int): The year the teacher was born.
            teaching_experience (int): The number of years the teacher has been teaching.
            discipline_ids (list of int): List of discipline IDs that the teacher is responsible for.
        """
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.year_of_birth = year_of_birth
        self.teaching_experience = teaching_experience
        self.discipline_ids = discipline_ids

    def total_subject(self, disciplines):
        """
        Calculate the total credits for the disciplines the teacher is responsible for.

        Args:
            disciplines (dict): A dictionary where the key is discipline ID and the value is a Discipline instance.

        Returns:
            tuple: A tuple containing:
                - A list of string representations of the disciplines.
                - The total number of credits for these disciplines.
        """
        total_credits = sum(
            disciplines[d_id].number_of_credits for d_id in self.discipline_ids
        )
        return [str(disciplines[d_id]) for d_id in self.discipline_ids], total_credits

    def __str__(self):
        """
        Return a string representation of the teacher.

        Returns:
            str: A formatted string with the teacher's full name, year of birth, and teaching experience.
        """
        return f"{self.last_name} {self.first_name} {self.patronymic}, Born: {self.year_of_birth}, Experience: {self.teaching_experience} years"

    @staticmethod
    def from_dict(data):
        """
        Create a Teacher instance from a dictionary.

        Args:
            data (dict): A dictionary with keys corresponding to the Teacher attributes.

        Returns:
            Teacher: An instance of the Teacher class.
        """
        required_keys = {
            "id",
            "last_name",
            "first_name",
            "patronymic",
            "year_of_birth",
            "teaching_experience",
            "discipline_ids",
        }
        if not required_keys.issubset(data.keys()):
            raise ValueError("Dictionary missing one or more required keys")

        return Teacher(
            data["id"],
            data["last_name"],
            data["first_name"],
            data["patronymic"],
            data["year_of_birth"],
            data["teaching_experience"],
            data["discipline_ids"],
        )

    def to_dict(self):
        """
        Convert the Teacher instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Teacher instance.
        """
        return {
            "id": self.id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "patronymic": self.patronymic,
            "year_of_birth": self.year_of_birth,
            "teaching_experience": self.teaching_experience,
            "discipline_ids": self.discipline_ids,
        }
