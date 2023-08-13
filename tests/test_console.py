#!/usr/bin/python3
"""Contains test cases for the command line interface of the AirBnB project"""
import os
import pycodestyle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestConsole(TestCase):
    """Suite of test for the console"""

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
        output = "$ create <class name>\n" \
            "Create a new instance of a class"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(f.getvalue().strip(), output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? create")
            self.assertEqual(f.getvalue().strip(), output)
        output = "$ show <class name> <id>\n" \
            "Prints the string representation of an instance"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(f.getvalue().strip(), output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? show")
            self.assertEqual(f.getvalue().strip(), output)
        output = "$ destroy <class name> <id>\n" \
            "Deletes an instance based on the class name and id"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(f.getvalue().strip(), output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? destroy")
            self.assertEqual(f.getvalue().strip(), output)
        output = "$ all [<class name>]\n" \
            "Prints all string representations of all instances"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(f.getvalue().strip(), output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? all")
            self.assertEqual(f.getvalue().strip(), output)
        output = "$ update <class name> <id> <attribute name> '<value>'\n" \
            "Updates an instance based on the class name and id"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(f.getvalue().strip(), output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? update")
            self.assertEqual(f.getvalue().strip(), output)

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


class TestCreateCommand(TestCase):
    """Suite of test for the create command"""

    opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'

    def tearDown(self):
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_BaseModel(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertRegex(f.getvalue(), TestCreateCommand.opt)
            self.assertIn(
                f"BaseModel.{f.getvalue().strip()}", storage.all().keys())

    def test_create_User(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertRegex(f.getvalue(), TestCreateCommand.opt)
            self.assertIn(f"User.{f.getvalue().strip()}", storage.all().keys())

    def test_create_State(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            self.assertRegex(f.getvalue(), TestCreateCommand.opt)
            self.assertIn(
                f"State.{f.getvalue().strip()}", storage.all().keys())

    def test_create_City(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            self.assertRegex(f.getvalue(), TestCreateCommand.opt)
            self.assertIn(
                f"City.{f.getvalue().strip()}", storage.all().keys())

    def test_create_Amenity(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            self.assertRegex(f.getvalue(), TestCreateCommand.opt)
            self.assertIn(
                f"Amenity.{f.getvalue().strip()}", storage.all().keys())

    def test_create_Place(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            self.assertRegex(f.getvalue(), TestCreateCommand.opt)
            self.assertIn(
                f"Place.{f.getvalue().strip()}", storage.all().keys())

    def test_create_Review(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            self.assertRegex(f.getvalue(), TestCreateCommand.opt)
            self.assertIn(
                f"Review.{f.getvalue().strip()}", storage.all().keys())

    def test_error_messages(self):
        output = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), output)
        output = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(f.getvalue(), output)


class TestShowCommand(TestCase):
    """Suite of tests for the show command"""

    def tearDown(self):
        """Tear down for show method tests."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_show_BaseModel(self):
        b = BaseModel()
        b.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {b.id}")
            self.assertEqual(f.getvalue().strip(), str(b))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show({b.id})")
            self.assertEqual(f.getvalue().strip(), str(b))

    def test_show_User(self):
        u = User()
        u.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {u.id}")
            self.assertEqual(f.getvalue().strip(), str(u))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show({u.id})")
            self.assertEqual(f.getvalue().strip(), str(u))

    def test_show_State(self):
        s = State()
        s.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show State {s.id}")
            self.assertEqual(f.getvalue().strip(), str(s))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show({s.id})")
            self.assertEqual(f.getvalue().strip(), str(s))

    def test_show_City(self):
        c = City()
        c.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show City {c.id}")
            self.assertEqual(f.getvalue().strip(), str(c))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.show({c.id})")
            self.assertEqual(f.getvalue().strip(), str(c))

    def test_show_Amenity(self):
        a = Amenity()
        a.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Amenity {a.id}")
            self.assertEqual(f.getvalue().strip(), str(a))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show({a.id})")
            self.assertEqual(f.getvalue().strip(), str(a))

    def test_show_Place(self):
        p = Place()
        p.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Place {p.id}")
            self.assertEqual(f.getvalue().strip(), str(p))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show({p.id})")
            self.assertEqual(f.getvalue().strip(), str(p))

    def test_show_Review(self):
        r = Review()
        r.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Review {r.id}")
            self.assertEqual(f.getvalue().strip(), str(r))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show({r.id})")
            self.assertEqual(f.getvalue().strip(), str(r))

    def test_error_message(self):
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


class TestDestroyCommand(TestCase):
    """Suite of tests for the destroy command"""

    errMsg = "** no instance found **"

    def tearDown(self):
        """Tear down for destroy method tests."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_destroy_BaseModel(self):
        b = BaseModel()
        b.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel {b.id}")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"show BaseModel {b.id}")
            self.assertEqual(f.getvalue().strip(), TestDestroyCommand.errMsg)
        b = BaseModel()
        b.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.destroy({b.id})")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"BaseModel.show({b.id})")
            self.assertEqual(f.getvalue().strip(), TestDestroyCommand.errMsg)

    def test_destroy_User(self):
        u = User()
        u.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {u.id}")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"show User {u.id}")
            self.assertEqual(f.getvalue().strip(), TestDestroyCommand.errMsg)
        u = User()
        u.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.destroy({u.id})")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"User.show({u.id})")
            self.assertEqual(f.getvalue().strip(), TestDestroyCommand.errMsg)

    def test_destroy_State(self):
        s = State()
        s.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy State {s.id}")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"show State {s.id}")
            self.assertEqual(f.getvalue().strip(), TestDestroyCommand.errMsg)
        s = State()
        s.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.destroy({s.id})")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"State.show({s.id})")
            self.assertEqual(f.getvalue().strip(), TestDestroyCommand.errMsg)

    def test_destroy_City(self):
        c = City()
        c.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy City {c.id}")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"show City {c.id}")
            self.assertEqual(f.getvalue().strip(), TestDestroyCommand.errMsg)
        c = City()
        c.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.destroy({c.id})")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"City.show({c.id})")
            self.assertEqual(f.getvalue().strip(), TestDestroyCommand.errMsg)

    def test_destroy_Amenity(self):
        a = Amenity()
        a.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Amenity {a.id}")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"show Amenity {a.id}")
            self.assertEqual(f.getvalue().strip(), TestDestroyCommand.errMsg)
        a = Amenity()
        a.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.destroy({a.id})")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"Amenity.show({a.id})")
            self.assertEqual(f.getvalue().strip(), TestDestroyCommand.errMsg)

    def test_destroy_Place(self):
        p = Place()
        p.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Place {p.id}")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"show Place {p.id}")
            self.assertEqual(f.getvalue().strip(), TestDestroyCommand.errMsg)
        p = Place()
        p.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.destroy({p.id})")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"Place.show({p.id})")
            self.assertEqual(f.getvalue().strip(), TestDestroyCommand.errMsg)

    def test_destroy_Review(self):
        r = Review()
        r.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Review {r.id}")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"show Review {r.id}")
            self.assertEqual(f.getvalue().strip(), TestDestroyCommand.errMsg)
        r = Review()
        r.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.destroy({r.id})")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"Review.show({r.id})")
            self.assertEqual(f.getvalue().strip(), TestDestroyCommand.errMsg)

    def test_error_message(self):
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


class TestAllCommand(TestCase):
    """Test the all command"""
    maxDiff = None

    def tearDown(self):
        """Tear down for show method tests."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_all(self):
        """Test the all command"""
        storage._FileStorage__objects = {}
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual(f.getvalue().strip(), "[]")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")

    def test_all_BaseModel(self):
        """Test the all command"""
        b = BaseModel()
        b.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual(f.getvalue().strip(), f'["{b}"]')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertEqual(f.getvalue().strip(), f'["{b}"]')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all State")
            self.assertEqual(f.getvalue().strip(), "[]")

    def test_all_State(self):
        """Test the all command"""
        s = State()
        s.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual(f.getvalue().strip(), f'["{s}"]')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all State")
            self.assertEqual(f.getvalue().strip(), f'["{s}"]')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Amenity")
            self.assertEqual(f.getvalue().strip(), "[]")

    def test_all_City(self):
        """Test the all command"""
        c = City()
        c.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual(f.getvalue().strip(), f'["{c}"]')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertEqual(f.getvalue().strip(), "[]")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all City")
            self.assertEqual(f.getvalue().strip(), f'["{c}"]')

    def test_all_Amenity(self):
        """Test the all command"""
        a = Amenity()
        a.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual(f.getvalue().strip(), f'["{a}"]')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all City")
            self.assertEqual(f.getvalue().strip(), "[]")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Amenity")
            self.assertEqual(f.getvalue().strip(), f'["{a}"]')

    def test_all_Place(self):
        """Test the all command"""
        p = Place()
        p.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual(f.getvalue().strip(), f'["{p}"]')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all State")
            self.assertEqual(f.getvalue().strip(), "[]")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Place")
            self.assertEqual(f.getvalue().strip(), f'["{p}"]')

    def test_all_Review(self):
        """Test the all command"""
        r = Review()
        r.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual(f.getvalue().strip(), f'["{r}"]')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Place")
            self.assertEqual(f.getvalue().strip(), "[]")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Review")
            self.assertEqual(f.getvalue().strip(), f'["{r}"]')

    def test_all_User(self):
        """Test the all command"""
        u = User()
        u.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual(f.getvalue().strip(), f'["{u}"]')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Review")
            self.assertEqual(f.getvalue().strip(), "[]")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertEqual(f.getvalue().strip(), f'["{u}"]')

    def test_error_message(self):
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


class TestCountCommand(TestCase):
    """Test the count command"""

    def tearDown(self):
        """Tear down for show method tests."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_count_BaseModel(self):
        """Test the count command"""
        b = BaseModel()
        b.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual(f.getvalue().strip(), "1")

    def test_count_State(self):
        """Test the count command"""
        s = State()
        s.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
            self.assertEqual(f.getvalue().strip(), "1")

    def test_count_City(self):
        """Test the count command"""
        c = City()
        c.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
            self.assertEqual(f.getvalue().strip(), "1")

    def test_count_Amenity(self):
        """Test the count command"""
        a = Amenity()
        a.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual(f.getvalue().strip(), "1")

    def test_count_Place(self):
        """Test the count command"""
        p = Place()
        p.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            self.assertEqual(f.getvalue().strip(), "1")

    def test_count_Review(self):
        """Test the count command"""
        r = Review()
        r.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
            self.assertEqual(f.getvalue().strip(), "1")

    def test_count_User(self):
        """Test the count command"""
        u = User()
        u.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(f.getvalue().strip(), "1")

    def test_error_message(self):
        output = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.count()")
            self.assertEqual(f.getvalue(), output)


class TestUpdateCommand(TestCase):
    """Test the update command"""

    def tearDown(self):
        """Tear down for show method tests."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_update_BaseModel(self):
        """Test the update command"""
        b = BaseModel()
        b.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {b.id} name Tunde")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"show BaseModel {b.id}")
            self.assertIn("'name': 'Tunde'", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update({b.id}, name, Betty)")
            self.assertEqual(f.getvalue(), "")
            HBNBCommand().onecmd(f"BaseModel.show({b.id})")
            self.assertIn("'name': 'Betty'", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f"BaseModel.update({b.id}, {{'name': 'Taiye', 'age': 20}})")
            self.assertEqual(f.getvalue(), "")
            HBNBCommand().onecmd(f"BaseModel.show({b.id})")
            self.assertIn("'name': 'Taiye'", f.getvalue())
            self.assertIn("'age': '20'", f.getvalue())

    def test_update_State(self):
        """Test the update command"""
        s = State()
        s.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update State {s.id} name Lagos")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"show State {s.id}")
            self.assertIn("'name': 'Lagos'", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.update({s.id}, name, Abuja)")
            self.assertEqual(f.getvalue(), "")
            HBNBCommand().onecmd(f"State.show({s.id})")
            self.assertIn("'name': 'Abuja'", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.update({s.id}, {{'name': 'Osun'}})")
            self.assertEqual(f.getvalue(), "")
            HBNBCommand().onecmd(f"State.show({s.id})")
            self.assertIn("'name': 'Osun'", f.getvalue())

    def test_update_City(self):
        """Test the update command"""
        c = City()
        c.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update City {c.id} name Surulere")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"show City {c.id}")
            self.assertIn("'name': 'Surulere'", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.update({c.id}, name, Ikeja)")
            self.assertEqual(f.getvalue(), "")
            HBNBCommand().onecmd(f"City.show({c.id})")
            self.assertIn("'name': 'Ikeja'", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f"City.update({c.id}, {{'name': 'GRA', 'state_id': '123'}})")
            self.assertEqual(f.getvalue(), "")
            HBNBCommand().onecmd(f"City.show({c.id})")
            self.assertIn("'name': 'GRA'", f.getvalue())
            self.assertIn("'state_id': '123'", f.getvalue())

    def test_update_Amenity(self):
        """Test the update command"""
        a = Amenity()
        a.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Amenity {a.id} name Wifi")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"show Amenity {a.id}")
            self.assertIn("'name': 'Wifi'", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.update({a.id}, name, AC)")
            self.assertEqual(f.getvalue(), "")
            HBNBCommand().onecmd(f"Amenity.show({a.id})")
            self.assertIn("'name': 'AC'", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f"Amenity.update({a.id}, {{'name': 'Fridge'}})")
            self.assertEqual(f.getvalue(), "")
            HBNBCommand().onecmd(f"Amenity.show({a.id})")
            self.assertIn("'name': 'Fridge'", f.getvalue())

    def test_update_Place(self):
        """Test the update command"""
        p = Place()
        p.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update Place {p.id} name "My house"')
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"show Place {p.id}")
            self.assertIn("'name': 'My house'", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Place.update({p.id}, name, "My room")')
            self.assertEqual(f.getvalue(), "")
            HBNBCommand().onecmd(f"Place.show({p.id})")
            self.assertIn("'name': 'My room'", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f"Place.update({p.id}, {{'name': 'paps', 'city_id': '123'}})")
            self.assertEqual(f.getvalue(), "")
            HBNBCommand().onecmd(f"Place.show({p.id})")
            self.assertIn("'name': 'paps'", f.getvalue())
            self.assertIn("'city_id': '123'", f.getvalue())

    def test_update_Review(self):
        """Test the update command"""
        r = Review()
        r.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update Review {r.id} text "My review"')
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"show Review {r.id}")
            self.assertIn("'text': 'My review'", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Review.update({r.id}, text, "My comment")')
            self.assertEqual(f.getvalue(), "")
            HBNBCommand().onecmd(f"Review.show({r.id})")
            self.assertIn("'text': 'My comment'", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f"Review.update({r.id}, {{'text': '***', 'user_id': '123'}})")
            self.assertEqual(f.getvalue(), "")
            HBNBCommand().onecmd(f"Review.show({r.id})")
            self.assertIn("'text': '***'", f.getvalue())
            self.assertIn("'user_id': '123'", f.getvalue())

    def test_update_User(self):
        """Test the update command"""
        u = User()
        u.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {u.id} first_name Toby")
            self.assertEqual(f.getvalue().strip(), "")
            HBNBCommand().onecmd(f"show User {u.id}")
            self.assertIn("'first_name': 'Toby'", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'User.update({u.id}, first_name, Bola)')
            self.assertEqual(f.getvalue(), "")
            HBNBCommand().onecmd(f"User.show({u.id})")
            self.assertIn("'first_name': 'Bola'", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update({}, {})".format(
                u.id, {'email': 'ma@mail.com', 'password': '1234'}))
            self.assertEqual(f.getvalue(), "")
            HBNBCommand().onecmd(f"User.show({u.id})")
            self.assertIn("'email': 'ma@mail.com'", f.getvalue())
            self.assertIn("'password': '1234'", f.getvalue())

    def test_error_message(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        uid = f.getvalue().strip()
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
