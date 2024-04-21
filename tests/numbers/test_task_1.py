from tasks.numbers.task_1 import count_changes_to_form_googol_number, read_numbers_from_file
import pytest


class TestTask1Functions:

    def test_read_numbers_from_file(self):
        numbers = read_numbers_from_file('tests/numbers/data/task_1_nums.txt')
        expected_numbers = [1, 2, 3, 4]
        assert numbers == expected_numbers

    def test_count_changes_to_form_googol_number(self):
        numbers = [1, 0, 0, 4, 0, 1, 6, 5, 6, 9, 5, 8, 4, 3, 7, 4, 0, 6, 7, 3, 0, 9, 7, 2, 3, 1, 5, 8, 2, 2,
                   4, 6, 7, 6, 6, 6, 6, 8, 0, 0, 9, 3, 4, 0, 7, 4, 4, 7, 0, 2, 2, 4, 2, 1, 3, 2, 7, 0, 3, 0, 9, 9, 7,
                   7, 5, 2, 8, 4, 6, 9, 8, 2, 9, 7, 3, 0, 0, 6, 8, 8, 9, 2, 4, 0, 6, 7, 3, 7, 9, 3, 8, 2, 7, 9, 2, 1, 0,
                   7, 0, 5, 0]
        expected_changes = 83
        assert count_changes_to_form_googol_number(numbers) == expected_changes

    def test_count_changes_to_form_googol_number_raises_error(self):
        numbers = [1, 2, 3, 4, 5]
        with pytest.raises(ValueError) as e:
            count_changes_to_form_googol_number(numbers)
        assert str(e.value) == "List must have 101 numbers"
