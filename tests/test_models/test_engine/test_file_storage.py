#!/usr/bin/python3
"""
`TestFileStorage` test case to test the `FileStorage` class
"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
import json
import os
import time
import uuid
import unittest


class TestFileStorage(unittest.TestCase):
    """Tests for 'FileStorage' class attributes and methods"""

    def setUp(self):
        """Create instances of FileStorage class for testcases"""
        storage._FileStorage__objects = {}
        storage.save()
        self.a = FileStorage()
        self.b = FileStorage()
        self.objects = (self.a, self.b)
        self.base_models = [BaseModel(), BaseModel(), BaseModel()]
        self.users = [User(), User(), User()]
        self.places = [Place(), Place(), Place()]
        self.states = [State(), State(), State()]
        self.cities = [City(), City(), City()]
        self.reviews = [Review(), Review(), Review()]
        self.all_objs = self.base_models + self.users + self.places\
            + self.states + self.cities + self.reviews

    def tearDown(self):
        """Deletes objects created after each test"""
        del self.a, self.b, self.objects, self.base_models
        del self.reviews, self.cities, self.states, self.places, self.users
        del self.all_objs

    def test_class_init(self):
        """Test instance class names"""
        self.assertTrue(hasattr(BaseModel, '__init__'))
        self.assertTrue(all(hasattr(obj, '__init__') for obj in self.objects))
        self.assertTrue(all(type(obj) == FileStorage for obj in self.objects))

    def test_init_method(self):
        """Tests __init__method"""
        with self.assertRaises(TypeError) as e:
            a = FileStorage('a')
        self.assertEqual(str(e.exception), 'FileStorage() takes no arguments')
        with self.assertRaises(TypeError) as e:
            a = FileStorage.__init__()
        self.assertEqual(str(e.exception), "descriptor '__init__' of "
                         + "'object' object needs an argument")

    def test_class_attributes(self):
        """Tests private class attributes"""
        attributes = ['_FileStorage__file_path', '_FileStorage__objects']
        self.assertTrue(hasattr(FileStorage, attr) for attr in attributes)
        self.assertTrue(all(hasattr(obj, attr) for obj in self.objects
                            for attr in attributes))
        c = FileStorage
        self.assertTrue(type(getattr(c, '_FileStorage__file_path')) == str)
        self.assertTrue(type(getattr(c, '_FileStorage__objects')) == dict)
        for o in self.objects:
            self.assertTrue(type(getattr(o, '_FileStorage__file_path')) == str)
            self.assertTrue(type(getattr(o, '_FileStorage__objects')) == dict)

    def test_methods(self):
        """Tests if required methods exist"""
        methods = ['all', 'new', 'save', 'reload']
        self.assertTrue(hasattr(FileStorage, method) for method in methods)
        self.assertTrue(all(hasattr(obj, method)
                            for obj in self.objects for method in methods))

    def test_new(self):
        """Tests the `new` method"""
        with self.assertRaises(TypeError) as e:
            FileStorage.new()
        self.assertEqual(str(e.exception), "new() missing 2 required "
                         + "positional arguments: 'self' and 'obj'")
        with self.assertRaises(TypeError) as e:
            self.a.new()
        self.assertEqual(str(e.exception), "new() missing 1 required "
                         + "positional argument: 'obj'")
        with self.assertRaises(TypeError) as e:
            self.a.new(1, 2)
        self.assertEqual(str(e.exception), 'new() takes 2 positional '
                         + 'arguments but 3 were given')
        # test new(obj) saves obj in __objects
        objs_dict = {}
        FileStorage._FileStorage__objects = {}
        for obj in self.all_objs:
            objs_dict[obj.__class__.__name__ + "." + obj.id] = obj
            self.b.new(obj)
        self.assertEqual(self.b.all(), objs_dict)

    def test_all(self):
        """Tests the `all` method"""
        with self.assertRaises(TypeError) as e:
            FileStorage.all()
        self.assertEqual(str(e.exception), "all() missing 1 required "
                         + "positional argument: 'self'")
        with self.assertRaises(TypeError) as e:
            self.a.all(1)
        self.assertEqual(str(e.exception), 'all() takes 1 positional '
                         + 'argument but 2 were given')
        # test __objects is returned by all
        self.assertEqual(FileStorage._FileStorage__objects, self.a.all())
        self.assertEqual(FileStorage._FileStorage__objects, self.b.all())
        objs_dict = {obj.__class__.__name__ + "." + obj.id: obj
                     for obj in self.all_objs}
        FileStorage._FileStorage__objects = objs_dict
        self.assertEqual(list(self.b.all().values()), self.all_objs)

    def test_save(self):
        """Tests the `save` method"""
        with self.assertRaises(TypeError) as e:
            FileStorage.save()
        self.assertEqual(str(e.exception), "save() missing 1 required "
                         + "positional argument: 'self'")
        with self.assertRaises(TypeError) as e:
            self.a.save(1)
        self.assertEqual(str(e.exception), 'save() takes 1 positional '
                         + 'argument but 2 were given')
        # test save() creates a file with __objects converted to json
        path = storage._FileStorage__file_path
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
        objects_json = {}
        for key, obj in storage._FileStorage__objects.items():
            objects_json[key] = obj.to_dict()
        storage.save()
        with open(path, 'r', encoding='utf-8') as file:
            self.assertEqual(json.load(file), objects_json)

    def test_reload(self):
        """Tests the `reload` method"""
        with self.assertRaises(TypeError) as e:
            FileStorage.reload()
        self.assertEqual(str(e.exception), "reload() missing 1 required "
                         + "positional argument: 'self'")
        with self.assertRaises(TypeError) as e:
            self.a.reload(1)
        self.assertEqual(str(e.exception), 'reload() takes 1 positional '
                         + 'argument but 2 were given')

        # test relaod() doesn't change __objects when path not found
        path = storage._FileStorage__file_path
        old_objects_dict = self.a.all()
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
        self.a.reload()
        self.assertTrue(old_objects_dict == self.a.all())

        # test reload() saves deserilized objects and set it to __objects
        storage._FileStorage__objects = {}
        with open(path, 'w', encoding='utf-8') as file:
            json.dump({k: v.to_dict()
                       for k, v in old_objects_dict.items()}, file)
        self.a.reload()
        self.assertEqual(old_objects_dict.keys(), self.a.all().keys())
        for k, v in self.a.all().items():
            self.assertEqual(str(v), str(old_objects_dict[k]))


if __name__ == '__main__':
    unittest.main()
