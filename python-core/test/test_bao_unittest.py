#-*- coding:utf-8 -*-

import unittest
from unittest.bao_unittest import *

class TestBaoUnittest(unittest.TestCase):
    """
    """
    # def setUp(self):
    #     print("do Something before test")
    #
    # def tearDown(self):
    #     print("do Something after test")
    # @classmethod
    # def setUpClass(cls):
    #     print("do Something before test only once")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("do Something after test only once")

    def test_add(self):
        self.assertEqual(3, add(1,2))
        self.assertEqual(4, add(2,2))

    def test_divide(self):
        self.assertEqual(2, divide(2,1))

    def test_mins(self):
        self.assertEqual(1, mins(3,2))

if __name__ == "__main__":
    unittest.main()