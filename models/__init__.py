#!/usr/bin/python3
"""
if it’s a new instance (not from a dictionary representation),
add a call to the method new(self) on storage
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
