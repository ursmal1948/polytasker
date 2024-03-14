import random
from typing import Callable


def get_array_length(r_min, r_max: int) -> int:
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
    Prompts the user
    :param message: str a message to display to the user
    :param condition_fn: Callable[[str],bool] a function that takes a string as argument and
    returns a boolean indicating whether the innput meets certain conditions
    :return str: text that meets the conditions specified by the condition_fn
    """
    while not condition_fn(v := input(f'{message}:\n')):
        pass
    return v
