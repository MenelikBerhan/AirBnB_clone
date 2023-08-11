#!/usr/bin/python3
"""Contains the `BaseModel` class"""
from datetime import datetime
from uuid import uuid4
from . import storage


class BaseModel():
    """A base class that defines common attributes and methods
    for other classes.
    """

    def __init__(self, *args, **kwargs):
        """Creates a `BaseModel` instance object"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    self.__setattr__(key, datetime.fromisoformat(value))
                elif key != '__class__':
                    self.__setattr__(key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """`str`: returns a fancier string representation"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """Updates `updated_at` instance attribute with the current datetime,
        and saves the changes in storage"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """`dict`: returns a dictionary containing all keys/values of
        `__dict__` of the instance"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return (dict_copy)
