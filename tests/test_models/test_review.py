#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
import os
from models.review import Review
from datetime import datetime


class test_review(unittest.TestCase):
    """Test cases for review class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.review = Review()
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
        datetime_prev = self.review.updated_at
        self.review.save()
        self.assertGreater(self.review.updated_at, datetime_prev)
        self.assertTrue(os.path.exists("file.json"))

    def test_str_method(self):
        """Test case for str instance representation"""
        cls_name = str(self.review.__class__.__name__)
        obj_dict = str(self.review.__dict__)
        obj_str = "[{}] ({}) {}".format(cls_name, self.review.id, obj_dict)
        self.assertEqual(obj_str, self.review.__str__())

    def test_to_dict_method(self):
        """Test case for 'to_dict' method"""
        dict = {
            "id": self.review.id,
            "__class__": self.review.__class__.__name__,
            "created_at": self.review.created_at.isoformat(),
            "updated_at": self.review.updated_at.isoformat()
        }
        self.assertDictEqual(dict, self.review.to_dict())


if __name__ == "__main__":
    unittest.main()
