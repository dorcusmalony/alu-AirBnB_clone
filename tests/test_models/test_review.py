#!/usr/bin/python3
"""
All your files, classes, functions must
be tested with unit tests
"""
from models.review import Review
from models import storage
import unittest


class TestReview(unittest.TestCase):
    """
    All your files, classes, functions must
    be tested with unit tests
    """
    def test_review_initialization(self):
        review_1 = Review()
        self.assertIsInstance(review_1, Review)
        review1_id = review_1.id
        review1_class_name = type(review_1).__name__
        review1_key = f"{review1_class_name}.{review1_id}"
        review_1.save()
        storage.reload()
        self.assertTrue(review1_key in storage.all())

    def test_review_public_class_attribute(self):
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
