#!/usr/bin/python3
"""
Write a class User that inherits
from BaseModel: models/user.py
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Public class attributes:
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
    # Public class attributes
    email = ""        # empty string
    password = ""     # empty string
    first_name = ""   # empty string
    last_name = ""    # empty string

    def __init__(self):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__()
