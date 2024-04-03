import os.path
import unittest
import pytest
from tasks.strings.task_3 import has_even_odd_ascii_pattern, swap_chars, save_to_file


class TestTask3Functions:
    @pytest.mark.parametrize("text, expected_result", [
        ("", False),
        ("A", False),
        ("EF", False),
        ("BADC", True),
    ])
    def test_has_even_odd_ascii_pattern(self, text, expected_result):
        result = has_even_odd_ascii_pattern(text)
        assert result == expected_result

    @pytest.mark.parametrize("text, expected_swapped_text", [
        ("A", "A"),
        ("EFGH", "FEHG"),
        ("ABCDE", "BADCE"),
    ])
    def test_swap_chars(self, text, expected_swapped_text):
        swapped_text = swap_chars(text)
        assert swapped_text == expected_swapped_text


class TestSaveToFileFunction(unittest.TestCase):
    def setUp(self):
        self.test_text = "This is a test"
        self.test_filename = "../data/test_file.txt"

    def test_save_to_file(self):
        save_to_file(self.test_filename, self.test_text)
        self.assertTrue(os.path.exists(self.test_filename))

        with open(self.test_filename, 'r') as f:
            self.assertEqual(f.read(), self.test_text)
