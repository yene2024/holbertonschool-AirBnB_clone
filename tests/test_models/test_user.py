#!/usr/bin/python3
"""unittest of the User Class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    This class contains unit tests for the User class.
    """

    def test_user_attributes(self):
        """
        Test case to verify the default attribute values of a User instance.
        """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_init(self):
        """
        Test case to verify the initialization of a User instance with specific attribute values.
        """
        user = User(email="test@example.com", password="password",
                    first_name="John", last_name="Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_email(self):
        """
        Test case to verify the email attribute of a User instance.
        """
        user = User()
        user.email = "test@example.com"
        self.assertEqual(user.email, "test@example.com")

    def test_user_password(self):
        """
        Test case to verify the password attribute of a User instance.
        """
        user = User()
        user.password = "password"
        self.assertEqual(user.password, "password")

    def test_user_first_name(self):
        """
        Test case to verify the first_name attribute of a User instance.
        """
        user = User()
        user.first_name = "John"
        self.assertEqual(user.first_name, "John")

    def test_user_last_name(self):
        """
        Test case to verify the last_name attribute of a User instance.
        """
        user = User()
        user.last_name = "Doe"
        self.assertEqual(user.last_name, "Doe")

    def test_user_str(self):
        """
        Test case to verify the __str__ method of a User instance.
        """
        user = User(email="test@example.com", password="password",
                    first_name="John", last_name="Doe")
        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)

    def test_user_to_dict(self):
        """
        Test case to verify the to_dict method of a User instance.
        """
        user = User(email="test@example.com", password="password",
                    first_name="John", last_name="Doe")
        user_dict = user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["email"], "test@example.com")
        self.assertEqual(user_dict["password"], "password")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")


if __name__ == '__main__':
    unittest.main()
