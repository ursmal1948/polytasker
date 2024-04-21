import random
from typing import Callable

"""
Write a program in which you prepare a two-dimensional array storing integers. The number of rows and columns
are randomly chosen from the range <2, 20> until the number of rows differs by at least 3 from half the value 
of the randomly chosen number of columns. The elements of the array are randomly chosen
from the range <30, 100>. Determine the row numbers for which the arithmetic mean of elements is between the
arithmetic means of neighboring rows. Zero out the rows that do not have this property.
"""


def get_size_of_matrix_until_predicate(
        r_min: int = 2,
        r_max: int = 20,
        predicate: Callable[[int, int], bool] = lambda a, b: abs(a - (b // 2)) >= 3) \
        -> tuple[int, int]:
    """
    Generates the size of a matrix until a specified predicate is satisfied.

    Parameters:
        r_min (int): The minimum number of rows/columns in the matrix. Defaults to 2.
        r_max (int): The maximum number of rows/columns in the matrix. Defaults to 20.
        predicate (Callable[[int, int], bool]): A function that takes two integers and returns a boolean.
            It determines whether the generated size satisfies the condition. Defaults to check if the
             absolute difference between the number of rows and half the number of columns is at least 3.

    Returns:
        tuple[int,int]: A tuple containing the number of rows and columns for the matrix.
    Raises:
        ValueError: if r_min higher than r_max.
    """

    if r_min > r_max:
        raise ValueError('Incorrect range')
    while True:
        rows = random.randint(r_min, r_max)
        columns = random.randint(r_min, r_max)
        if predicate(rows, columns):
            return rows, columns


def generate_matrix(rows: int, columns: int, r_min: int = 30, r_max: int = 100) -> list[list[int]]:
    """
    Generates a two-dimensional array with random integer elements.

    Parameters:
        rows (int): The number of rows in the matrix.
        columns (int): The number of columns in the matrix.
        r_min (int): The minimum value for the randomly generated elements. Defaults to 30.
        r_max (int): The maximum value for the randomly generated elements. Defaults to 100.

    Returns:
        list[list[int]]: A two-dimensional list representing the matrix.
    """

    return [[random.randint(r_min, r_max) for _ in range(columns)] for _ in range(rows)]


def calculate_rows_average(matrix: list[list[int]]) -> list[float]:
    """
    Calculates the average value of elements in each row of the matrix.

    Parameters:
        matrix (list[list[int]]): Input matrix.

    Returns:
        list[float]: A list containing the average value of elements for each row in the matrix.
    """

    return [round(sum(n for n in row) / len(row), 2) for row in matrix]


def find_rows_with_averages_between_neighbours(averages: list[float]) -> list[int]:
    """
    Finds the indexes of rows whose average values are between the averages of their neighboring rows.

    Parameters:
        averages (list[float]): A list containing the average value of elements for each row of the matrix.

    Returns:
        list[int]: A list of indexes of rows whose average values meet the specified condition.
    """

    matching_indexes = []
    for i in range(1, len(averages) - 1):
        if averages[i - 1] <= averages[i] <= averages[i + 1] or averages[i - 1] >= averages[i] >= averages[i + 1]:
            matching_indexes.append(i)
    return matching_indexes


def zero_out_rows_not_matching_indexes(matrix: list[list[int]], indexes: list[int]) -> list[list[int]]:
    """
    Zeros out rows in the matrix that do not match the specified indexes.

    Parameters:
        matrix (list[list[int]]): Input matrix.
        indexes (list[int]): A list of indexes of rows to keep unchanged.

    Returns:
        list[list[int]]: The modified matrix with rows not matching the indexes zeroed out.
    """

    return [matrix[i] if i in indexes else [0] * len(matrix[i]) for i in range(len(matrix))]


# def main() -> None:
#     rows, columns = get_size_of_matrix_until_predicate()
#     print(f'Size of matrix rows: {rows} columns: {columns}')
#     matrix = generate_matrix(4, 3, 1, 15)
#     for m in matrix:
#         print(m)
#     matrix = [[7, 10, 13],
#               [10, 14, 1],
#               [2, 8, 14],
#               [12, 9, 8]]
#     rows_average = calculate_rows_average(matrix)
#     print(f'Rows average: {rows_average}')
#     indexes = find_rows_with_averages_between_neighbours(rows_average)
#     print(f'Rows with average between neighbours: {indexes}')
#     new_matrix = zero_out_rows_not_matching_indexes(matrix, indexes)
#     print(f'New matrix: {new_matrix}')
#
#
# if __name__ == '__main__':
#     main()
