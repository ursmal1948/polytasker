import unittest
from unittest.mock import patch
from tasks.strings.task_1 import get_string, count_vowels, get_strings, rearrange_vowels_consonants


class TestTask1(unittest.TestCase):
    vowels_count = [
        ("Queue", 4),
        ("garden", 2),
        ("hello world everyone", 8),
        ("Brr", 0)
    ]
    rearrangement = [
        ("Clear", "eaClr"),
        ("sunny day", "uyaysnnd"),
        ("aeyu", "aeyu"),
        ("bcdf", "bcdf")
    ]

    @patch("builtins.input", return_value="apple")
    def test_get_string(self, mock_input):
        result = get_string("Enter a string")
        self.assertEqual(result, "apple")

    @patch("builtins.input", return_value="")
    def test_get_string_empty(self, mock_input):
        result = get_string("Enter a string")
        self.assertEqual(result, "")

    def test_count_vowels(self):
        for text, exp_vowels_count in self.vowels_count:
            with self.subTest(text=text):
                vowels_count = count_vowels(text)
                self.assertEqual(vowels_count, exp_vowels_count)

    def test_rearrange_vowels_consontants(self):
        for text, exp_rearranged_text in self.rearrangement:
            with self.subTest(text=text):
                rearranged_text = rearrange_vowels_consonants(text)
                self.assertEqual(rearranged_text, exp_rearranged_text)
