#!/usr/bin/python3
""" BaseModel class """
from uuid import uuid4
import datetime


class BaseModel():
    """ This is the BaseModel class """

    def __init__(self):
        """ Init method """
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        """ str method """
        name_class = str("[" + self.__class__.__name__ + "]")
        base_id = str("(" + self.id + ")")
        base_dict = str(self.__dict__)
        return (name_class + " " base_id + " " + base_dict)

    def save(self):
        """ save method """
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """ to_dict method """
