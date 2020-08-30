from django.test import TestCase

from .calc import add, subtract


class CalcTest(TestCase):

    def test_add_numbers(self):
        """test that 2 numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_umber(self):
        """values are subtracted and returned"""
        self.assertEqual(subtract(8, 3), 5)
