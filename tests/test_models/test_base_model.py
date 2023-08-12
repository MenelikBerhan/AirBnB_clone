#!/usr/bin/python3
"""
`TestBaseModel` test case to test the `BaseModel` class
"""
from models.base_model import BaseModel
from datetime import datetime
import time
import uuid
import unittest


class TestBaseModel(unittest.TestCase):
    """Tests for 'BaseModel' class attributes and methods"""

    def setUp(self):
        """Create instances of Base class for testcases"""
        self.a = BaseModel()
        self.b = BaseModel()
        self.c = BaseModel()
        self.objects = (self.a, self.b, self.c)

    def tearDown(self):
        """Deletes objects created after each test"""
        del self.a, self.b, self.c

    def test_class_init(self):
        """Test instance class names"""
        self.assertTrue(hasattr(BaseModel, '__init__'))
        self.assertTrue(all(type(obj) == BaseModel for obj in self.objects))

    def test_init_method(self):
        """Tests __init__method"""
        a_1 = BaseModel(**self.a.to_dict())
        a_2 = BaseModel('1', '2', '3', **self.a.to_dict())
        self.assertTrue(self.a.id == a_1.id == a_2.id)
        self.assertTrue(self.a.created_at == a_1.created_at == a_2.created_at)
        self.assertTrue(self.a.updated_at == a_1.updated_at ==
                        a_2.updated_at)
        self.assertTrue(self.a.to_dict() == a_1.to_dict() == a_2.to_dict())
        self.assertTrue(all('__class__' not in obj.__dict__
                            for obj in (a_1, a_2)))
        self.assertTrue(all(type(obj.created_at) == datetime
                            for obj in (a_1, a_2)))
        self.assertTrue(all(type(obj.updated_at) == datetime
                            for obj in (a_1, a_2)))
        a = BaseModel('123', '0', '0')
        self.assertTrue(all([a.id != '123', a.created_at != '0',
                            a.updated_at != '0']))

    def test_attributes(self):
        """Tests if required attributes exist"""
        attributes = ['id', 'created_at', 'updated_at']
        self.assertTrue(all(hasattr(obj, attr) for obj in self.objects
                            for attr in attributes))

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

        self.assertTrue(all((datetime.now() - obj.created_at).seconds == 0
                            for obj in self.objects))

    def test_updated_at(self):
        """Tests if updated_at attribute is valid"""
        self.assertTrue(all(type(obj.updated_at) == datetime
                            for obj in self.objects))

        self.assertTrue(all((datetime.now() - obj.updated_at).seconds == 0
                            for obj in self.objects))

    def test_methods(self):
        """Tests if required methods exist"""
        methods = ['__str__', 'save', 'to_dict']
        self.assertTrue(hasattr(BaseModel, method) for method in methods)
        self.assertTrue(all(hasattr(obj, method)
                            for obj in self.objects for method in methods))

    def test_storage_variable(self):
        """Tests storage variable"""
        import models
        import models.base_model as module
        self.assertTrue(hasattr(models, 'storage'))
        self.assertTrue(type(models.storage).__name__ == 'FileStorage')
        self.assertTrue(hasattr(module, 'storage'))
        self.assertTrue(type(module.storage).__name__ == 'FileStorage')

    def test_str(self):
        """Tests __str__ method"""
        with self.assertRaises(TypeError) as e:
            self.a.__str__(12)
        self.assertEqual(str(e.exception), "__str__() takes 1 positional "
                         + "argument but 2 were given")
        self.assertTrue(str(obj) == "[BaseModel] ({obj.id}) {obj.__dict__}"
                        for obj in self.objects)

    def test_save(self):
        """Tests the save method"""
        with self.assertRaises(TypeError) as e:
            self.a.save(12)
        self.assertEqual(str(e.exception), "save() takes 1 positional "
                         + "argument but 2 were given")
        updated_at_old = [obj.updated_at for obj in self.objects]
        for obj in self.objects:
            obj.save()
        update_at_new = [obj.updated_at for obj in self.objects]
        deltas = [(new - old)
                  for new, old in zip(update_at_new, updated_at_old)]
        self.assertTrue(all(delta.days == 0 and delta.seconds == 0
                            and delta.microseconds > 0 for delta in deltas))
        time.sleep(1)
        for obj in self.objects:
            obj.save()
        updated_at_old = update_at_new
        update_at_new = [obj.updated_at for obj in self.objects]
        deltas = [(new - old).total_seconds()
                  for new, old in zip(update_at_new, updated_at_old)]
        self.assertTrue(all(delta >= 1 for delta in deltas))

    def test_to_dict(self):
        """Tests the to_dict method"""
        with self.assertRaises(TypeError) as e:
            self.a.to_dict(12)
        self.assertEqual(str(e.exception), "to_dict() takes 1 positional "
                         + "argument but 2 were given")
        for obj in self.objects:
            obj_dict = obj.__dict__.copy()
            obj_dict['__class__'] = type(obj).__name__
            obj_dict['created_at'] = obj.created_at.isoformat()
            obj_dict['updated_at'] = obj.updated_at.isoformat()
            self.assertEqual(obj.to_dict(), obj_dict)
            obj.name = 'test'
            obj.number = 1
        for obj in self.objects:
            obj_dict = obj.__dict__.copy()
            obj_dict['__class__'] = type(obj).__name__
            obj_dict['created_at'] = obj.created_at.isoformat()
            obj_dict['updated_at'] = obj.updated_at.isoformat()
            self.assertEqual(obj.to_dict(), obj_dict)


if __name__ == '__main__':
    unittest.main()
