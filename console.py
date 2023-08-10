#!/usr/bin/python3
"""This program contains the entry point to the command line interface
For the AirBnB software
"""
import cmd
from models import storage, classes
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Entry point for the command interpreter"""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it (to the JSON file)
        and prints the id: $ create <class name>"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
