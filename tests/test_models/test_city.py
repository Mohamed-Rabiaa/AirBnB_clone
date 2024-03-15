#!/usr/bin/env bash
""" This module contains the 'TestCity' class """


import unittest
from models.city import City
from models.base_model import BaseModel
from models.state import State


class TestCity(unittest.TestCase):
    """ This class tests the City class """

    def setUp(self):
        """ Called before executing the test method """
        pass

    def test_attributes(self):
        """ Tests city attributes """
        City.state_id = None
        City.name = None

        self.assertEqual(City.state_id, None)
        self.assertEqual(City.name, None)
