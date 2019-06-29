#!/usr/bin/python3
""" Import cmd """
import cmd
from models.base_model import BaseModel
import sys
import inspect


class HBNBCommand(cmd.Cmd):
    """ This is the      console """
    prompt = "(hbnb) "

    __file_path = None
    __objects = None

    def do_create(self, args):
        """ create method """
        my_classes = [
            "Review", "BaseModel", "City", "State", "User", "Amenity", "Place"
        ]
        if len(args) is 0:
            print("** class name missing **")
        else:
            arguments = args.split()
            if arguments[0] in my_classes:
                print("Se va a crear la clase {}".format(arguments[0]))
            else:
                print("** class doesn't exist **'")

#        super().__init__(args)

    def show():
        """ show method """
        pass

    def destroy():
        """ destroy method """
        pass

    def do_all():
        """ all method """
        pass

    def do_update():
        """ update method """
        pass

    def do_EOF(self, *args):
        """ EOF method """
        return (True)

    def do_quit(self, *args):
        """ Quit command to exit the program \n"""
        return (True)

    def emptyline(self):
        pass


if __name__ == '__main__':
    interpreter = HBNBCommand()
    interpreter.cmdloop()
