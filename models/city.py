#!/usr/bin/python3
"""Contains the `City` class"""
from .base_model import BaseModel


class City(BaseModel):
    """A class that inherits from base class `BaseModel` and
    defines a city with a state id and name class attribute.
    """
    state_id = ""
    name = ""
