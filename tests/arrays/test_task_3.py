import unittest
from unittest.mock import patch
from tasks.arrays.task_3 import ArrayGenerator, ArrayOperations


class TestArrayGenerator(unittest.TestCase):

    def setUp(self):
        self.array_generator = ArrayGenerator(4, 0, 30)

    @patch("tasks.arrays.task_3.rand_number")
    def test_generate_unique_numbers(self, rand_number_mock):
        rand_number_mock.side_effect = [0, 10, 20, 30]  # Seeding the mock with specific values
        unique_numbers = self.array_generator.generate_unique_numbers()
        self.assertEqual(unique_numbers, [0, 10, 20, 30])


class TestArrayOpeartions(unittest.TestCase):
    def setUp(self):
        self.array_operations = ArrayOperations([10, 20, 30, 40, 50])

    def test_get_minimum_element(self):
        min_element = self.array_operations.get_extreme_element(lambda nums: min(nums))
        self.assertEqual(min_element, 10)

    def test_get_maxinum_element(self):
        max_element = self.array_operations.get_extreme_element(lambda nums: max(nums))
        self.assertEqual(max_element, 50)
