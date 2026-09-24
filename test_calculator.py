import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(6, 4), 10)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(4, 6), 24)
        self.assertEqual(calculator.multiply(3, 9), 27)
        self.assertEqual(calculator.multiply(5, 5), 25)

    def test_divide(self):
        # Removed the conflicting 6/0 check
        self.assertEqual(calculator.divide(10, 2),5)
        self.assertAlmostEqual(calculator.divide(1, 3), 0.3333333, places=6)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()