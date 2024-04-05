import unittest
from unittest.mock import patch
from tasks.numbers.task_2 import draw_and_process_number_with_condition, is_palindrome
from algohub.algorithms.numbers.primes import is_prime_basic


class TestTask2Functions(unittest.TestCase):
    test_palindrome_cases = [
        [1, True],
        [424, True],
        [123, False],
    ]

    def test_is_palindrome(self):
        for test_palindrome_case in self.test_palindrome_cases:
            number, expected_result = test_palindrome_case
            result = is_palindrome(number)
            self.assertEqual(result, expected_result)

    def test_draw_and_process_number_until_palindrome(self):
        with patch("random.randint") as mock_randint:
            mock_randint.return_value = 878
            number = draw_and_process_number_with_condition()
            self.assertEqual(number, 878)

    def test_draw_and_process_number_with_custom_handlers(self):
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 523
            result = draw_and_process_number_with_condition(
                condition_fn=lambda num: is_prime_basic(num),
                finisher_fn=lambda num: sum(int(d) for d in str(num)))
            self.assertEqual(result, 10)
