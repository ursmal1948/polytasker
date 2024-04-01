import pytest

from tasks.strings.task_2 import (
    does_string_match_regex,
    get_divisors,
    replace_digits_with_divisors
)


class TestTask2Functions:
    @pytest.mark.parametrize("text, regex, expected_result", [
        ["a1b4c7", r'^([a-z]\d)+$', True],
        ["A562B1", r'^([A-Z]\d{2})+$', False],
        ['hello world', r'([a-z]+ [a-z]+)+[a-z]', True],
        ["d", r'^[^abc]$', True],
        ["_2", r'^\w{2}$', True]
    ])
    def test_custom_regex(self, text, regex, expected_result):
        result = does_string_match_regex(text, regex)
        assert result == expected_result

    @pytest.mark.parametrize("text,expected_result", [
        ["A2B8C9", True],
        ["a9c8", False],
        ["8b7a", False],
    ])
    def test_default_regex(self, text, expected_result):
        assert does_string_match_regex(text) == expected_result

    @pytest.mark.parametrize("number, expected_divisors", [
        (0, float("inf")),
        (1, 1),
        (2, [1, 2]),
        (4, [1, 2, 4]),
        (13, [1, 13]),
        (25, [1, 5, 25]),
        (100, [1, 2, 4, 5, 10, 20, 25, 50, 100])
    ])
    def test_get_divisors(self, number, expected_divisors):
        divisors = get_divisors(number)
        assert divisors == expected_divisors

    @pytest.mark.parametrize("text, expected_modified_text", [
        ("A0", "A151365"),
        ("B3", "B611223366"),
        ("X9", "X11224488")
    ])
    def test_replace_digits_with_divisors(self, text, expected_modified_text):
        modified_text = replace_digits_with_divisors(text)
        assert modified_text == expected_modified_text
