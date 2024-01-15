#!/usr/bin/python3
"""
Write all those classes that
inherit from BaseModel:
Review (models/review.py):
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Public class attributes:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self):
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__()
