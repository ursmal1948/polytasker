import pytest

from tasks.strings.task_2 import (
    does_string_match_regex,
    get_divisors,
    get_pairs_matching_regex,
    replace_digits_with,
    get_digit_divisors,
    digit_to_str
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
        (1, [1]),
        (2, [1, 2]),
        (4, [1, 2, 4]),
        (13, [1, 13]),
        (25, [1, 5, 25]),
        (100, [1, 2, 4, 5, 10, 20, 25, 50, 100])
    ])
    def test_get_divisors(self, number, expected_divisors):
        divisors = get_divisors(number)
        assert divisors == expected_divisors

    @pytest.mark.parametrize("text, custom_regex, expected_result", [
        ("BcYz", r'([A-Z])([a-z])', [('B', 'c'), ('Y', 'z')]),
        ("2a8B9?", r'(\d)([A-Za-z])', [('2', 'a'), ('8', 'B')]),
        ("a2c8", r'([A-Z])([a-z])', [])
    ])
    def test_get_pairs_matching_custom_regex(self, text, custom_regex, expected_result):
        result = get_pairs_matching_regex(text, custom_regex)
        assert result == expected_result

    def test_get_pairs_matching_default_regex(self):
        text = "A3E2Y4c9"
        result = get_pairs_matching_regex(text)
        assert result == [('A', '3'), ('E', '2'), ('Y', '4')]

    def test_replace_digits_with_divisors(self):
        text = "B8A9C4"
        result = replace_digits_with(text, lambda d: get_digit_divisors(d))
        assert result == "B1248A139C124"

    def test_replace_digits_with_string_representation(self):
        text = "A0C3"
        result = replace_digits_with(text, lambda d: digit_to_str(d))
        assert result == "AzeroCthree"
