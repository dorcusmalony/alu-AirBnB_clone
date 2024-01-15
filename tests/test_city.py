#!/usr/bin/python3
"""
All your files, classes, functions must
be tested with unit tests
"""
from models.city import City
from models import storage
import unittest


class TestCity(unittest.TestCase):
    """
    All your files, classes, functions must
    be tested with unit tests
    """
    def test_city_initialization(self):
        city_1 = City()
        self.assertIsInstance(city_1, City)
        city1_id = city_1.id
        city1_class_name = type(city_1).__name__
        city1_key = f"{city1_class_name}.{city1_id}"
        city_1.save()
        storage.reload()
        self.assertTrue(city1_key in storage.all())

    def test_city_public_class_attribute(self):
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")
