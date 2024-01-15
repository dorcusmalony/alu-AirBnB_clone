#!/usr/bin/python3
"""
All your files, classes, functions must
be tested with unit tests
"""
from models.state import State
from models import storage
import unittest


class TestState(unittest.TestCase):
    """
    All your files, classes, functions must
    be tested with unit tests
    """
    def test_state_initialization(self):
        state_1 = State()
        self.assertIsInstance(state_1, State)
        state1_id = state_1.id
        state1_class_name = type(state_1).__name__
        state1_key = f"{state1_class_name}.{state1_id}"
        state_1.save()
        storage.reload()
        self.assertTrue(state1_key in storage.all())

    def test_state_public_class_attribute(self):
        self.assertEqual(State.name, "")
