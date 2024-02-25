#!/usr/bin/python3
"""
Module for testing the BaseModel class
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class
    """

    def test_instance_creation(self):
        """
        Test the creation of a BaseModel instance
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_str_method(self):
        """
        Test the __str__ method of the BaseModel class
        """
        my_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(
            my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_save_method(self):
        """
        Test the save method of the BaseModel class
        """
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(original_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of the BaseModel class
        """
        my_model = BaseModel()
        model_dict = my_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertEqual(model_dict['id'], my_model.id)
        self.assertIn('created_at', model_dict)
        self.assertEqual(
            model_dict['created_at'], my_model.created_at.isoformat())
        self.assertIn('updated_at', model_dict)
        self.assertEqual(
            model_dict['updated_at'], my_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
