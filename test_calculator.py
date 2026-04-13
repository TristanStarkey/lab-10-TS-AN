#https://github.com/TristanStarkey/lab-11/blob/main/test_calculator.py
# Partner 1: Tristan Starkey
# Partner 2: Arthur Nikitin
import unittest
import math
from calculator import add, subtract, mul, div, modulo, power, square_root, logarithm, exp, hypotenuse


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-2, -5), -7)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(2, 9), -7)
        self.assertEqual(subtract(5, 0), 5)

    def test_multiply(self):
        self.assertEqual(mul(3, 5), 15)
        self.assertEqual(mul(-3, 4), -12)
        self.assertEqual(mul(99, 0), 0)

    def test_divide(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(-9, 3), -3)
        self.assertAlmostEqual(div(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            div(10, 0)

    def test_sqrt(self):
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(0), 0)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))
        with self.assertRaises(ValueError):
            square_root(-4)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(math.e), 1.0)
        self.assertAlmostEqual(logarithm(100, 10), 2.0)
        self.assertAlmostEqual(logarithm(8, 2), 3.0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0)
        with self.assertRaises(ValueError):
            logarithm(-5)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(10, 0)
        with self.assertRaises(ValueError):
            logarithm(10, -1)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(1, 1), math.sqrt(2))


if __name__ == '__main__':
    unittest.main()
