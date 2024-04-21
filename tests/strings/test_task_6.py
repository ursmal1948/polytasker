import unittest
from unittest.mock import patch
from tasks.strings.task_6 import (
    generate_string,
    count_feature_occurrences,
    dupliacte_uppercase_letters,
    find_words_starting_with_letter,
    select_representative_word_by_first_letter,
    map_letters_to_representative_words
)


class TestTask6Functions(unittest.TestCase):
    test_cases_feature_occurences = [
        ['ABCDEFG', lambda char: ord(char) % 2 == 0, 3],
        ['ABCDEFG', lambda char: ord(char) % 2 == 1, 4],
        ['HELLO', lambda char: char in 'AEYUIO', 2]
    ]

    @patch("tasks.strings.task_6.rand_chr")
    def test_generate_string(self, mock_gen_str):
        mock_gen_str.side_effect = ['F', 'P', 'H', 'M', 'A', 'L', 'I', 'P', 'K', 'T']
        result = generate_string(10, 'A', 'K', 'L', 'Z')
        self.assertEqual(result, 'FPHMALIPKT')

    def test_default_count_feature_occurences(self):
        text = 'ADFHKO'
        result = count_feature_occurrences(text)
        self.assertEqual(result, 3)

    def test_custom_count_feature_occurences(self):
        for test_case in TestTask6Functions.test_cases_feature_occurences:
            with self.subTest(test_case=test_case):
                text, feature_check, expected_result = test_case
                self.assertEqual(count_feature_occurrences(text, lambda c: feature_check(c)), expected_result)

    def test_duplicate_uppercase_letters(self):
        text = 'A2BCdf!'
        result = dupliacte_uppercase_letters(text)
        self.assertEqual(result, 'aA2bBcCdf!')

    def test_find_words_starting_with_letter(self):
        items = ['APPLE', 'AMBULANSE', 'BANANA']
        self.assertEqual(find_words_starting_with_letter(items, 'A'), ['APPLE', 'AMBULANSE'])
        self.assertEqual(find_words_starting_with_letter(items, 'B'), ['BANANA'])
        self.assertEqual(find_words_starting_with_letter(items, 'C'), [])

    def test_select_representative_words_by_first_letter(self):
        words = ['ALFA', 'BETA', 'GAMMA', 'ACTION']
        result = select_representative_word_by_first_letter(words)
        self.assertEqual(result, {'A': 'ACTION', 'B': 'BETA', 'G': 'GAMMA'})

    def test_map_letters_to_representative_words(self):
        result = map_letters_to_representative_words('PYTHON', 'tests/strings/data/task_6_words.txt')
        self.assertEqual(result, 'PAPAYA|YETI|TANGERINE|HORSERADISH|ORANGE|NECTARINE')
