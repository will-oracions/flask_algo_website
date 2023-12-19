import unittest
from algorithms import calculate_factorial

class TestAlgorithms(unittest.TestCase):
    def test_factorial_of_0(self):
        result = calculate_factorial(0)
        self.assertEqual(result, 1)

    def test_factorial_of_1(self):
        result = calculate_factorial(1)
        self.assertEqual(result, 1)

    def test_factorial_of_positive_number(self):
        result = calculate_factorial(5)
        self.assertEqual(result, 120)

    def test_factorial_of_negative_number(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-3)

if __name__ == '__main__':
    unittest.main()
