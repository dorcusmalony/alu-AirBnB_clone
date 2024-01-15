#!/usr/bin/python3
"""
All your files, classes, functions must
be tested with unit tests
"""
from models.place import Place
from models import storage
import unittest


class TestPlace(unittest.TestCase):
    """
    All your files, classes, functions must
    be tested with unit tests
    """
    def test_place_initialization(self):
        place_1 = Place()
        self.assertIsInstance(place_1, Place)
        place1_id = place_1.id
        place1_class_name = type(place_1).__name__
        place1_key = f"{place1_class_name}.{place1_id}"
        place_1.save()
        storage.reload()
        self.assertTrue(place1_key in storage.all())

    def test_place_public_class_attribute(self):
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])
