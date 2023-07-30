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
    def test_access_nested_map_exception(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function with invalid paths that should raise exceptions.

        Args:
            nested_map (dict): The nested dictionary to search.
            path (tuple): A tuple of keys representing the path to the desired value.
            expected_result: The expected exception type raised by the access_nested_map function.

        Returns:
            None: This method does not return anything explicitly.
        """
        with self.assertRaises(expected_result) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test case class to test the get_json function.
    """

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    def test_get_json(self, url, expected_output):
        """
        Test the get_json function with different URLs.

        Args:
            url (str): The URL to fetch JSON data from.
            expected_output (dict): The expected JSON data.

        Returns:
            None: This method does not return anything explicitly.
        """
        mock_response = Mock()
        mock_response.json.return_value = expected_output
        with patch('requests.get', return_value=mock_response):
            response = get_json(url)
            self.assertEqual(response, expected_output)


class TestMemoize(unittest.TestCase):
    """
    Test case class to test the memoize decorator.
    """

    def test_memoize(self):
        """
        Test the memoize decorator.

        Returns:
            None: This method does not return anything explicitly.
        """

        class TestClass:
            """
            A test class to demonstrate the use of the memoize decorator.
            """

            def a_method(self):
                """
                A method to simulate a computation.

                Returns:
                    int: The result of the computation (constant value for this example).
                """
                return 42

            @memoize
            def a_property(self):
                """
                A property decorated with the memoize decorator.
                This property will be memoized, i.e., the computation is performed only once.

                Returns:
                    int: The result of the a_method call.
                """
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
