#!/usr/bin/python3
"""Contains the `State` class"""
from .base_model import BaseModel


class State(BaseModel):
    """A class that inherits from base class `BaseModel` and
    defines a state with name class attribute.
    """
    name = ""
