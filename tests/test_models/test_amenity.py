#!/usr/bin/env bash
""" This module contains the 'TestAmenity' class """


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ This class tests the Amenity class """

    def setUp(self):
        """ Called before executing the test method """
        pass

    def test_attributes(self):
        """ Tests Amenity attributes """
        Amenity.name = "Wifi"

        self.assertEqual(Amenity.name, "Wifi")
