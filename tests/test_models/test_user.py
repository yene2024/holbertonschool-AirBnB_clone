#!/usr/bin/python3
"""Module test_user"""
import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):
    """Testing User functionality"""

    def setUp(self):
        """Set up"""
        self.user1 = User()
        self.user2 = User()
        self.user2.email = "user@example.com"
        self.user2.password = "password"
        self.user2.first_name = "Betty"
        self.user2.last_name = "Holberton"
        self.user2.save()

    def test_attributes(self):
        """Testing User attributes"""
        self.assertTrue(hasattr(self.user1, "email"))
        self.assertTrue(hasattr(self.user1, "password"))
        self.assertTrue(hasattr(self.user1, "first_name"))
        self.assertTrue(hasattr(self.user1, "last_name"))

    def test_id(self):
        """Testing User id"""
        self.assertNotEqual(self.user1.id, self.user2.id)

    def test_attribute_default(self):
        """Test attribute default"""
        self.assertEqual(self.user1.email, "")
        self.assertEqual(self.user1.password, "")
        self.assertEqual(self.user1.first_name, "")
        self.assertEqual(self.user1.last_name, "")

    def test_created_at(self):
        """Testing created_at"""
        self.assertNotEqual(self.user1.created_at, self.user2.created_at)

    def test_str(self):
        """Testing User __str__"""
        expected = "[User] ({}) {}".format(self.user1.id, self.user1.__dict__)
        self.assertEqual(expected, str(self.user1))

    def test_save(self):
        """Testing save"""
        created = self.user1.created_at
        updated = self.user1.updated_at
        self.user1.save()
        self.assertNotEqual(updated, self.user1.updated_at)
        self.assertEqual(created, self.user1.created_at)

    def test_to_dict(self):
        """Testing to_dict"""
        expected = {
            "id": self.user2.id,
            "__class__": type(self.user2).__name__,
            "email": "user@example.com",
            "password": "password",
            "first_name": "Betty",
            "last_name": "Holberton",
            "created_at": self.user2.created_at.isoformat(),
            "updated_at": self.user2.updated_at.isoformat()
        }
        self.assertDictEqual(expected, self.user2.to_dict())


if __name__ == "__main__":
    unittest.main()
