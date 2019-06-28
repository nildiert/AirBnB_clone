#!/usr/bin/python3
""" Import cmd """
import cmd


class HBNBCommand(cmd.Cmd):
    """ This is the      console """
    prompt = "(hbnb) "

    __file_path = None
    __objects = None

    def create():
        """ create method """
        pass

    def show():
        """ show method """
        pass

    def destroy():
        """ destroy method """
        pass

    def all():
        """ all method """
        pass

    def update():
        """ update method """
        pass

    def do_EOF(self, args):
        """ EOF method """
        return (True)

    def do_quit(self, args):
        """ Quit command to exit the program \n"""
        return (True)

    def emptyline(self):
        pass


if __name__ == '__main__':
    interpreter = HBNBCommand()
    interpreter.cmdloop()
