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
        if not self.errorCheck(arg):
            key = arg.split()[0] + "." + arg.split()[1]
            print(storage.all()[key])

    def do_destroy(self, arg):
        if not self.errorCheck(arg):
            key = arg.split()[0] + "." + arg.split()[1]
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
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
        from shlex import split
        if self.errorCheck(arg):
            return
        args = split(arg)
        if len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            obj = storage.all()[key]
            if hasattr(obj, args[2]):
                attr_type = type(getattr(obj, args[2]))
                setattr(obj, args[2], attr_type(args[3]))
            else:
                setattr(obj, args[2], args[3])
            obj.save()

    def help_create(self):
        print("$ create <class name>",
              "Create a new instance of a class", sep="\n", end='')

    def help_show(self):
        print("$ show <class name> <id>",
              "Prints the string representation of an instance",
              sep="\n", end='')

    def help_destroy(self):
        print("$ destroy <class name> <id>",
              "Deletes an instance based on the class name and id",
              sep="\n", end='')

    def help_all(self):
        print("$ all [<class name>]",
              "Prints all string representations of all instances",
              sep="\n", end='')

    def help_update(self):
        print("$ update <class name> <id> <attribute name> '<value>'",
              "Updates an instance based on the class name and id",
              sep="\n", end='')

    def default(self, line):
        """Called for the following commands:
        <class name>.all()
        <class name>.count()
        <class name>.show(<id>)
        <class name>.destroy(<id>)
        <class name>.update(<id>, <attribute name>, <attribute value>)
        """
        from re import compile
        from ast import literal_eval
        rx = compile(r'([^\.]+)(.*)$')
        cmdComm = rx.match(line).groups()
        if len(cmdComm) == 2 and cmdComm[1]:
            command = cmdComm[1][1:].split("(")
            if command[0] == "all":
                self.do_all(cmdComm[0])
            elif command[0] == "count":
                if cmdComm[0] not in classes:
                    print("** class doesn't exist **")
                    return
                objs = [obj for key, obj in storage.all().items()
                        if cmdComm[0] in key]
                print(len(objs))
            elif command[0] == "show":
                id = command[1][:-1].strip("\"")
                self.do_show(f"{cmdComm[0]} {id}")
            elif command[0] == "destroy":
                id = command[1][:-1].strip("\"")
                self.do_destroy(f"{cmdComm[0]} {id}")
            elif command[0] == "update":
                if cmdComm[0] not in classes:
                    print("** class doesn't exist **")
                    return
                rx = compile(r'([^,]+)(?:,\s*(.*))?$')
                args = rx.match(command[1][:-1])
                if not args:
                    print("** instance id missing **")
                    return
                args = args.groups()
                id = args[0].strip("\"")
                if (cmdComm[0] + "." + id) not in storage.all():
                    print("** no instance found **")
                    return
                if not args[1]:
                    print("** attribute name missing **")
                    return
                attrs = args[1]
                if attrs.startswith('{') and attrs.endswith('}'):
                    attrs = literal_eval(attrs)
                    for attr, value in attrs.items():
                        self.do_update(f"{cmdComm[0]} {id} {attr} {value}")
                else:
                    args = attrs.split(",")
                    if len(args) < 2:
                        print("** value missing **")
                        return
                    attr = args[0].strip().strip("\"")
                    value = args[1].strip()
                    self.do_update(f"{cmdComm[0]} {id} {attr} {value}")
            else:
                return super().default(line)
        else:
            return super().default(line)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
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
