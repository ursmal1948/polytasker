import pytest

from tasks.matrixes.task_1 import (
    get_size_of_matrix_until_predicate,
    generate_matrix,
    calculate_rows_average,
    find_rows_with_averages_between_neighbours,
    zero_out_rows_not_matching_indexes
)
from unittest.mock import patch


class TestTask1Functions:

    @pytest.fixture
    def matrix(self):
        return [[7, 10, 13],
                [10, 14, 1],
                [2, 8, 14],
                [12, 9, 8]]

    @patch('random.randint')
    def test_get_size_of_matrix_until_predicate(self, mock_random):
        mock_random.side_effect = [6, 5]
        rows, columns = get_size_of_matrix_until_predicate(1, 10)
        assert (rows, columns) == (6, 5)

    @patch('random.randint')
    def test_generate_matrix(self, mock_random):
        mock_random.side_effect = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        rows, columns = 2, 5
        matrix = generate_matrix(rows, columns, 1, 20)
        assert matrix == [[3, 4, 5, 6, 7], [8, 9, 10, 11, 12]]

    def test_calculate_rows_average(self, matrix):
        rows_average = calculate_rows_average(matrix)
        assert rows_average == [10.0, 8.33, 8.0, 9.67]

    def test_find_rows_with_averages_between_neighbours(self, matrix):
        idx = calculate_rows_average(matrix)
        rows_with_average_between_neighbours = find_rows_with_averages_between_neighbours(idx)
        assert rows_with_average_between_neighbours == [1]

    def test_zero_out_non_matching_indexes(self, matrix):
        idx = calculate_rows_average(matrix)
        matching_idx = find_rows_with_averages_between_neighbours(idx)
        new_matrix = zero_out_rows_not_matching_indexes(matrix, matching_idx)
        assert new_matrix == [[0, 0, 0],
                              [10, 14, 1],
                              [0, 0, 0],
                              [0, 0, 0]]
