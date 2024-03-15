#!/usr/bin/env bash
""" This module contains the TestState class """


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ This class tests the State class """

    def setUp(self):
        """ called before executing the test method """
        pass

    def test_attribute(self):
        """ Tests the name attribute """
        self.assertEqual(State.name, "")
