#!usr/bin/python3
""" This module defines the BaseModel class that defines all common attributes/methods for other classes """


import datetime
import uuid

class BaseModel:
    def __init__(self, id=None, createdat=None, updatedat=None):
        """ the initialization method for the class"""
        self.id = str(uuid.uuid4())
        self.createdat = datetime.datetime.now()
        self.save()

    def save(self):
        """ the save method for the class"""
        self.updatedat = datetime.datetime.now()

    def  to_dict(self):
        """
        the to_dict method for the class
        it will return a dictionary containing
        all the attributes and methods for the class
        """

        dictionary = self.__dict__
        dictionary.update({'__class__' : self.__class__.__name__})
        dictionary['createdat'] = self.createdat.isoformat()
        dictionary['updatedat'] = self.updatedat.isoformat()
        return dictionary


    def __str__(self):
        """
        the __str__ method for the class
        it will return a string containing
        all the attributes and methods for the class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    