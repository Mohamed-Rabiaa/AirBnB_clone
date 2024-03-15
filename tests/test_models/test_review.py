#!/usr/bin/env bash
""" This module contains the 'TestReview' class """


import unittest
from models.base_model import BaseModel
from models.review import Review
from models.place import Place
from models.user import User


class TestReview(unittest.TestCase):
    """ This class tests the Review class """

    def setUp(self):
        """ Called before executing the test method """
        pass

    def test_attributes(self):
        """ Tests Review attributes """

        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
