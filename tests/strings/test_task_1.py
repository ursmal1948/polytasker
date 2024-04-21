import unittest
from unittest.mock import patch
from tasks.strings.task_1 import get_string, count_chars, get_strings_until_same_chars_count, \
    rearrange_group1_group2_chars


class TestTask1(unittest.TestCase):
    chars_counter_cases = [
        ["HAPPY SONG", r'[AEYUIO]', 3],
        ["HAPPY SONG", r'[^AEYUIO\s]', 6],
        ["One two three 1 2 3", r'\d', 3],
        ['Hello world', r'\d', 0],
        ["?^%A", r'\w', 1]
    ]
    rearrangement_cases = [
        ["GARDEN", "AEY", "GRDN", "AEGRDN"],
        ["HELLO", "AEYUIO", "123456", "EO"],
        ["APPLE", "123", "456", ""],
    ]

    @patch("builtins.input", return_value="apple")
    def test_get_string(self, mock_input):
        result = get_string("Enter a string")
        self.assertEqual(result, "apple")

    @patch("builtins.input", return_value="")
    def test_get_string_empty(self, mock_input):
        result = get_string("Enter a string")
        self.assertEqual(result, "")

    def test_count_chars(self):
        for char_counter_case in self.chars_counter_cases:
            with self.subTest(char_counter_case=char_counter_case):
                text, regex, expected_chars_count = char_counter_case
                chars_count = count_chars(text, regex)
                self.assertEqual(chars_count, expected_chars_count)

    def test_rearrange_group1_group2_chars(self):
        for rearrangement_case in self.rearrangement_cases:
            with self.subTest(rearrangement_case):
                text, group1, group2, expected_result = rearrangement_case
                result = rearrange_group1_group2_chars(text, group1, group2)
                self.assertEqual(result, expected_result)

    def test_get_strings_until_same_vowels_count(self):
        count = 4
        with patch("tasks.strings.task_1.get_string") as mock_get_string:
            mock_get_string.side_effect = ["hello", "apple", "pears", "lemon"]
            result = get_strings_until_same_chars_count(
                message="Get string",
                count=count,
                regex="[aeyuio]",
                chars_count_fn=lambda text, regex: count_chars(text, regex)
            )
            self.assertEqual(result, "helloapplepearslemon")

    def test_get_strings_until_same_digits_count(self):
        count = 2
        with patch("tasks.strings.task_1.get_string") as mock_get_string:
            mock_get_string.side_effect = ["one12", "two34"]
            result = get_strings_until_same_chars_count(
                message="Get string",
                count=count,
                regex=r'\d',
                chars_count_fn=lambda text, regex: count_chars(text, regex)
            )
            self.assertEqual(result, "one12two34")
