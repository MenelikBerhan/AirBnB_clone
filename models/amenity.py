#!/usr/bin/python3
"""Contains the `Amenity` class"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """A class that inherits from base class `BaseModel` and
    defines an amenity with a name class attribute.
    """
    name = ""
