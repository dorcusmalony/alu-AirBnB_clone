#!/usr/bin/python3
"""
Write all those classes that
inherit from BaseModel:
State (models/state.py)
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Public class attributes:
    name: string - empty string
    """
    name = ""

    def __init__(self):
        self.name = ""
        super().__init__()
