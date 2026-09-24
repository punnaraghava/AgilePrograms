import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(0, 7), -7)
        self.assertEqual(calculator.subtract(7, 0), 7)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)
        self.assertEqual(calculator.multiply(-2, 5), -10)
        self.assertEqual(calculator.multiply(0, 5), 0)
    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)
        self.assertEqual(calculator.power(5, 0), 1)
        self.assertEqual(calculator.power(0, 5), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(9, 3), 3)
        self.assertAlmostEqual(calculator.divide(1, 3), 0.333333, places=6)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

if __name__ == "__main__":
    unittest.main()