#!/usr/bin/python3
""" a Unittest module. """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ unittest for max_interger. """
    def test_list_inorder(self):
        """ test for a list in order. """
        list1 = [2, 4, 6, 8]
        self.assertEqual(max_integer(list1), 8)

    def test_list_notorder(self):
        """ test case for a lsit not in order. """
        list2 = [4, 2, 8, 6]
        self.assertEqual(max_integer(list2), 8)

    def test_maxfirst(self):
        """ test case for max at beginning of the list. """
        list_first = [8, 4, 6, 2]
        self.assertEqual(max_integer(list_first), 8)

    def test_empty(self):
        """ test to check an empty list. """
        list_emp = []
        self.assertEqual(max_integer(list_emp), None)

    def test_not_empty(self):
        """ test for a list with one element. """
        one_elem = [4]
        self.assertEqual(max_integer(one_elem), 4)

    def test_float_element(self):
        """ test case for floats. """
        float_elem = [1.2, 3.87, 12.9, 0.3]
        self.assertEqual(max_integer(float_elem), 12.9)

    def test_mix_element(self):
        """ test case for float and integer. """
        int_float = [2, 2.3, 4, 5.7]
        self.assertEqual(max_integer(int_float), 5.7)

    def test_strings(self):
        """ test case for list of strings. """
        str_list = ["me", "rat", "book", "we"]
        self.assertEqual(max_integer(str_list), "we")


if __name__ == "__main__":
    unittest.main()
