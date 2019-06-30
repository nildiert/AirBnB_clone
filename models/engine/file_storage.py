#!/usr/bin/python3
""" FileStorage class """
import json
from models.base_model import BaseModel


class FileStorage():
    """ This is the FileStorage class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ all method that return objects"""
        return FileStorage.__objects

    def new(self, obj):
        """new method """
        FileStorage.__objects[str(obj.__class__.__name__ + "." + obj.id)] = obj

    def save(self):
        """save method"""
        tmp_dict = {}
        for key, item in FileStorage.__objects.items():
            tmp_dict.update({key: item.to_dict()})
        with open(FileStorage.__file_path, "w") as f:
            json.dump(tmp_dict, f)

    def reload(self):
        """ Reload method """
        dict2 = {}
        try:
            with open(FileStorage.__file_path, "r") as f:
                tmp_dict = json.load(f)
                for item in tmp_dict.values():
                    cls_name = item["__class__"]
                    del item["__class__"]
                    self.new(eval(cls_name)(**item))
        except:
            pass
