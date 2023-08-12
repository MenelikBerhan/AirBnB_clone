#!/usr/bin/python3
"""
Tests for the `BaseModel` class
"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from datetime import datetime
from importlib import import_module
import uuid
import unittest


class TestBaseModel(unittest.TestCase):
    """Tests for 'BaseModel' class attributes and methods"""

    def setUp(self):
        """Create instances of Base class for testcases"""
        self.a = BaseModel()
        self.b = BaseModel()
        self.objects = (self.a, self.b)

    def tearDown(self):
        """Deletes objects created after each test"""
        del self.a, self.b

    def test_class(self):
        """Test instance class names"""
        self.assertTrue(all(type(obj) == BaseModel for obj in self.objects))

    def test_attributes(self):
        """Tests if required attributes exist"""
        attributes = ['id', 'created_at', 'updated_at']
        self.assertTrue(all(hasattr(self.a, attr) for attr in attributes))

    def test_id(self):
        """Tests public instance attribute `id`"""
        self.assertTrue(hasattr(self.a, 'id'))

    def test_id_value(self):
        """Tests if id attribute is valid"""
        self.assertTrue(all(type(obj.id) == str for obj in self.objects))
        self.assertTrue(all(len(obj.id) == 36 for obj in self.objects))
        self.assertTrue(all(obj.id[x] == '-' for obj in self.objects
                            for x in (8, 13, 18, 23)))
        try:
            uuid.UUID(self.a.id)
            uuid.UUID(self.b.id)
        except ValueError:
            self.fail("Improper id attribute Value")

    def test_created_at(self):
        """Tests if created_at attribute is valid"""
        self.assertTrue(all(type(obj.created_at) == datetime
                            for obj in self.objects))

        self.assertTrue(all((datetime.now() - obj.created_at).seconds <= 1
                            for obj in self.objects))

    def test_updated_at(self):
        """Tests if updated_at attribute is valid"""
        self.assertTrue(all(type(obj.updated_at) == datetime
                            for obj in self.objects))

        self.assertTrue(all((datetime.now() - obj.updated_at).seconds <= 1
                            for obj in self.objects))


if __name__ == '__main__':
    unittest.main()
