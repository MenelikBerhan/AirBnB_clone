#!/usr/bin/python3
"""
Tests for the `BaseModel` class
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
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

    def test_attributes(self):
        """Tests if required attributes exist"""
        attributes = ['id', 'created_at', 'updated_at']
        self.assertTrue(all([hasattr(self.a, attr) for attr in attributes]))

    def test_id(self):
        """Tests public instance attribute `id`"""
        self.assertTrue(hasattr(self.a, 'id'))

    def test_id_value(self):
        """Tests if id is a uuid string"""
        self.assertTrue(type(self.a.id) == str)
        self.assertTrue(all([len(obj.id) == 36] for obj in self.objects))
        self.assertTrue(all([obj.id[x] == '-' for obj in self.objects
                             for x in (8, 13, 18, 23)]))
        try:
            uuid.UUID(self.a.id)
            uuid.UUID(self.b.id)
        except ValueError:
            self.fail("Improper id attribute Value")


if __name__ == '__main__':
    unittest.main()
