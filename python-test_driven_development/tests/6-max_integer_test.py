#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""
    
    def test_ordered_list(self):
        """Test an ordered list of integers"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)
    
    def test_unordered_list(self):
        """Test an unordered list of integers"""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)
    
    def test_max_at_beginning(self):
        """Test a list with max at the beginning"""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)
    
    def test_max_at_end(self):
        """Test a list with max at the end"""
        max_at_end = [1, 2, 3, 4]
        self.assertEqual(max_integer(max_at_end), 4)
    
    def test_max_in_middle(self):
        """Test a list with max in the middle"""
        max_in_middle = [1, 4, 3, 2]
        self.assertEqual(max_integer(max_in_middle), 4)
    
    def test_one_element_list(self):
        """Test a list with single element"""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)
    
    def test_empty_list(self):
        """Test an empty list"""
        empty = []
        self.assertIsNone(max_integer(empty))
    
    def test_negative_numbers(self):
        """Test a list of negative numbers"""
        negative = [-1, -2, -3, -4]
        self.assertEqual(max_integer(negative), -1)
    
    def test_mixed_numbers(self):
        """Test a list of mixed positive and negative numbers"""
        mixed = [1, -2, 3, -4]
        self.assertEqual(max_integer(mixed), 3)
    
    def test_float_numbers(self):
        """Test a list of floating numbers"""
        floats = [1.5, 2.7, 3.3, 4.9]
        self.assertEqual(max_integer(floats), 4.9)
    
    def test_mixed_int_float(self):
        """Test a list of mixed integers and floats"""
        mixed = [1, 2.5, 3, 4.2]
        self.assertEqual(max_integer(mixed), 4.2)
    
    def test_duplicate_max(self):
        """Test a list with duplicate maximum values"""
        duplicates = [1, 4, 3, 4, 2]
        self.assertEqual(max_integer(duplicates), 4)
    
    def test_large_list(self):
        """Test a large list"""
        large = list(range(1000))
        self.assertEqual(max_integer(large), 999)
    
    def test_string_in_list(self):
        """Test a list containing a string (should raise TypeError)"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three", 4])
    
    def test_none_as_argument(self):
        """Test None as argument (should raise TypeError)"""
        with self.assertRaises(TypeError):
            max_integer(None)
    
    def test_string(self):
        """Test a string (iterable of characters)"""
        string = "Hello"
        self.assertEqual(max_integer(string), 'o')
    
    def test_list_of_strings(self):
        """Test a list of strings"""
        strings = ["apple", "banana", "cherry"]
        self.assertEqual(max_integer(strings), "cherry")


if __name__ == '__main__':
    unittest.main()
