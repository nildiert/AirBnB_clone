#!/usr/bin/python3
""" FileStorage class """
import json

class FileStorage():
    """ This is the FileStorage class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ all method """
        return self.__objects

    def new(self, obj):
        """ new method """
        self.__objects[str(obj.__class__.__name__ + "." + obj.id)] = obj.to_dict()

    def save(self):
        """ Save method """
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """ Reload method """
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except:
            pass
