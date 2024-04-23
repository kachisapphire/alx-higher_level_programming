#!/usr/bin/python3
""" unittest for base.py. """
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Unittest to test all edge cases of base.py. """
    def test_noarg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_threearg(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_noid(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_uniqueid(self):
        b1 = Base()
        b2 = Base(10)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id(self):
        self.assertEqual(10, Base(10).id)

    def test_private_instance(self):
        with self.assertRaises(AttributeError):
            print(Base(10).__nd_instances)

    def test_public_instance(self):
        b1 = Base(10)
        b1.id = 5
        self.assertEqual(5, b1.id)

    def test_float(self):
        self.assertEqual(2.5, Base(2.5).id)

if __name__ == "__main__":
    unittest.main()
