#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
import os
from models.user import User
from datetime import datetime


class test_user(unittest.TestCase):
    """Test cases for user class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.user = User()
        try:
            os.rename("file.json", "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """Class method to close test's environment"""
        try:
            os.remove("file.json")
            os.rename("test_file.json", "file.json")
        except Exception:
            pass

    def test_save_method(self):
        """Test case for 'save' method"""
        datetime_prev = self.user.updated_at
        self.user.save()
        self.assertGreater(self.user.updated_at, datetime_prev)
        self.assertTrue(os.path.exists("file.json"))

    def test_str_method(self):
        """Test case for str instance representation"""
        cls_name = str(self.user.__class__.__name__)
        obj_dict = str(self.user.__dict__)
        obj_str = "[{}] ({}) {}".format(cls_name, self.user.id, obj_dict)
        self.assertEqual(obj_str, self.user.__str__())

    def test_to_dict_method(self):
        """Test case for 'to_dict' method"""
        dict = {
            "id": self.user.id,
            "__class__": self.user.__class__.__name__,
            "created_at": self.user.created_at.isoformat(),
            "updated_at": self.user.updated_at.isoformat()
        }
        self.assertDictEqual(dict, self.user.to_dict())


if __name__ == "__main__":
    unittest.main()
