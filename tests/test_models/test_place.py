from models.place import Place
from models import storage
import unittest


class TestPlace(unittest.TestCase):

  def test_place_initialization(self):
    place_1 = Place()
    self.assertIsInstance(place_1, Place)
    place1_id = place_1.id
    place1_class_name = type(place_1).__name__
    place1_key = f"{place1_class_name}.{place1_id}"
    place_1.save()
    storage.reload()
    self.assertTrue(place1_key in storage.all())
