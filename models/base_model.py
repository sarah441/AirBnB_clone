#!/usr/bin/python3

"""
Create basemodel the start point for the project
"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
    Base class to create id and update info of new user
    """

    def __init__(self):
        """
        instatiates a user
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        updates and save
        """
        self.updated_at = datetime.now()

    def __str__(self):
        """modify ro string"""
        forma = "[{}] ({}) {}"
        return forma.format(
                type(self).__name__,
                self.id,
                self.__dict__)


    def to_dict(self):
        """
        returns a dic with all keys/values
        """
        dict = {**self.__dict__}
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()

        return dict
