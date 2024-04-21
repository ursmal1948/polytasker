from typing import Callable
from collections import defaultdict
import re

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


def count_chars(text: str, regex: str) -> int:
    """
    Count the number of chars provided by regex.

    Parameters:
        text (str): The input text.
        regex (str): Regular expression to check under text.

    Returns:
        int: The count of vowels in the text.
    """
    matches = re.findall(regex, text, flags=re.IGNORECASE)
    return len(matches)


def get_strings_until_same_chars_count(message: str, count: int = 3,
                                       regex: str = r'[aeyuio]',
                                       chars_count_fn: Callable[[str, str], int] = count_chars) -> str:
    """
    Get strings from the user until the number of vowels in each string is the same.

    Parameters:
        message (str): The message prompt for each string.
        count (int, optional): The number of strings to retrieve. Defaults to 3.
        regex (str,optional): Regex to apply.
        chars_count_fn (Callable[[str], int], optional): A function to apply to each string to determine its "vowel count".
            Defaults to count_vowels.

    Returns:
        str: A concatenated string of the inputs.
    """
    first_string = get_string(f'1.{message}')
    first_word_vowels_count = chars_count_fn(first_string, regex)
    strings = [first_string]
    for i in range(1, count):
        while chars_count_fn(v := get_string(f'{i + 1}. {message}'), regex) != first_word_vowels_count:
            pass
        strings.append(v)

    return ''.join(strings)


def rearrange_group1_group2_chars(text: str, group1_chars: str, group2_chars: str) -> str:
    """
    Rearrange the characters in the text so that vowels appear first, followed by consonants.

    Parameters:
        text (str): The input text.
        group1_chars (str): First group of chars.
        group2_chars (str): Second group of chars.

    Returns:
        str: The text with vowels followed by consonants.

    Example:
        Input: clear
        Output: eaclr

    """
    grouped_by_chars = defaultdict(list)
    for char in text:
        if char in group1_chars:
            grouped_by_chars[group1_chars].append(char)
        elif char in group2_chars:
            grouped_by_chars[group2_chars].append(char)

    return ''.join(grouped_by_chars[group1_chars] + grouped_by_chars[group2_chars])


# def main() -> None:
#     string = get_strings_until_same_chars_count("POdaj stringa", 2,
#                                                 chars_count_fn=lambda text, regex: count_chars(text, regex))
#     # text = rearrangr_group1_group2_chars("WAISTCOAT", 'AEYUIO', 'WSTC')
#     print(string)
#     string = 'SA123oj'
#     # print(count_chars(text, r'[a-z]'))
#
#
# if __name__ == '__main__':
#     main()
