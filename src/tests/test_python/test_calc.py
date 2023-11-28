
import sys
import os
from unittest import TestCase

current_dir = os.path.dirname(os.path.abspath(__file__))

project_root = os.path.join(current_dir, '../..')

sys.path.append(project_root)

from main.python.calc import add, subtract, multiply, divide


class TestCalculator(TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(7, 2), 14)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(divide(8, 0), "Cannot divide by zero!")


sys.path.remove(project_root)
