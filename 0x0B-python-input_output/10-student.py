#!/usr/bin/python3
"""
Contains the definition of the class Student
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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of Student instance

        Args:
            attrs (list): a list of attributes to be retrieved
        """

        if isinstance(attrs, list):
            return {a: self.__dict__.get(a) for a in attrs if a in
                    self.__dict__.keys()}
        return self.__dict__
