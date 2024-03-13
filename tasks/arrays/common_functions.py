import random


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
        raise ValueError('Incorrect range')
    return random.randint(r_min, r_max)
