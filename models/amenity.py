#!/usr/bin/python3
"""
Write all those classes that
inherit from BaseModel:
Amenity (models/amenity.py)
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Public class attributes:
    name: string - empty string
    """
    name = ""

    def __init__(self):
        self.name = ""
        super().__init__()
