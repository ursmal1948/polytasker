from collections import defaultdict
from tasks.common_functions import get_array_length, generate_n_numbers

"""
Write a program in which you generate a one-dimensional array of integers. The size of the array is randomly
chosen from the range <10, 40>. The elements of the array are randomly selected from the range <30, 50>. Determine 
the indexes of the two elements in the array with the smallest difference. Generate a new array by moving the two
determined elements to the end of the array.
"""


def find_indexes_with_smallest_difference(numbers: list[int]) -> list[tuple[int, int]]:
    """
    Finds indexes of two elements in the list with the smallest difference.

    Parameters:
        numbers (list[int]): The list of integers.

    Returns:
        list[tuple[int,int]]: A list of tuples containing the indexes of the elements with the smallest difference.

    Example:
        input: [100,200,250,400,450,600,700,800]
        output: [(1, 2), (3, 4)]
    """

    group_by_difference = defaultdict(list)
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            group_by_difference[diff].append((i, j))
    return min(group_by_difference.items())[1]


def move_elements_to_the_end(numbers: list[int], indexes: list[tuple[int, int]]) -> list[int]:
    """
    Moves elements specified by indexes to the end of the list.

    Parameters:
        numbers (list[int]): The list of integers.
        indexes (list[tuple[int,int]]): A list of tuples containing the indexes of elements to be moved.

    Returns:
        list[int]: A new list with elements moved to the end.

    Example:
        Input: numbers: [100,200,250,400,450,600,700,800] indexes: [(1, 2), (3, 4)]
        Output: [100,200,250,400,450,600,700,800]
    """

    not_indexed_numbers = []
    indexed_numbers = []
    idx = [num for tpl in indexes for num in tpl]
    for i in range(len(numbers)):
        if i in idx:
            indexed_numbers.append(numbers[i])
        else:
            not_indexed_numbers.append(numbers[i])
    return not_indexed_numbers + indexed_numbers


def main() -> None:
    array_length = get_array_length(10, 40)
    numbers = generate_n_numbers(array_length, 30, 50)
    print(numbers)
    indexes = find_indexes_with_smallest_difference(numbers)
    print(indexes)
    print(move_elements_to_the_end(numbers, indexes))


if __name__ == '__main__':
    main()
