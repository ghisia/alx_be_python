import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.addition(2, 3), 5)
        self.assertEqual(self.calc.addition(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtraction(5, 3), 2)
        self.assertEqual(self.calc.subtraction(3, 5), -2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 0), None)

if __name__ == "__main__":
    unittest.main()
