#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertTrue(hasattr(bm, 'id'))
        self.assertTrue(hasattr(bm, 'created_at'))
        self.assertTrue(hasattr(bm, 'updated_at'))

    def test_str(self):
        bm = BaseModel()
        self.assertIsInstance(str(bm), str)

    def test_save(self):
        bm = BaseModel()
        bm.save()
        self.assertNotEqual(bm.created_at, bm.updated_at)

    def test_to_dict(self):
        bm = BaseModel()
        obj_dict = bm.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_to_json_string(self):
        bm = BaseModel()
        json_string = bm.to_json_string()
        self.assertIsInstance(json_string, str)
