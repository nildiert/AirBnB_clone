#!/usr/bin/python3
""" Import cmd """
import cmd
from models.base_model import BaseModel
from models import storage
import sys
import inspect


class HBNBCommand(cmd.Cmd):
    """ This is the      console """
    prompt = "(hbnb) "

    def do_create(self, args):
        """ create method """
        if len(args) is 0:
            print("** class name missing **")
        else:
            arguments = args.split()
            if HBNBCommand.verifyclass(arguments[0]):
                new_object = eval(arguments[0])(arguments[1:])
                print(new_object.id)
                new_object.save()
            else:
                print("** class doesn't exist **'")

#        super().__init__(args)

    def do_show(self, args):
        """ show method """
        if len(args) is 0:
            print("** class name missing **")
        elif len(args) is 1:
            print("** instance id missing **")
        else:
            arguments = args.split()
            if HBNBCommand.verifyclass(arguments[0]):
                storage.reload()
                element = arguments[0] + "." + arguments[1]
                if element in list(storage.all().keys()):
                    print(BaseModel(storage.all()[element]))
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **'")

    def do_destroy(self, args):
        """ destroy method """
        if len(args) is 0:
            print("** class name missing **")
        elif len(args) is 1:
            print("** instance id missing **")
        else:
            arguments = args.split()
            if HBNBCommand.verifyclass(arguments[0]):
                storage.reload()
                print(storage.all())
                element = arguments[0] + "." + arguments[1]
                if element in list(storage.all().keys()):
                    del storage.all()[element]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **'")

    def do_all():
        """ all method """
        pass

    def do_update():
        """ update method """
        pass

    def do_EOF(self, *args):
        """ EOF method """
        print()
        return (True)

    def do_quit(self, *args):
        """ Quit command to exit the program \n"""
        return (True)

    def emptyline(self):
        pass

    def verifyclass(name_class):
        my_classes = [
            "Review", "BaseModel", "City", "State", "User", "Amenity", "Place"
        ]
        if name_class in my_classes:
            return True
        else:
            return False


if __name__ == '__main__':
    interpreter = HBNBCommand()
    interpreter.cmdloop()
