"""
Contains unittests for the base class methods.
"""
import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """Unittest test class for Base class"""

    def setUp(self):
        """Set up resources required to run the tests"""
        self.base_1 = Base()
        self.base_2 = Base(5)
        self.base_3 = Base(-5)

    def test_assign_id(self):
        """Check whether id is assigned automatically if none is provided"""
        self.assertEqual(self.base_1.id, 1)
        self.assertEqual(self.base_2.id, 5)

    def test_assign_negative_id(self):
        self.assertEqual(self.base_3.id, -5)
