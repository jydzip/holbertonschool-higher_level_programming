#!/usr/bin/python3

import pickle


class CustomObject:
    """
        Initializes the CustomObject with name, age, and student status.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
            Displays the attributes of the object.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        '''Serialize the instance itself'''
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        # Deserialize and return an instance of CustomObject
        with open(filename, 'rb') as file:
            return pickle.load(file)
