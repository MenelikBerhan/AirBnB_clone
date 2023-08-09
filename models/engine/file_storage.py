#!/usr/bin/python3
"""Contains the `FileStorage` class"""
import json


class FileStorage():
    """Serializes instances to a JSON file and deserializes
    JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """`dict`: returns `_objects` private class attribute"""
        return self.__objects

    def new(self, obj):
        """Adds `<obj class name>.id`: `obj` key value pair to `__objects`"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serializes `__object` to a JSON file named in `__file_path`"""
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            objects_json = {}
            for key, obj in self.__objects.items():
                objects_json[key] = obj.to_dict()
            json.dump(objects_json, file)

    def reload(self):
        """Deseralizes the JSON file named in `__file_path` and assign
        it to `__objects`"""
        from ..base_model import BaseModel
        from ..user import User
        from ..state import State
        from ..city import City
        from ..place import Place
        from ..amenity import Amenity
        from ..review import Review
        objects_json = {}
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                objects_json = json.load(file)
                for key, obj in objects_json.items():
                    self.__objects[key] = eval(obj['__class__'] + '(**obj)')

        except FileNotFoundError:
            pass
