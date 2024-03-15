#!/usr/bin/python3


"""Unittest for User."""


import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ This class tests the User class """ 
    def setUp(self):
        """ Called before executing the test method """
        pass
        
    def test_attributes(self):
        """ Tests User attributes """
        User.email = "au@gmail.com"
        User.password = "12345678"
        User.first_name = "John"
        User.last_name = "Smith"

        self.assertEqual(User.email, "au@gmail.com")
        self.assertEqual(User.password, "12345678")
        self.assertEqual(User.first_name, "John")
        self.assertEqual(User.last_name, "Smith")
