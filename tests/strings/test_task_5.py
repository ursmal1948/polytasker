import unittest
from unittest.mock import patch

from tasks.strings.task_5 import CharacterPair


class TestTask5Functions(unittest.TestCase):
    def setUp(self):
        self.character_pair = CharacterPair("a", "b")

    test_cases = [
        ["abba", "abab"],
        ["aabbaa", "ababaa"],
        ["abb", "abb"]

    ]

    @patch("tasks.strings.task_5.CharacterPair.generate_balanced_string")
    def test_generate_balanced_string(self, mock_fn):
        mock_fn.return_value = "ababa"
        self.assertEqual(
            self.character_pair.generate_balanced_string(5),
            "ababa")

    def test_alternate_chars(self):
        for test_case in self.test_cases:
            with self.subTest(test_case=test_case):
                text, expected_result = test_case
                result = self.character_pair.alternate_chars(text)
                self.assertEqual(result, expected_result)

    def test_alternate_chars_not_present_chars(self):
        with self.assertRaises(ValueError) as e:
            text = "HELLO"
            self.character_pair.alternate_chars(text)
        self.assertTrue(str(e.exception).endswith('must be present in the text.'))
