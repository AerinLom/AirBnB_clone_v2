#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import os


class test_User(test_basemodel):
    """ test class for user model"""

    def __init__(self, *args, **kwargs):
        """ user test class init"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ testing user first name attr"""
        new = self.value()
        expected_type = (
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
        self.assertEqual(type(new.first_name), expected_type)

    def test_last_name(self):
        """ testing user last name attr"""
        new = self.value()
        expected_type = (
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
        self.assertEqual(type(new.last_name), expected_type)

    def test_email(self):
        """ testing user email attr"""
        new = self.value()
        expected_type = (
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
        self.assertEqual(type(new.email), expected_type)

    def test_password(self):
        """ testing user password attr"""
        new = self.value()
        expected_type = (
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
        self.assertEqual(type(new.password), expected_type)
