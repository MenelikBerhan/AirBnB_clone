"""Initializes the `models` package by creating
a unique FileStorage instance `storage` to store created objects"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
class_dict = {
    "Amenity": "amenity",
    "BaseModel": "base_model",
    "City": "city",
    "Place": "place",
    "Review": "review",
    "State": "state",
    "User": "user"
}
