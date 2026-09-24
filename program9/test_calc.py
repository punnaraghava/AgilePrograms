
import unittest
from calcy import add

class TestCalculator(unittest.TestCase):

      def test_positive_numbers(self):
            self.assertEqual(add(2, 3), 5)

      def test_negative_numbers(self):
            self.assertEqual(add(-2, -3), -5)

      def test_positive_negative(self):
            self.assertEqual(add(5, -2), 3)

      def test_zero(self):
            self.assertEqual(add(0, 5), 5)

      def test_both_zero(self):
            self.assertEqual(add(0, 0), 0)
 

if __name__ == '__main__':
        unittest.main()
