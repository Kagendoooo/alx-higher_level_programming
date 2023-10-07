#!/usr/bin/python3

"""Unittest for max_integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer"""

    def test_ordered(self):
        """Test an ordered list of integers."""
        i = [4, 5, 6, 7]
        self.assertEqual(max_integer(i), 7)

    def test_unordered(self):
        """Test an unordered list of integers."""
        i = [4, 5, 7, 6]
        self.assertEqual(max_integer(i), 7)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        i = [8, 7, 6, 5]
        self.assertEqual(max_integer(i), 8)

    def test_empty(self):
        """Test an empty list."""
        i = []
        self.assertEqual(max_integer(i), None)

    def test_one_element(self):
        """Test a list with a single element."""
        i = [3]
        self.assertEqual(max_integer(i), 3)

    def test_floats(self):
        """Test a list of floats."""
        i = [4.53, 7.83, -9.00, 15.1, 5.0]
        self.assertEqual(max_integer(i), 15.1)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        i = [4.53, 7.83, 9, 15.1, 5]
        self.assertEqual(max_integer(i), 15.1)

    def test_string(self):
        """Test a string."""
        i = "None"
        self.assertEqual(max_integer(i), 'o')

    def test_list_of_strings(self):
        """Test a list of strings."""
        i = ["Faith", "is", "in", "ALX"]
        self.assertEqual(max_integer(i), "is")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
