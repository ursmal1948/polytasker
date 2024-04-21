import pytest

from tasks.oop.task_2 import Row, Numbers


class TestRowMethods:
    def test_when_raises_error(self):
        with pytest.raises(ValueError) as e:
            Row.parse('A;B;C')
        assert str(e.value).startswith("Line does not match regex")

    def test_when_correct_data(self):
        row = Row.parse('1;2;3')
        assert row == Row([1, 2, 3])

    def test_get_numbers(self):
        row = Row([4, 5, 6])
        numbers = row.get_numbers()
        assert numbers == [4, 5, 6]


class TestNumbersFileMethods:
    def test_from_file(self):
        numbers = Numbers.from_file('tests/oop/data/task_2_numbers_perfect.txt')
        assert numbers == Numbers(
            smallest_numbers=[10, 8, 9, 1, 7],
            middle_numbers=[20, 13, 18, 11, 17],
            highest_numbers=[30, 22, 25, 29, 31])

    def test_is_file_perfect(self):
        perfect_file = Numbers.from_file('tests/oop/data/task_2_numbers_perfect.txt')
        not_perfect_file = Numbers.from_file('tests/oop/data/task_2_numbers_not_perfect.txt')
        assert perfect_file.is_file_perfect()
        assert not_perfect_file.is_file_perfect() == (False, {0: [29], 1: [58, 60]})


class TestNumbersMethods:
    @pytest.fixture
    def numbers(self):
        return Numbers([13, 17, 19, 29, 10],
                       [28, 25, 58, 60, 49],
                       [56, 78, 99, 98, 432])

    @pytest.fixture(params=[
        [lambda num: num % 2 == 0, 4],
        [lambda num: sum(int(d) for d in str(num)) > 14, 3]

    ])
    def condition_and_result(self, request):
        return request.param

    def test_get_diff_between(self, numbers):
        diff = numbers.get_diff_between(lambda nums: max(nums), lambda nums: min(nums))
        assert diff == 4

    def test_count_elements_meeting_condition(self, numbers, condition_and_result):
        condition_fn, expected_result = condition_and_result
        result = numbers.count_elements_meeting_condition(condition_fn=lambda num: condition_fn(num))
        assert result == expected_result

    def test_find_minimum_non_decreasing_sequence(self, numbers):
        result = numbers.find_extreme_non_decreasing_sequence(lambda nums: min(nums))
        assert result == 1

    def test_find_maximum_non_decreasing_sequence(self, numbers):
        result = numbers.find_extreme_non_decreasing_sequence(lambda nums: max(nums))
        assert result == 0

    def test_find_minimum_difference(self, numbers):
        diff = numbers.find_index_of_extreme_difference(lambda nums: min(nums))
        assert diff == 4

    def test_find_maximum_difference(self, numbers):
        diff = numbers.find_index_of_extreme_difference(lambda nums: max(nums))
        assert diff == 0
