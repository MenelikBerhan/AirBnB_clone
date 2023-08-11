#!/usr/bin/python3
"""This program contains the entry point to the command line interface
For the AirBnB software

Attributes:
    allClasses (list): list of all classes
    classes (set): set of all classes

Usage:
    $ ./console.py
    (hbnb) help
    (hbnb) quit
    (hbnb) EOF
    $ echo "help" | ./console.py
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
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id: $ show <class name> <id>"""
        if not self.errorCheck(arg):
            key = arg.split()[0] + "." + arg.split()[1]
            print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change
         into the JSON file) . Ex: $ destroy BaseModel 1234-1234-1234"""
        if not self.errorCheck(arg):
            key = arg.split()[0] + "." + arg.split()[1]
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
         the class name. Ex: $ all BaseModel or $ all"""
        if len(arg) == 0:
            objs = [str(obj) for obj in storage.all().values()]
            print(objs)
        elif arg in classes:
            objs = [str(obj)
                    for key, obj in storage.all().items() if arg in key]
            print(objs)
        else:
            print("** class doesn't exist **")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything"""
        pass

    @staticmethod
    def errorCheck(arg):
        if len(arg) == 0:
            print("** class name missing **")
            return (1)
        if arg.split()[0] not in classes:
            print("** class doesn't exist **")
            return (1)
        if len(arg.split()) == 1:
            print("** instance id missing **")
            return (1)
        if (arg.split()[0] + "." + arg.split()[1]) not in storage.all():
            print("** no instance found **")
            return (1)
        return (0)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
