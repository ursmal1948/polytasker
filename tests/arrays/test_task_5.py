import unittest
from unittest.mock import mock_open, patch
from tasks.arrays.task_5 import read_data_from_file, sort_items


class TestTask5Functions(unittest.TestCase):
    test_cases = [
        ([12, 5, 8, 0, 3], [0, 3, 5, 8, 12]),
        ([5], [5])
    ]

    @patch("builtins.open", new_callable=mock_open, read_data="10.0\n12.8\n17.9\n8.2\n15.0\n")
    def test_read_data_from_file(self, mock_open):
        result = read_data_from_file("test_file2.txt")
        self.assertEqual(result, [10.0, 12.8, 17.9, 8.2, 15.0])

    def test_when_file_has_inorrect_extension(self):
        with self.assertRaises(AttributeError) as e:
            read_data_from_file("tests/arrays/data/test.text")
        self.assertEqual(str(e.exception), "File has incorrect extension")

    def test_when_file_not_found(self):
        with self.assertRaises(FileNotFoundError) as e:
            read_data_from_file("tests/arrays/data/testt.txt")
        self.assertTrue(str(e.exception).startswith("File not found"))

    def test_sort_items(self):
        for test_case in self.test_cases:
            numbers, expected_result = test_case
            with self.subTest(test_case=test_case):
                result = sort_items(numbers)
                self.assertEqual(result, expected_result)
