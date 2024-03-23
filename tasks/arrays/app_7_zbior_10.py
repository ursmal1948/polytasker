from collections import OrderedDict
from tasks.common_functions import rand_number, generate_n_numbers

"""
Write a program in which you generate a one-dimensional array of integers. The size of the array is randomly
chosen from the range <10, 20>, and the elements of the array are randomly selected from the range <100, 999>.
Then, based on the previously created array, generate a new array that contains the digits of all the numbers 
in the first array, but without repetitions. For example, for an array with elements: 123, 345, 567, the result
is an array with elements: 1, 2, 3, 4, 5, 6, 7.
"""


def get_unique_digits(numbers: list[int]) -> list[int]:
    """
    Generates a list of unique digits from a list of integers.

    Parameters:
        numbers (list[int]): A list of integers from which unique digits are to be extracted.

    Returns:
        list[int]: A list of unique digits extracted from the input list of integers.

    Example:
        Input: [123,111, 345, 567]
        Output: [1, 2, 3, 4, 5, 6, 7]
    """

    unique_digits = OrderedDict.fromkeys(int(d) for number in numbers for d in str(number))
    return list(unique_digits)


def main() -> None:
    array_length = rand_number(10, 20)
    numbers = generate_n_numbers(array_length, 100, 999)
    print(f'NUMBERS: {numbers}')
    unique_digits = get_unique_digits(numbers)
    print(f'UNIQUE DIGITS: {unique_digits}')


if __name__ == '__main__':
    main()
