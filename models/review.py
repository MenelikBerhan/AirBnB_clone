#!/usr/bin/python3
"""Contains the `Review` class"""
from .base_model import BaseModel


class Review(BaseModel):
    """A class that inherits from base class `BaseModel` and
    defines a review with place id, user id and text.
    """
    place_id = ""
    user_id = ""
    text = ""
