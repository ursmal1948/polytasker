import unittest
from unittest.mock import patch

from tasks.numbers.task_4 import (
    get_positive_int,
    get_numbers_until_predicate,
    get_digit,
    is_condition_met,
    is_digits_sum_even_and_units_greater_than_tens_sum
)


class TestTask4Functions(unittest.TestCase):
    test_cases = [
        (1, 4, True),
        (123, 127, True),
        (102, 111, False)
    ]

    def test_get_positive_int(self):
        with patch("builtins.input") as mock_input:
            mock_input.return_value = 10
            number = get_positive_int("Enter positive integer")
            self.assertEqual(number, 10)

    def test_get_numbers_until_predicate(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = [10, 20]
            result = get_numbers_until_predicate(predicate_fn=lambda n1, n2: n1 + n2 > 20)
            self.assertEqual(result, (10, 20))

    def test_is_digits_sum_even_and_units_greater_than_tens_sum(self):
        for test_case in self.test_cases:
            a, b, expected_result = test_case
            with self.subTest(a=a):
                result = is_digits_sum_even_and_units_greater_than_tens_sum(a, b)
                self.assertEqual(result, expected_result)

    def test_is_condition_met(self):
        a, b = 8, 4
        result = is_condition_met(a, b, lambda n1, n2: (n1 + n2) % 2 == 0)
        self.assertTrue(result)
