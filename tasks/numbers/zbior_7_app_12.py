import random
from algohub.algorithms.strings.string_analysis import is_palindrome

"""
W pliku tekstowym znajduje się 1000 liczb losowanych z przedziału
<2000, 5000>, które się nie powtarzają. Przygotuj taki plik
implementując odpowiednią metodę. Następnie zlicz, ile w pliku
tekstowym występuje liczb lustrzanych. Przykładami liczb lustrzanych
są liczby 125 oraz 521.
"""


def generate_n_unique_numbers(n: int, r_min: int, r_max: int) -> list[int]:
    """
    Generates a list of n unique random integers within the range [r_min, r_max]
    :param n: int the number of random integers to generate
    :param r_min: int the mimimum value of the range (inclusive)
    :param r_max: int the maximum value of the range (inclusive)
    :return list[int]: a list of unique random integers within the specified range
    :raises ValueError: if r_min is greater than r_max
    """
    if r_min > r_max:
        raise ValueError('Incorrect range')
    unique_numbers = set()
    while len(unique_numbers) < n:
        unique_numbers.add(random.randint(r_min, r_max))
    return list(unique_numbers)


def read_from_file(filename: str) -> list[int]:
    """
    Reads a list of integers from a text file
    :param filename: str the name of the file to read the data from
    :return list[int]: the list of integers read from the file
    """
    with open(filename, 'r') as f:
        return [int(line) for line in f.readlines()]


def save_to_file(filename: str, data: list[int]) -> None:
    """
    Saves a list of integers to a text file
    :param filename: str the name of the file to save the data to
    :param data: list[int] the list of integers to be saved to the file
    :return: None
    """
    with open(filename, 'w') as f:
        f.writelines('\n'.join([str(d) for d in data]))


# OPTYMALNY SPOSOB
def count_palindromic_pairs(numbers: list[int]) -> int:
    """
    Counts the number of palindromic pairs in a list of numbers
    :param numbers: list[int] the list of numbers to search for palindromic pairs
    :return int: the number of palindromic pairs found in the list
    """
    count = 0
    palindromic_numbers = sum(1 for n in numbers if is_palindrome(str(n)))  # 11,22 101,etc
    print(palindromic_numbers)
    count -= palindromic_numbers
    for n in numbers:
        palindrome_number = ''.join((str(d) for d in str(n)))[::-1]
        if int(palindrome_number) in numbers:
            count += 1
    return int(count / 2)
