import pytest
from tasks.arrays.task_1 import get_unique_digits


class TestTask1Function:
    @pytest.mark.parametrize("numbers, expected_unique_digits", [
        ([123, 345, 567], [1, 2, 3, 4, 5, 6, 7]),
        ([123, 456, 890], [1, 2, 3, 4, 5, 6, 8, 9, 0]),
        ([0, 0, 0], [0])
    ])
    def test_get_unique_digits(self, numbers, expected_unique_digits):
        unique_digits = get_unique_digits(numbers)
        assert unique_digits == expected_unique_digits
