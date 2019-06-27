#!/usr/bin/python3
""" BaseModel class """


class BaseModel():
    """ This is the BaseModel class """

    id = 0
    created_at = ""
    updated_at = ""

    def __init__(self, *args, **kwargs):
        """ Init method """
        pass

    def __str__(self):
        """ str method """
        pass

    def save(self):
        """ save method """
        pass

    def to_dict(self):
        """ to_dict method """
        pass
