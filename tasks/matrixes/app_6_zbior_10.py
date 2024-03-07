import random
from typing import Callable

"""
6. Napisz program, w którym przygotujesz tablicę dwuwymiarową
przechowującą liczby całkowite. Liczba wierszy i kolumn losowane są
z przedziału <2, 20> dopóki liczba wierszy nie będzie różnić się
co najmniej o 3 od połowy wartości wylosowanej liczby kolumn. Elementy
tablicy losowane są z przedziału <30, 100>. Wyznacz numery wierszy,
dla których średnia arytmetyczna elementów ma wartość pomiędzy
wartościami średniej arytmetycznej elementów wierszy sąsiednich.
Wyzeruj wiersze, które nie mają tej własności.
"""


def get_size_of_matrix_until_predicate(
        r_min: int = 2,
        r_max: int = 20,
        predicate: Callable[[int, int], bool] = lambda a, b: abs(a - (b // 2)) >= 3) \
        -> tuple[int, int]:
    """
    Generates the size of a matrix until a specified predicate is satisfied
    :param r_min: int the minimum number of rows/columns in the matrix
    :param r_max: int the maximum number of rows/columns in the matrix
    :param predicate: Callable[[int, int], bool] a function that takes two integers and returns a boolea. The predicates
    determines whether the generated size satisfies the condition. Defaults to check if the absolute difference between
    the number of rows and half the number of columns is at least 3
    :return tuple[int,int]: a tuple containing the number of rows and columns for matrix
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
    Generates a two-dimensional array with random integer elements
    :param rows: int the number of rows in the matrix
    :param columns: int the number of columns in the matrix
    :param r_min: int the minimum value for the randomly generated elements. Defaults to 30
    :param r_max: int the maximum value for the randomly generated elements. Defaults to 100
    :return list[list[int]]: a two-dimensional list representing the matrix
    """

    return [[random.randint(r_min, r_max) for _ in range(columns)] for _ in range(rows)]


def calculate_row_average(matrix: list[list[int]]) -> list[float]:
    """
    Calculates the average value of elements in each row of the matrix

    :param matrix: list[list[int]] input matrix
    :return list[float]: a list containing the average value of elements for each row in the matrix
    """
    return [sum(n for n in row) / len(row) for row in matrix]


def get_indexes_where_average_between(averages: list[float]) -> list[int]:
    """
    Finds the indexes of rows whose average values are between the averages of their neighboring rows

    :param averages: list[float] a list containing the average value of elements for each row of the matrix
    :return: list[int] a list of indexes of rows whose average values meet the specified condition
    """
    matching_indexes = []
    for i in range(1, len(averages) - 1):
        if averages[i - 1] <= averages[i] <= averages[i + 1] or averages[i - 1] >= averages[i] >= averages[i + 1]:
            matching_indexes.append(i)
    return matching_indexes


def zero_out_rows_not_matchin_indexes(matrix: list[list[int]], indexes: list[int]) -> list[list[int]]:
    """
    Zeros out rows in the matrix that do not match the specified indexes

    :param matrix: list[list[int]] input matrix
    :param indexes: list[int] a list of indexes of rows to keep unchanged
    :return: list[list[int]] the modified matrix with rows not matching the indexes zeroed out
    """
    return [matrix[i] if i in indexes else [0] * len(matrix[i]) for i in range(len(matrix))]


def main() -> None:
    size = get_size_of_matrix_until_predicate()
    matrix = [[90, 71, 81, 93],
              [75, 43, 39, 80],
              [34, 86, 49, 76],
              [36, 99, 46, 99],
              [49, 38, 56, 47],
              [36, 38, 68, 83],
              [30, 31, 79, 73],
              [45, 50, 37, 77]]
    rows_average = calculate_row_average(matrix)
    print(rows_average)
    matching_indexes = get_indexes_where_average_between(rows_average)
    modified_matrix = zero_out_rows_not_matchin_indexes(matrix, matching_indexes)
    print(modified_matrix)


if __name__ == '__main__':
    main()
# DONE
