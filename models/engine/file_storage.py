#!/usr/bin/python3
""" FileStorage class """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        obj_to_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_to_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as f:
            json.dump(obj_to_dict, f)

    def reload(self):
        """ Reload method """
        try:
            with open(FileStorage.__file_path, "r") as f:
                tmp_dict = json.load(f)
            for item in tmp_dict.values():
                cls_name = item["__class__"]
                del item["__class__"]
                self.new(eval(cls_name)(**item))
        except:
            pass
