#!/usr/bin/python3
"""
All your files, classes, functions must
be tested with unit tests
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import unittest
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """
    All your files, classes, functions must
    be tested with unit tests
    """
    def test_file_storage_initialization(self):
        self.assertIsInstance(storage, FileStorage)

    def test_file_storage_private_class_attributes(self):
        self.assertEqual(FileStorage.__file_path, "file.json")
        self.assertEqual(FileStorage.__objects, {})
      
    def test_all_method(self):
        model2 = BaseModel()
        model2.save()
        storage.reload()
        model2_id = model2.id
        model2_class_name = type(model2).__name__
        self.assertTrue(f"{model2_class_name}.{model2_id}" in storage.all())

    def test_reload_method(self):
      model = BaseModel()
      model_id = model.id
      model_class_name = type(model).__name__
      model_key = f"{model_class_name}.{model_id}"
      model_dict = storage.all()[model_key]
      self.assertFalse("__class__" in model_dict)
      model.save()
      storage.reload()
      model_dict = storage.all()[model_key]
      self.assertTrue("__class__" in model_dict)

    def test_new_method(self):
      prev_dict_length = len(storage.all())
      new_added_model = BaseModel()
      curr_dict_length = len(storage.all())
      self.assertNotEqual(prev_dict_length, curr_dict_length)
      new_added_model.save()
      storage.reload()

    def test_save_method(self):
      last_model = BaseModel()
      self.assertIsInstance(last_model.created_at, datetime)
      self.assertIsInstance(last_model.updated_at, datetime)
      self.assertTrue("__class__" not in storage.all()
                      [f"{type(last_model).__name__}.{last_model.id}"])
      last_model.save()
      self.assertIsInstance(
          storage.all()[f"{type(last_model).__name__}.{last_model.id}"]
          ["updated_at"], str)
      self.assertIsInstance(
          storage.all()[f"{type(last_model).__name__}.{last_model.id}"]
          ["updated_at"], str)
      self.assertTrue("__class__" in storage.all()
                      [f"{type(last_model).__name__}.{last_model.id}"])
      storage.reload()
