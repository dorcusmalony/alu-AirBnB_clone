from models.amenity import Amenity
from models import storage
import unittest


class TestAmenity(unittest.TestCase):

  def test_amenity_initialization(self):
    amenity_1 = Amenity()
    self.assertIsInstance(amenity_1, Amenity)
    amenity1_id = amenity_1.id
    amenity1_class_name = type(amenity_1).__name__
    amenity1_key = f"{amenity1_class_name}.{amenity1_id}"
    amenity_1.save()
    storage.reload()
    self.assertTrue(amenity1_key in storage.all())
