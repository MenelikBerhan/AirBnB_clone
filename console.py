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

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id: $ show <class name> <id>"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg.split()[0] in classes:
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        else:
            key = arg.split()[0] + "." + arg.split()[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change 
        into the JSON file) . Ex: $ destroy BaseModel 1234-1234-1234"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg.split()[0] in classes:
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        else:
            key = arg.split()[0] + "." + arg.split()[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the
        class name. Ex: $ all BaseModel or $ all"""
        if len(arg) == 0:
            for obj in storage.all().values():
                print(obj)
        elif arg in classes:
            for key, obj in storage.all().items():
                if arg in key:
                    print(obj)
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
