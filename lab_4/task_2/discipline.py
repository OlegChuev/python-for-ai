class Discipline:
    """
    A class to represent a discipline or course.

    Attributes:
        id (int): The unique identifier for the discipline.
        name (str): The name of the discipline.
        number_of_credits (int): The number of credits associated with the discipline.
        semester_of_teaching (int): The semester during which the discipline is taught.
    """

    def __init__(self, id, name, number_of_credits, semester_of_teaching):
        """
        Initialize a new Discipline instance.

        Args:
            id (int): The unique identifier for the discipline.
            name (str): The name of the discipline.
            number_of_credits (int): The number of credits associated with the discipline.
            semester_of_teaching (int): The semester during which the discipline is taught.
        """
        self.id = id
        self.name = name
        self.number_of_credits = number_of_credits
        self.semester_of_teaching = semester_of_teaching

    def __str__(self):
        """
        Return a string representation of the discipline.

        Returns:
            str: A formatted string with the discipline's name, number of credits, and semester of teaching.
        """
        return f"{self.name}, Credits: {self.number_of_credits}, Semester: {self.semester_of_teaching}"

    @staticmethod
    def from_dict(data):
        """
        Create a Discipline instance from a dictionary.

        Args:
            data (dict): A dictionary with keys corresponding to the Discipline attributes.

        Returns:
            Discipline: An instance of the Discipline class.
        """
        # Ensure all required keys are present in the dictionary and handle missing keys gracefully
        required_keys = {"id", "name", "number_of_credits", "semester_of_teaching"}
        if not required_keys.issubset(data.keys()):
            raise ValueError("Dictionary missing one or more required keys")

        return Discipline(**data)

    def to_dict(self):
        """
        Convert the Discipline instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Discipline instance.
        """
        return {
            "id": self.id,
            "name": self.name,
            "number_of_credits": self.number_of_credits,
            "semester_of_teaching": self.semester_of_teaching,
        }
