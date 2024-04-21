import math
import unittest
from unittest.mock import patch
from tasks.arrays.task_3 import ArrayGenerator, ArrayOperations, rand_number


class TestArrayGenerator(unittest.TestCase):

    def setUp(self):
        self.array_generator = ArrayGenerator(4, 0, 30)

    def test_rand_number(self):
        with patch("random.randint") as mock_randint:
            mock_randint.return_value = 10

            result = rand_number(0, 30)
            self.assertEqual(result, 10)

    @patch("tasks.arrays.task_3.rand_number")
    def test_generate_unique_numbers(self, rand_number_mock):
        rand_number_mock.side_effect = [0, 10, 20, 30]
        unique_numbers = self.array_generator.generate_unique_numbers()
        self.assertEqual(unique_numbers, [0, 10, 20, 30])


class TestArrayOpeartions(unittest.TestCase):
    test_cases = [
        [lambda num: TestArrayOpeartions.calculate_digits_sum(num), lambda nums: min(nums), 20],
        [lambda num: TestArrayOpeartions.calculate_digits_sum(num), lambda nums: max(nums), 78],
        [lambda num: TestArrayOpeartions.calculate_half_number_factorial(num), lambda nums: min(nums), 13],
        [lambda num: TestArrayOpeartions.calculate_half_number_factorial(num), lambda nums: max(nums), 78],
        [lambda num: TestArrayOpeartions.calculate_odd_digits_sum(num), lambda nums: min(nums), [30, 43]],
        [lambda num: TestArrayOpeartions.calculate_odd_digits_sum(num), lambda nums: max(nums), 78]
    ]

    def setUp(self):
        self.array_operations = ArrayOperations([13, 20, 30, 40, 43, 50, 78])

    @staticmethod
    def calculate_digits_sum(number: int) -> int:
        return sum(int(d) for d in str(number))

    @staticmethod
    def calculate_odd_digits_sum(number: int) -> int:
        return sum(int(d) for d in str(number) if int(d) % 2 == 1)

    @staticmethod
    def calculate_half_number_factorial(number: int) -> int:
        if number < 0:
            raise ValueError("Number must be non-negative")
        half_number = number // 2
        if half_number == 0 or half_number == 1:
            return 1
        return half_number * TestArrayOpeartions.calculate_half_number_factorial(half_number - 1)

    def test_get_minimum_element(self):
        min_element = self.array_operations.get_extreme_element(lambda nums: min(nums))
        self.assertEqual(min_element, 13)

    def test_get_maxinum_element(self):
        max_element = self.array_operations.get_extreme_element(lambda nums: max(nums))
        self.assertEqual(max_element, 78)

    def test_process_elements_based_on_mapper(self):
        for test_case in self.test_cases:
            mapper, finisher, expected_result = test_case
            with self.subTest(test_case=test_case):
                result = self.array_operations.process_elements_based_on_mapper(
                    mapper_fn=lambda num: mapper(num),
                    finisher_fn=lambda nums: finisher(nums)
                )
                self.assertEqual(result, expected_result)
