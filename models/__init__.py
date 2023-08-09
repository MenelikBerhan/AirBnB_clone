"""Initializes the `models` package by creating
a unique FileStorage instance `storage` to store created objects"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
