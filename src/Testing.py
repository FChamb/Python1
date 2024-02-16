import IntricateInteger
import sys
import unittest
import random


class Testing(unittest.TestCase):
    def setUp(self):
        self.obj = [i for i in range(10)]
        self.n = [i for i in range(10)]
        self.alpha = [i for i in range(10)]
        self.i = 0

    def test_alpha0(self):
        x = IntricateInteger.IntricateInteger(0, 7, 2)
        y = IntricateInteger.IntricateInteger(0, 1, 2)
        #self.assertEqual(x * y, )