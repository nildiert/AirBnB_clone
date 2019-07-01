#!/usr/bin/python3
""" BaseModel class """
from uuid import uuid4
import datetime
import models


class BaseModel():
    """ This is the BaseModel class """

    def __init__(self, *args, **kwargs):
        """ Init method """
        '''
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ str method """
        name_class = str("[" + self.__class__.__name__ + "]")
        base_id = str("(" + self.id + ")")
        base_dict = str(self.__dict__)
        return (name_class + " " + base_id + " " + base_dict)

    def save(self):
        """ save method """
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ to_dict method WITH A COPY to AVOID BE ALTERED"""
        tmpdict = self.__dict__.copy()
        tmpdict["__class__"] = self.__class__.__name__
        tmpdict["created_at"] = self.created_at.isoformat()
        tmpdict["updated_at"] = self.updated_at.isoformat()
        return tmpdict
