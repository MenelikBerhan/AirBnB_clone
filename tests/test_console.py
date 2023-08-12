#!/usr/bin/python3
"""Contains test cases for the command line interface of the AirBnB project"""
import os
import pycodestyle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestConsole(TestCase):
    """Suite of test for the console"""

    def setUp(self):
        """Function empties file.json"""
        FileStorage._FileStorage__objects = {}
        FileStorage().save()

    def tearDown(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_create(self):
        """Test all variations of the create command"""
        storage = FileStorage()
        storage.reload()
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        # Help message
        output = "$ create <class name>\n" \
            "Create a new instance of a class"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(f.getvalue().strip(), output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? create")
            self.assertEqual(f.getvalue().strip(), output)
        # Create a new instance of a class
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            self.assertRegex(f.getvalue(), opt)
        # Error handling
        output = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), output)
        output = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(f.getvalue(), output)

    def test_show(self):
        """Test all variations of the show command"""
        # Help message
        output = "$ show <class name> <id>\n" \
            "Prints the string representation of an instance"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(f.getvalue().strip(), output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? show")
            self.assertEqual(f.getvalue().strip(), output)
        # Testing show command with an actual instance
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        uid = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {uid}")
            self.assertIn(uid, f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show({uid})")
            self.assertIn(uid, f.getvalue())
        # Error handling main commands
        output = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue(), output)
        output = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            self.assertEqual(f.getvalue(), output)
        output = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(f.getvalue(), output)
        output = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1234")
            self.assertEqual(f.getvalue(), output)
        # Error handling class based commands
        output = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.show()")
            self.assertEqual(f.getvalue(), output)
        output = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
            self.assertEqual(f.getvalue(), output)
        output = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(1234)")
            self.assertEqual(f.getvalue(), output)

    def test_destroy(self):
        """Test all variations of the destroy command"""
        # Help message
        output = "$ destroy <class name> <id>\n" \
            "Deletes an instance based on the class name and id"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(f.getvalue().strip(), output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? destroy")
            self.assertEqual(f.getvalue().strip(), output)
        # Testing destroy command with an actual instance
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        uid = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Place {uid}")
            HBNBCommand().onecmd(f"show Place {uid}")
            output = "** no instance found **\n"
            self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        uid = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.destroy({uid})")
            HBNBCommand().onecmd(f"Amenity.show({uid})")
            output = "** no instance found **\n"
            self.assertEqual(f.getvalue(), output)
        # Error handling main commands
        output = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue(), output)
        output = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            self.assertEqual(f.getvalue(), output)
        output = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue(), output)
        output = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1234")
            self.assertEqual(f.getvalue(), output)
        # Error handling class based commands
        output = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.destroy()")
            self.assertEqual(f.getvalue(), output)
        output = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy()")
            self.assertEqual(f.getvalue(), output)
        output = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy(1234)")
            self.assertEqual(f.getvalue(), output)

    def test_all(self):
        """Test all variations of the all command"""
        # Help message
        output = "$ all [<class name>]\n" \
            "Prints all string representations of all instances"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(f.getvalue().strip(), output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? all")
            self.assertEqual(f.getvalue().strip(), output)
        # Testing all command with an actual instance
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        uid = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertIn(uid, f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all City")
            self.assertIn(uid, f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
            self.assertIn(uid, f.getvalue())
        # Error handling main commands
        output = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            self.assertEqual(f.getvalue(), output)
        # Error handling class based commands
        output = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.all()")
            self.assertEqual(f.getvalue(), output)

    def test_update(self):
        """Test all variations of the update command"""
        # Help message
        output = "$ update <class name> <id> <attribute name> '<value>'\n" \
            "Updates an instance based on the class name and id"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(f.getvalue().strip(), output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? update")
            self.assertEqual(f.getvalue().strip(), output)
        # Testing update command with an actual instance
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        uid = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {uid} first_name 'Betty'")
            HBNBCommand().onecmd(f"show User {uid}")
            self.assertIn("'first_name': 'Betty'", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update({uid}, first_name, 'Bob')")
            HBNBCommand().onecmd(f"User.show({uid})")
            self.assertIn("'first_name': 'Bob'", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f"User.update({uid}, {{'first_name': 'Tunde'}})")
            HBNBCommand().onecmd(f"User.show({uid})")
            self.assertIn("'first_name': 'Tunde'", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f"User.update({uid}, first_name, Wale, last_name, Tunde)")
            HBNBCommand().onecmd(f"User.show({uid})")
            self.assertIn("'first_name': 'Wale'", f.getvalue())
            self.assertNotIn("'last_name': 'Tunde'", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f"update User {uid} first_name Tunde last_name Wale")
            HBNBCommand().onecmd(f"show User {uid}")
            self.assertIn("'first_name': 'Tunde'", f.getvalue())
            self.assertNotIn("'last_name': 'Wale'", f.getvalue())
        # Error handling main commands
        output = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue(), output)
        output = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
            self.assertEqual(f.getvalue(), output)
        output = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(f.getvalue(), output)
        output = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1234")
            self.assertEqual(f.getvalue(), output)
        output = "** attribute name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {uid}")
            self.assertEqual(f.getvalue(), output)
        output = "** value missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {uid} first_name")
            self.assertEqual(f.getvalue(), output)
        #  Error handling class based commands
        output = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.update()")
            self.assertEqual(f.getvalue(), output)
        output = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update()")
            self.assertEqual(f.getvalue(), output)
        output = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update(1234)")
            self.assertEqual(f.getvalue(), output)
        output = "** attribute name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update({uid})")
            self.assertEqual(f.getvalue(), output)
        output = "** value missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update({uid}, first_name)")
            self.assertEqual(f.getvalue(), output)

    def test_quit(self):
        """Test the quit command"""
        output = "Quit command to exit the program\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue(), output)
        output = ""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), output)

    def test_EOF(self):
        """Test the EOF command"""
        output = "EOF command to exit the program\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "\n")

    def test_emptyline(self):
        """Test an emptyline input"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), "")

    def test_help(self):
        """Test all variations of the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIsInstance(f.getvalue(), str)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("?")
            self.assertIsInstance(f.getvalue(), str)

    def testPycodeStyle(self):
        """Pycodestyle test for console.py"""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['console.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_doc_console(self):
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
