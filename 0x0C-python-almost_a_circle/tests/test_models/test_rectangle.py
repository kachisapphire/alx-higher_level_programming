#!/usr/bin/python3
""" Unittest for rectangle.py. """
import unittest
import os
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Unittest for rectangle. contains test cases for
    about 4-5 tasks in the project. """
    def test_rectangle(self):
        self.assertIsInstance(Rectangle(2, 4), Base)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_three(self):
        r1 = Rectangle(1, 2, 1)
        r2 = Rectangle(4, 8, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_argone(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_id_arg(self):
        self.assertEqual(1, Rectangle(2,4,6,8,1).id)

    def test_six_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__width)

    def test_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__height)

    def test_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__x)

    def test_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__y)

    def test_setter_for_width(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.width = 9
        self.assertEqual(9, r.width)

    def test_getter_width(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(1, r.width)

    def test_height_getter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(2, r.height)

    def test_setter_for_height(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.height = 8
        self.assertEqual(8, r.height)

    def test_x_getter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(3, r.x)

    def test_setter_for_x(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.y = 6
        self.assertEqual(6, r.x)

    def test_y_getter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(4, r.y)

    def test_setter_for_y(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.y = 8
        self.assertEqual(8, r.y)


class TestWidthErrors(unittest.TestCase):
    """ Unittest to check for possible errors. """
    def test_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.2, 8)

    def test_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("school", 2)

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((2, 4, 6), 4)

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([2, 4, 6], 4)

    def test_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 6)

    def test_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 7)

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"key": 4, "two": 4}, 5)

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 8)


class TestHeightErrors(unittest.TestCase):
    """ unittest to check for possible errors. """
    def test_none_error(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_float_error(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, 2.7)

    def test_string_error(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "school")

    def test_tuple_error(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, (2, 3, 4))

    def test_list_error(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, [6, 7, 9])

    def test_bool_error(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, True)

    def test_zero_error(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(6, 0)

    def test_dict_error(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, {"one": 1, "two": 2})

    def test_negative_error(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(8, -9)

    def test_nan_error(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, float('nan'))


class TestX(unittest.TestCase):
    """ Unittest to handle errors. """
    def test_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 8, None)

    def test_X_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 8, "new")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 8, 2.9)

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 8, (5, 6, 7))

    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 8, [9, 8, 7])

    def test_x_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 8, True)

    def test_x_negative(self):
        with self.assertRaisesRegex(valueError, "x must be >= 0"):
            Rectangle(9, 8, -2)

    def test_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 8, {"one": 1, "two": 4})


class TestY(unittest.TestCase):
    """ This checks errors of y. """
    def test_none_y:
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 9, 2, None)

    def test_string_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(9, 9, 2, "alx")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 9, 2, 2.8)

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 9, 2, {"one": 4, "six": 8})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 9, 2, [4, 5, 7])

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 9, 2, (3, 8, 9))

    def test_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 9, 2, range(8))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(7, 9, 2, -3)

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 9, 2, float('nan'))


class TestRectangle_Area_Display(unittest.TestCase):
    """ This checks for the static method area. """
    def test_private(self):
        r = Rectangle(2, 4, 6, 8, 9)
        self.assertEqual(8, r.area())

    def test_set_attribute(self):
        r = Rectangle(2, 4, 6, 8, 1)
        r.width = 8
        r.height = 2
        self.assertEqual(16, r.area())

    def test_one_args(self):
        r = Rectangle(2, 4, 6, 8, 9)
        with self.assertRaisesRegex(TypeError):
            r.area(1)
