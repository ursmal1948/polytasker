import pytest
from tasks.strings.task_4 import (
    read_from_file,
    get_common_words,
    chars_1_group_exceeds_chars_2_group_count,
    create_string_from_file
)


@pytest.fixture
def file_path():
    return '/Users/python/Desktop/dev/PROJEKTY_GIT/polytasker/tests/strings/data/words.txt'


class TestTask4Functions:

    def test_read_from_file(self, file_path):
        words = read_from_file(file_path)
        expected_words = ["banana", "note", "tomato", "potato", "wheel"]
        assert words == expected_words

    @pytest.mark.parametrize("words_1, words_2, expected_common_words", [
        (["sun", "ball", "eye", "pen"], ["eye", "sun"], ["sun", "eye"]),
        (["eye"], ["sun"], [])
    ])
    def test_get_common_words(self, words_1, words_2, expected_common_words):
        common_words = get_common_words(words_1, words_2)
        assert common_words == expected_common_words

    @pytest.mark.parametrize("text, expected_result", [
        ("WORLD", True),
        ("QUEUES", False),
        ("PEAR", False)
    ])
    def test_consonants_exceeds_vowels_count(self, text, expected_result):
        result = chars_1_group_exceeds_chars_2_group_count(text)
        assert result == expected_result

    @pytest.mark.parametrize("text, regex_1, regex_2, expected_result", [
        ("A28123C", r'\d', r'[a-z]', True),
        ("??az", r'[a-z]', r'\?', False),
        ("A123", r'[A-Z]', r'\d', False)
    ])
    def test_group_1_chars_exceeds_group_2_chars_count(self, text, regex_1, regex_2, expected_result):
        result = chars_1_group_exceeds_chars_2_group_count(text, regex_1, regex_2)
        assert result == expected_result

    def test_create_string_from_file(self, file_path):
        separator = ","
        items = create_string_from_file(file_path, separator)
        assert items == 'banana,note,potato,tomato,wheel'
