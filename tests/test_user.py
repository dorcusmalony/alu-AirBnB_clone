#!/usr/bin/python3
"""
All your files, classes, functions must
be tested with unit tests
"""
from models.user import User
from models import storage
import unittest


class TestUser(unittest.TestCase):
    """
    All your files, classes, functions must
    be tested with unit tests
    """
    def test_user_initialization(self):
        user_1 = User()
        self.assertIsInstance(user_1, User)
        user1_id = user_1.id
        user1_class_name = type(user_1).__name__
        user1_key = f"{user1_class_name}.{user1_id}"
        user_1.save()
        storage.reload()
        self.assertTrue(user1_key in storage.all())

    def test_user_public_class_attributes(self):
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
