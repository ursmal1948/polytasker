import unittest
from unittest.mock import patch
import pytest

from tasks.numbers.task_3 import (
    generate_n_unique_numbers,
    count_pairs_meeting_condition,
    is_consecutive_pair,
    is_palindromic_pair,
    is_sum_prime
)


class TestTask3Functions(unittest.TestCase):

    def test_generate_n_unique_numbers(self):
        with patch("random.randint") as mock_random:
            mock_random.side_effect = [11, 20, 35, 60]
            numbers = generate_n_unique_numbers(4, 10, 50)
            self.assertEqual(sorted(numbers), [11, 20, 35, 60])

    def test_is_palindromic_pair(self):
        num1, num2 = 102, 201
        result = is_palindromic_pair(num1, num2)
        self.assertTrue(result)

    def test_is_consecutive_pair(self):
        num1, num2, = 3, 4
        self.assertTrue(is_consecutive_pair(num1, num2))

    def test_is_sum_prime(self):
        num1, num2 = 3, 8
        self.assertTrue(is_sum_prime(num1, num2))


class TestCountPairsMeetingCondition:
    @pytest.mark.parametrize("numbers, condition_fn, expected_count", [
        (
                [201, 58, 38, 32, 83, 102, 5],
                lambda num1, num2: is_palindromic_pair(num1, num2),
                2,
        ),
        (
                [1, 3, 4, 8, 10, 12, 9, 11],
                lambda num1, num2: is_consecutive_pair(num1, num2),
                5
        ),
        (
                [1, 9, 10, 6],
                lambda num1, num2: is_sum_prime(num1, num2),
                3
        )
    ])
    def test_count_pairs_meeting_condition(self, numbers, condition_fn, expected_count):
        count = count_pairs_meeting_condition(numbers, condition_fn)
        assert count == expected_count
