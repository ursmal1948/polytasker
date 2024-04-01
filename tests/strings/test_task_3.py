import unittest
from unittest.mock import patch
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


class TestFileFunction(unittest.TestCase):
    def test_save_to_file(self):
        with patch("builtins.open") as mock_open:
            filename = "encrypted.txt"
            text = "HELLO"

            save_to_file(filename, text)
            mock_open.assert_called_once_with(filename, "w")
