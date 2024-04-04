import random
from typing import Callable


def rand_number(r_min, r_max: int) -> int:
    """
    Generates a random length for the array within the specified range.

    Parameters:
        r_min (int): The minimum length of the array.
        r_max (int): The maximum length of the array.

    Returns:
        int: The randomly generated length of the array.

    Raises:
        ValueError: If r_min is greater than r_max.
    """

    if r_min > r_max:
        raise ValueError("Min value is greater than max value=")
    return random.randint(r_min, r_max)


def generate_n_numbers(size: int, r_min: int, r_max: int) -> list[int]:
    """
    Generates a list of random integers within the specified range.

    Parameters:
        size (int): The size of the list.
        r_min (int): The minimum value of the range (inclusive).
        r_max (int): The maximum value of the range (inclusive).

    Returns:
        list[int]: A list of random integers within the range.

    Raises:
        ValueError: If r_min is greater than r_max.
    """

    if r_min > r_max:
        raise ValueError('Incorrect range')
    return [random.randint(r_min, r_max) for _ in range(size)]


def get_string_until(message: str, condition_fn: Callable[[str], bool]) -> str:
    """
    Prompts the user with a message until the input meets certain conditions specified by the condition_fn.

    Parameters:
        message (str): A message to display to the user.
        condition_fn (Callable[[str], bool]): A function that takes a string as an argument and returns
            a boolean indicating whether the input meets certain conditions.

    Returns:
        str: Text that meets the conditions specified by the condition_fn.
    """

    while not condition_fn(v := input(f'{message}:\n')):
        pass
    return v


def get_number(message: str) -> int:
    """
    Prompts the user with a message to input a number and returns the input as an integer.

    Parameters:
        message (str): The message to prompt the user for input.

    Returns:
        int: The integer input by the user.

    Raises:
        ValueError: If the input cannot be converted to an integer.
    """

    try:
        v = int(input(f'{message}:\n'))
    except Exception as e:
        raise ValueError(e.args[0])
    return v


def get_positive_number(message: str) -> int:
    """
    Get an integer input from the user.

    Parameters:
        message (str): The message to display to the user.

    Returns:
        int: The integer entered by the user.
    """

    while True:
        try:
            num = int(input(f'{message}:\n'))
            if num > 0:
                return num
            else:
                print('Enter a positive integer')
        except ValueError:
            print('Please enter a valid integer')
