#!/usr/bin/python3
"""
All your files, classes, functions must
be tested with unit tests
"""
from datetime import datetime
from models.base_model import BaseModel
from models import storage
import unittest
import uuid
import json


class TestBaseModel(unittest.TestCase):
    """
    All your files, classes, functions must
    be tested with unit tests
    """
    def test_string_method(self):
        o1 = BaseModel()
        o1.save()
        storage.reload()
        o2 = BaseModel()
        o2.save()
        storage.reload()
        o3 = BaseModel()
        o3.save()
        storage.reload()
        self.assertEqual(o1.__str__(),
                         f"[{type(o1).__name__}] ({o1.id}) {o1.__dict__}")
        self.assertEqual(o2.__str__(),
                         f"[{type(o2).__name__}] ({o2.id}) {o2.__dict__}")
        self.assertEqual(o3.__str__(),
                         f"[{type(o3).__name__}] ({o3.id}) {o3.__dict__}")

    def test_save_method(self):
        obj1 = BaseModel()
        before_save1 = obj1.updated_at
        obj1.save()
        storage.reload()
        obj2 = BaseModel()
        before_save2 = obj2.updated_at
        obj2.save()
        storage.reload()
        obj3 = BaseModel()
        before_save3 = obj3.updated_at
        obj3.save()
        storage.reload()
        after_save1 = obj1.updated_at
        after_save2 = obj2.updated_at
        after_save3 = obj3.updated_at
        self.assertIsInstance(before_save1, datetime)
        self.assertIsInstance(before_save2, datetime)
        self.assertIsInstance(before_save3, datetime)
        self.assertIsInstance(after_save1, datetime)
        self.assertIsInstance(after_save2, datetime)
        self.assertIsInstance(after_save3, datetime)
        self.assertNotEqual(before_save1, after_save1)
        self.assertNotEqual(before_save2, after_save2)
        self.assertNotEqual(before_save3, after_save3)

    def test_save_method_2(self):
        obj1 = BaseModel()
        before_save1 = obj1.updated_at
        before_save2 = obj1.created_at
        obj1.save()
        after_save1 = obj1.updated_at.isoformat()
        after_save2 = obj1.created_at.isoformat()
        self.assertIsInstance(before_save1, datetime)
        self.assertIsInstance(before_save2, datetime)
        self.assertIsInstance(after_save1, str)
        self.assertIsInstance(after_save2, str)
        storage.reload()

    def test_isformat_method(self):
        obj1 = BaseModel()
        obj1.save()
        storage.reload()
        obj2 = BaseModel()
        obj2.save()
        obj3 = BaseModel()
        obj3.save()
        storage.reload()
        obj1_dict = obj1.to_dict()
        obj2_dict = obj2.to_dict()
        obj3_dict = obj3.to_dict()
        self.assertEqual(obj1_dict["created_at"], obj1.created_at)
        self.assertEqual(obj1_dict["updated_at"], obj1.updated_at)
        self.assertEqual(obj2_dict["created_at"], obj2.created_at)
        self.assertEqual(obj2_dict["updated_at"], obj2.updated_at)
        self.assertEqual(obj3_dict["created_at"], obj3.created_at)
        self.assertEqual(obj3_dict["updated_at"], obj3.updated_at)

    def test_isinstance(self):
        self.obj1 = BaseModel()
        self.obj1.save()
        storage.reload()
        self.obj2 = BaseModel()
        self.obj2.save()
        storage.reload()
        self.obj3 = BaseModel()
        self.obj3.save()
        storage.reload()
        self.assertIsInstance(self.obj1, BaseModel)
        self.assertIsInstance(self.obj2, BaseModel)
        self.assertIsInstance(self.obj3, BaseModel)

    def test_initialization_attributes_without_args_kwargs(self):
        self.obj4 = BaseModel()
        self.obj4.save()
        storage.reload()
        self.obj5 = BaseModel()
        self.obj5.save()
        storage.reload()
        self.assertIsInstance(self.obj4.id, str)
        self.assertIsInstance(self.obj5.id, str)
        self.assertIsInstance(self.obj4.created_at, datetime)
        self.assertIsInstance(self.obj5.created_at, datetime)
        self.assertIsInstance(self.obj4.updated_at, datetime)
        self.assertIsInstance(self.obj5.updated_at, datetime)
        self.assertEqual(len(self.obj4.id), 36)
        self.assertEqual(len(self.obj5.id), 36)

    def test_initialization_attributes_with_args_only(self):
        args_1 = (str(uuid.uuid4()), datetime.now(), datetime.now())
        obj1 = BaseModel(*args_1)
        obj1.save()
        storage.reload()
        args_2 = (str(uuid.uuid4()), datetime.now(), datetime.now())
        obj2 = BaseModel(*args_2)
        obj2.save()
        storage.reload()
        self.assertNotEqual(obj1.id, args_1[0])
        self.assertNotEqual(obj2.id, args_2[0])
        self.assertNotEqual(obj1.created_at, args_1[1])
        self.assertNotEqual(obj2.created_at, args_2[1])
        self.assertNotEqual(obj1.updated_at, args_1[2])
        self.assertNotEqual(obj2.updated_at, args_2[2])
        self.assertIsInstance(obj1.id, str)
        self.assertIsInstance(obj2.id, str)
        self.assertIsInstance(obj1.created_at, datetime)
        self.assertIsInstance(obj2.created_at, datetime)
        self.assertIsInstance(obj1.updated_at, datetime)
        self.assertIsInstance(obj2.updated_at, datetime)
        self.assertEqual(len(obj1.id), 36)
        self.assertEqual(len(obj2.id), 36)

    def test_initialization_attributes_with_kwargs_only(self):
        my_model = BaseModel()
        my_model.save()
        storage.reload()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        my_new_model.save()
        storage.reload()
        self.assertIsInstance(my_new_model.id, str)
        self.assertIsInstance(my_new_model.created_at, datetime)
        self.assertIsInstance(my_new_model.updated_at, datetime)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertNotEqual(my_model.created_at, my_new_model.created_at)
        self.assertNotEqual(my_model.created_at, my_new_model.updated_at)
        self.assertNotEqual(my_model, my_new_model)

    def test_dict_method(self):
        obj1 = BaseModel()
        obj1.save()
        storage.reload()
        obj1_new_dict = obj1.to_dict()
        obj2 = BaseModel()
        obj2.save()
        storage.reload()
        obj2_new_dict = obj2.to_dict()
        obj3 = BaseModel()
        obj3.save()
        storage.reload()
        obj3_new_dict = obj3.to_dict()
        self.assertDictEqual(obj1_new_dict, obj1.__dict__)
        self.assertDictEqual(obj2_new_dict, obj2.__dict__)
        self.assertDictEqual(obj3_new_dict, obj3.__dict__)
