#!/usr/bin/python3
"""This module defines the BaseModel class"""
import datetime
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ the initialization method for the class"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()

        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__.update(kwargs)
        self.save()

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
