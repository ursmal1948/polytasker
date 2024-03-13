from itertools import chain

"""
Napisz metodę, która pobiera jako argument dwa pliki tekstowe. W
plikach tekstowych znajdują się tablice jednowymiarowe o elementach
typu double, w każdym pliku jedna tablica. Pliki nie zawierają
informacji na temat wymiarów tablic, dlatego trzeba go ustalić na
podstawie ilości danych znajdujących się w plikach. Scal dwie pobrane
w ten sposób tablice w jedną, w której elementy są posortowane rosnąco
według wybranej przez Ciebie metody sortowania.
"""


def read_data_from_files(filename1: str, filename2: str) -> tuple[list[float], list[float]]:
    """
    Reads numerical data from two files and returns them as lists of floats
    :param filename1: str the path the first file containing numerical data
    :param filename2: str the path to the second file containing numerical data
    :return tuple[list[float],list[float]]: a tuple containing two lists of floats, representing the data read from the files
    """
    with open(filename1, 'r') as f:
        numbers1 = [float(n) for n in f.readlines()]

    with open(filename2, 'r') as f:
        numbers2 = [float(n) for n in f.readlines()]
    return numbers1, numbers2


def sort_items(*args) -> list[float]:
    """
    Implements QuickSort algorithm to sort a collection of numerical items
    :param args: variable number of iterable collections containing numerical items
    :return list[float]: a sorted list of floats from the collections
    """
    items = list(chain(*args))
    if len(items) <= 1:
        return items
    pivot = items[len(items) // 2]
    less_than_pivot = [n for n in items if n < pivot]
    equal_to_pivot = [n for n in items if n == pivot]
    greater_than_pivot = [n for n in items if n > pivot]
    return sort_items(less_than_pivot) + equal_to_pivot + sort_items(greater_than_pivot)
