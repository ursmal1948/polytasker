from itertools import chain

"""
Write a method that takes two text files as arguments. The text files contain one-dimensional arrays of double
type elements, with one array per file. The files do not contain information about the dimensions of the arrays,
so it needs to be determined based on the amount of data in the files. Merge the two arrays obtained in this way
into one, where the elements are sorted in ascending order according to the sorting method chosen by you
"""


def read_data_from_file(filename: str) -> list[float]:
    """
    Reads numerical data from file and returns list of floats.

    Parameters:
        filename (str): The path to the first file containing numerical data.

    Returns:
        list[float]: A list of floats, representing
        the data read from the file

    Example:
        Input:   filename1 = "data/file1.txt"
        Output: (
        [10.5, 12.8, 17.9, 24.0, 90.1, 3.14, 17.12, 12.56]
        )
    """

    if not filename.endswith(".txt"):
        raise AttributeError('File has incorrect extension')

    try:
        with open(filename, 'r') as f:
            return [float(n.strip()) for n in f.readlines()]
    except Exception as e:
        raise FileNotFoundError(f'File not found: {e}')


def sort_items(*args) -> list[float]:
    """
    Implements QuickSort algorithm to sort a collection of numerical items.

    Parameters:
        *args: variable number of iterable collections containing numerical items.

    Returns:
        list[float]: A sorted list of floats from the collections.

    Example:
        Input: *args = [12,34,78,19,2,-15,90],[0,-3,13,49,23]
        Output: [-15, -3, 0, 2, 12, 13, 19, 23, 34, 49, 78, 90]
    """

    numbers = list(chain(*args))
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[len(numbers) // 2]
    less_than_pivot = [n for n in numbers if n < pivot]
    equal_to_pivot = [n for n in numbers if n == pivot]
    greater_than_pivot = [n for n in numbers if n > pivot]
    return sort_items(less_than_pivot) + equal_to_pivot + sort_items(greater_than_pivot)


# def main() -> None:
#     filename1 = "data/file1.txt"
#     filename2 = "data/file2.txt"
#     numbers1, numbers2 = read_data_from_file(filename1), read_data_from_file(filename2)
#     sorted_numbers = sort_items(numbers1, numbers2)
#     print(f'SORTED COLLECTION: {sorted_numbers}')
#     print(sort_items([1, 2, 3], [4, 5,2, 6]))
#
#
# if __name__ == '__main__':
#     main()
