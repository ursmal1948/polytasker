import random

"""
In a text file, there are 1000 numbers randomly selected from the range [2000, 5000], which do not repeat.
It is also possible to generate unique numbers with function generate_n_unique_numbers. 
Count how many mirror numbers occur in the text file. Examples of mirror numbers are 125 and 521.
"""


def read_from_file(filename: str) -> list[int]:
    """
    Reads a list of integers from a text file

    Parameters:
        filename (str): The name of the file to read the data from

    Returns:
        list[int]: The list of integers read from the file
    """

    with open(filename, 'r') as f:
        return [int(line) for line in f.readlines()]


def save_to_file(filename: str, data: list[int]) -> None:
    """
    Saves a list of integers to a text file

    Parameters:
        filename (str): The name of the file to save the data to
        data (list[int]): The list of integers to be saved to the file

    Returns:
        None
    """

    with open(filename, 'w') as f:
        f.writelines('\n'.join([str(d) for d in data]))


def generate_n_unique_numbers(n: int, r_min: int, r_max: int) -> list[int]:
    """
    Generates a list of n unique random integers within the range [r_min, r_max]

    Parameters:
        n (int): The number of random integers to generate
        r_min (int): The minimum value of the range (inclusive)
        r_max (int): The maximum value of the range (inclusive)

    Returns:
        list[int]: A list of unique random integers within the specified range

    Raises:
        ValueError: If r_min is greater than r_max

    Example:
        Input: n = 5, r_min = 10, r_max = 100
        Output: [70, 54, 87, 29, 95]
    """

    if r_min > r_max:
        raise ValueError('Incorrect range')
    unique_numbers = set()
    while len(unique_numbers) < n:
        unique_numbers.add(random.randint(r_min, r_max))
    return list(unique_numbers)


# todo count pairs meeting condition
def count_palindromic_pairs(numbers: list[int]) -> int:
    """
    Counts the number of palindromic pairs in a list of numbers

    Parameters:
        numbers (list[int]): The list of numbers to search for palindromic pairs

    Returns:
        int: The number of palindromic pairs found in the list

    Example:
        Input: [125, 521, 245, 555, 542, 786, 989]
        Output: 2
    """

    count = 0
    for i in range(len(numbers) - 1):
        palindrome = ''.join([d for d in str(numbers[i])])[::-1]
        for j in range(i + 1, len(numbers)):
            if int(palindrome) == numbers[j]:
                count += 1
    return count


def main() -> None:
    filename = "data/numbers.txt"
    unique_numbers2 = read_from_file(filename)
    print(unique_numbers2)
    palindromic_pairs_count = count_palindromic_pairs(unique_numbers2)
    print(f'COUNT OF PALINDROMIC PAIRS: {palindromic_pairs_count}')


if __name__ == '__main__':
    main()
