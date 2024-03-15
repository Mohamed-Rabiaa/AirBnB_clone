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

        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
