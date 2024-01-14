from models.review import Review
from models import storage
import unittest


class TestReview(unittest.TestCase):

  def test_review_initialization(self):
    review_1 = Review()
    self.assertIsInstance(review_1, Review)
    review1_id = review_1.id
    review1_class_name = type(review_1).__name__
    review1_key = f"{review1_class_name}.{review1_id}"
    review_1.save()
    storage.reload()
    self.assertTrue(review1_key in storage.all())
