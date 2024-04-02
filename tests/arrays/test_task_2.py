import pytest
from tasks.arrays.task_2 import find_indexes_with_smallest_difference, move_elements_to_the_end


class TestTask2Functions:
    @pytest.mark.parametrize('numbers, expected_indexes', [
        ([31, 30, 50, 36, 46, 42, 37, 37], [(6, 7)]),
        ([36, 34, 35, 46, 41], [(0, 2), (1, 2)]),
        ([30, 40, 50, 60, 70], [(0, 1), (1, 2), (2, 3), (3, 4)])
    ])
    def test_find_indexes_with_smallest_difference(self, numbers, expected_indexes):
        indexes = find_indexes_with_smallest_difference(numbers)
        assert indexes == expected_indexes

    @pytest.mark.parametrize('numbers, indexes, expected_result', [
        ([100, 200, 300, 400], [(1, 2)], [100, 400, 200, 300]),
        ([10, 20, 30, 40, 50], [(0, 4)], [20, 30, 40, 10, 50]),
        ([1, 2, 3, 4, 5], [(0, 1), (1, 2), (2, 3), (3, 4)], [1, 2, 3, 4, 5])
    ])
    def test_move_elements_to_the_end(self, numbers, indexes, expected_result):
        result = move_elements_to_the_end(numbers, indexes)
        assert result == expected_result
