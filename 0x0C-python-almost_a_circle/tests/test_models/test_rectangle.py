#!/usr/bin/python3
"""Test Rectangle class"""
import unittest
from models.base import Base


class test_Rectangle(unittest.TestCase):
    """ Test Rectangle """

    def test_create_rect(self):
        """ test """
        b1 = Base()
        self.assertEqual(b1.id, 1)
