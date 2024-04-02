from typing import Callable

"""

Write a program that takes three strings from the user until the number of vowels in the strings is the same. 
Then, prepare a new string that will be a concatenation of the three strings obtained earlier, which have been 
modified (or possibly saved to new strings). The modification involves rearranging the characters in the string
in such a way that vowels appear first in the order of their occurrence in the original string, followed by
consonants in the order of their occurrence in the original string. For example, when we have 
the string "WAISTCOAT", after modification it looks like "AIOAWSTCT".
"""


def get_string(message: str) -> str:
    """
    Prompt the user to enter a string.

    Parameters:
        message (str): The message to display to the user.

    Returns:
        str: The string entered by the user.
    """

    return input(f'{message}:\n')


def count_vowels(text: str) -> int:
    """
    Count the number of vowels in a given text.

    Parameters:
        text (str): The input text.

    Returns:
        int: The count of vowels in the text.
    """

    return sum(1 for c in text if c.isalpha() and c.lower() in 'aeyuio')


def get_strings_with_condition(message: str, count: int = 3, mapper_fn: Callable[[str], int] = count_vowels) -> str:
    """
    Get strings from the user until the number of vowels in each string is the same.

    Parameters:
        message (str): The message prompt for each string.
        count (int, optional): The number of strings to retrieve. Defaults to 3.
        mapper_fn (Callable[[str], int], optional): A function to apply to each string to determine its "vowel count".
            Defaults to count_vowels.

    Returns:
        str: A concatenated string of the inputs.
    """
    strings = []
    mapped_values = []

    while len(set(mapped_values)) != 1:
        strings.clear()
        mapped_values.clear()
        for i in range(count):
            string = get_string(f'{i + 1}.{message}')
            strings.append(string)
            mapped_values.append(mapper_fn(string))
    return ''.join(strings)


# while True:
#     strings = [get_string(f'{i + 1}.{message}') for i in range(count)]
#     vowels_count = [mapper_fn(string) for string in strings]
#
#     if all(count == vowels_count[0] for count in vowels_count):
#         return ''.join(strings)


def rearrange_vowels_consonants(text: str) -> str:
    """
    Rearrange the characters in the text so that vowels appear first, followed by consonants.

    Parameters:
        text (str): The input text.

    Returns:
        str: The text with vowels followed by consonants.

    Example:
        Input: clear
        Output: eaclr
    """

    vowels = [c for c in text if c.isalpha() and c.lower() in 'aeyuio']
    consonants = [c for c in text if c.isalpha() and c.lower() not in 'aeyuio']
    return "".join(vowels + consonants)
