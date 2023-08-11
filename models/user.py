#!/usr/bin/python3
"""Contains the `User` class"""
from .base_model import BaseModel


class User(BaseModel):
    """A class that inherits from base class `BaseModel` and
    defines a user with name, password and email attributes.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
