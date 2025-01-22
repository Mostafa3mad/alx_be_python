import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)        # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)      # Negative and positive
        self.assertEqual(self.calc.add(0, 0), 0)       # Zero
        self.assertEqual(self.calc.add(-5, -5), -10)   # Negative numbers

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)      # Positive numbers
        self.assertEqual(self.calc.subtract(0, 5), -5)     # Zero and positive
        self.assertEqual(self.calc.subtract(-5, -3), -2)   # Negative numbers
        self.assertEqual(self.calc.subtract(3, 5), -2)     # Result is negative

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)         # Positive numbers
        self.assertEqual(self.calc.multiply(-3, 5), -15)       # Negative and positive
        self.assertEqual(self.calc.multiply(0, 5), 0)          # Zero
        self.assertEqual(self.calc.multiply(-3, -5), 15)       # Negative numbers

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)       # Positive numbers
        self.assertEqual(self.calc.divide(-10, 2), -5)     # Negative and positive
        self.assertEqual(self.calc.divide(0, 1), 0)        # Zero numerator

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))         # Division by zero
        self.assertIsNone(self.calc.divide(0, 0))          # Zero divided by zero


if __name__ == "__main__":
    unittest.main()
