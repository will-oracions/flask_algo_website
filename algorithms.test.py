import unittest
from algorithms import calculate_factorial, is_prime

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

    # Exercice: 10
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))

    # Exercice 11
    def test_are_amicable_numbers(self):
        self.assertTrue(are_amicable_numbers(220, 284))
        self.assertTrue(are_amicable_numbers(1184, 1210))
        self.assertFalse(are_amicable_numbers(220, 285))
        self.assertFalse(are_amicable_numbers(1184, 1211))

if __name__ == '__main__':
    unittest.main()
