"""
In the text file, 101 digits ranging from 0 to 9 are written next to each other.
Count how many digits in the file should be changed to 1 or 0 to obtain a Googol number. A Googol number
consists of a leading 1 followed by a hundred 0s.
"""


def read_numbers_from_file(filename: str) -> list[int]:
    """
    Reads a list of integers from a text file.

    Parameters:
        filename (str): The path to the text file containing integers.

    Returns:
        list[int]: A list of integers read from the file.

    Example:
        Input: filename "numbers.txt" containing:
        12345
        Output: [1, 2, 3, 4, 5]
    """

    with open(filename, "r") as f:
        return [int(n) for n in f.readline()]


def count_changes_to_form_googol_number(numbers: list[int]) -> int:
    """
    Counts the number of changes needed in a list of integers to form a Googol number.

    Parameters:
        numbers (list[int]): A list of integers representing digits.

    Returns:
        int: The number of changes needed to form a Googol number, where a Googol is defined as a number
             with '1' followed by 100 '0's.

    Example:
        Input: [1, 0, 0, 4, 0, 1, 6, 5, 6, 9, 5, 8, 4, 3, 7, 4, 0, 6, 7, 3, 0, 9, 7, 2, 3, 1, 5, 8, 2, 2,
         4, 6, 7, 6, 6, 6, 6, 8, 0, 0, 9, 3, 4, 0, 7, 4, 4, 7, 0, 2, 2, 4, 2, 1, 3, 2, 7, 0, 3, 0, 9, 9, 7,
          7, 5, 2, 8, 4, 6, 9, 8, 2, 9, 7, 3, 0, 0, 6, 8, 8, 9, 2, 4, 0, 6, 7, 3, 7, 9, 3, 8, 2, 7, 9, 2, 1, 0,
           7, 0, 5, 0]
        Output: 83
    """
    if len(numbers) != 101:
        raise ValueError("List must have 101 numbers")

    non_zero_digits_count = sum([1 for i in range(1, len(numbers)) if numbers[i] != 0])
    return non_zero_digits_count + (1 if numbers[0] != 1 else 0)


# def main() -> None:
#     filename = 'data/googol.txt'
#     digits = read_numbers_from_file(filename)
#     changes_count = count_changes_to_form_googol_number(digits)
#     print(f'CHANGES TO BE MADE TO FORM A GOOGOL NUMBER: {changes_count}')
#
#
# if __name__ == '__main__':
#     main()
