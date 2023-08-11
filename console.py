#!/usr/bin/python3
"""This program contains the entry point to the command line interface
For the AirBnB software

Attributes:
    classes (set): set of all class names

Usage:
    $ ./console.py
    (hbnb) help
    (hbnb) quit
    (hbnb) EOF
    $ echo "help" | ./console.py
"""
import cmd
from models import storage, class_dict
from importlib import import_module

classes = set(class_dict.keys())


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
            module = import_module(f"models.{class_dict[arg]}")
            new_instance = getattr(module, arg)()
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

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
         updating attribute (save the change into the JSON file).
         Ex: $ update BaseModel 1234-1234-1234 email

        Usage: update <class name> <id> <attribute name> '<attribute value>'
        """
        from shlex import split
        if self.errorCheck(arg):
            return
        args = split(arg)
        if not args[2]:
            print("** attribute name missing **")
        elif not args[3]:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            obj = storage.all()[key]
            if hasattr(obj, args[2]):
                attr_type = type(getattr(obj, args[2]))
                setattr(obj, args[2], attr_type(args[3]))
            else:
                setattr(obj, args[2], args[3])
            storage.save()

    def default(self, line):
        """Called for the following commands:
        <class name>.all()
        <class name>.count()
        <class name>.show(<id>)
        <class name>.destroy(<id>)
        <class name>.update(<id>, <attribute name>, <attribute value>)  
        """
        cmdComm = line.split(".")
        if len(cmdComm) == 2:
            command = cmdComm[1].split("(")
            if command[0] == "all":
                self.do_all(cmdComm[0])
            if command[0] == "count":
                objs = [obj for key, obj in storage.all().items()
                        if cmdComm[0] in key]
                print(len(objs))

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
