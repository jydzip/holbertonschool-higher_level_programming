#!/usr/bin/python3
"""
    Unittest for max_integer.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        Tests for the function max_integer.
    """

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 5, 4]), 5)

    def test_max_integer_negation(self):
        self.assertEqual(max_integer([-1, -2, -3, -5, -4]), -1)

    def test_max_integer_with_negation(self):
        self.assertEqual(max_integer([-1, 0, -3, 5, 1]), 5)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_zero(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_one_number(self):
        self.assertEqual(max_integer([1]), 1)

    def test_error_is_string(self):
        with self.assertRaises(TypeError):
            max_integer([0, "1"])

    def test_error_is_list_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, [10, 20]])

    def test_error_is_tuple(self):
        with self.assertRaises(TypeError):
            max_integer([0, (1, 2)])

    def test_error_is_number(self):
        with self.assertRaises(TypeError):
            max_integer(5)
