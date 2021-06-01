#!/usr/bin/python3
"""
Contains the definition of class Student
"""


class Student():
    """Definition of class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new instance of class Student

        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            age (int): Student's age
        """

        if isinstance(first_name, str):
            self.first_name = first_name
        if isinstance(last_name, str):
            self.last_name = last_name
        if isinstance(age, int):
            self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of Student instance"""

        return self.__dict__
