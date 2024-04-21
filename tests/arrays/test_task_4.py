import unittest
from unittest.mock import patch
from algohub.algorithms.numbers.digits import sum_digits
from algohub.algorithms.numbers.primes import is_prime_basic

from tasks.arrays.task_4 import (
    generate_n_numbers_until_predicate,
    process_n_extreme_elements,
    get_highest_n_elements,
)


class TestTask4Functions(unittest.TestCase):

    def test_generate_n_numbers_until_default_predicate(self):
        with patch("random.randint") as mock_random:
            mock_random.side_effect = [82, 78, 33, 46]
            result = generate_n_numbers_until_predicate(
                size=4, r_min=10, r_max=100)
            self.assertEqual(result, [82, 78, 33, 46])

    def test_generate_n_numbers_until_custom_predicate(self):
        with patch("random.randint") as mock_random:
            mock_random.side_effect = [104, 113, 200, 166]
            result = generate_n_numbers_until_predicate(
                size=4, r_min=100, r_max=200,
                predicate_fn=lambda num: is_prime_basic(sum_digits(num)))
            self.assertEqual(result, [104, 113, 200, 166])

    def test_get_highest_n_elements(self):
        numbers = [10, 20, 30, 40, 50, 60]
        count = 4
        expeced_result = [30, 40, 50, 60]
        self.assertEqual(get_highest_n_elements(numbers, count), expeced_result)

    def test_process_n_extreme_elements(self):
        numbers = [100, 120, 80, 120, 60, 150]
        count = 3
        expected_result = process_n_extreme_elements(numbers, 3)
        self.assertEqual(process_n_extreme_elements(numbers, count), expected_result)

    def test_process_n_extreme_elements_raises_error(self):
        with self.assertRaises(ValueError) as e:
            result = process_n_extreme_elements(
                numbers=[10, 20],
                count=5,
            )
        self.assertEqual(str(e.exception), "Not enough numbers in a list")
