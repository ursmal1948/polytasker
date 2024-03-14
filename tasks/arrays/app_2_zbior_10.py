from collections import defaultdict

"""
2. Napisz program, w którym wygenerujesz tablicę jednowymiarową liczb
całkowitych. Rozmiar tablicy losowany jest z przedziału <10, 40>.
Elementy tablicy losowane są z przedziału < 30, 50>. Wyznacz indeksy
tych dwóch elementów tablicy, pomiędzy którymi występuje najmniejsza
różnica. Wygeneruj nową tablicę, w której ‘przesuniesz’ dwa wyznaczone
elementy na koniec tablicy.
"""


def get_indexes_with_smallest_difference(numbers: list[int]) -> list[tuple[int, int]]:
    """
    Finds indexes of two elements in the list with the smallest difference.

    Parameters:
        numbers (list[int]): The list of integers.

    Returns:
        list[tuple[int,int]]: A list of tuples containing the indexes of the elements with the smallest difference.
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
