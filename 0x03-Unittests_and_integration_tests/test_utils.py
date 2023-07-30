#!/usr/bin/env python3
"""Familiarize yourself with the utils.access_nested_map function and
understand its purpose. Play with it in the Python console to make
sure you understand.

In this task you will write the first unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test that
the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function for
ollowing inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case class to test the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function with various inputs.

        Args:
            nested_map (dict): The nested dictionary to search.
            path (tuple): A tuple of keys representing the path to the desired value.
            expected_result: The expected result from the access_nested_map function.

        Returns:
            None: This method does not return anything explicitly.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

@parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        """
        Test the access_nested_map function with invalid paths that should raise KeyError.

        Args:
            nested_map (dict): The nested dictionary to search.
            path (tuple): A tuple of keys representing the path to the desired value.
            expected_exception (type): The expected exception type to be raised.

        Returns:
            None: This method does not return anything explicitly.
        """
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)

        # Verify the exception message (optional but recommended)
        if expected_exception is KeyError:
            expected_message = f"Key not found: {path[-1]}"
            self.assertEqual(str(context.exception), expected_message)
