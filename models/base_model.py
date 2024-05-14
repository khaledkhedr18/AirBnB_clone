#!/usr/bin/python3
""" This module defines the BaseModel class that defines
all common attributes/methods for other classes """


import datetime
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ the initialization method for the class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        """the save method for the class"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        the to_dict method for the class
        it will return a dictionary containing
        all the attributes and methods for the class
        """

        dictionary = self.__dict__
        dictionary["__class__"] = type(self).__name__
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        return dictionary

    def __str__(self):
        """
        the __str__ method for the class
        it will return a string containing
        all the attributes and methods for the class
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)
