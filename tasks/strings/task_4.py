import re
from typing import Callable
from collections import defaultdict

"""
In two text files prepared by you, each line contains words. We don't know how many words are in each file.
Write a program that saves only those words to a third text file, which appeared simultaneously in both files 
and contain more consonants than vowels. From the words in the third text file, create a single string, 
in which successive words are separated by commas and appear in alphabetical order.
"""


def read_from_file(filename: str) -> list[str]:
    """
    Read words from a text file.

    Parameters:
        filename (str): The name of the file to read.

    Returns:
        list[str]: A list containing words read from the file.
    """

    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        words = []
        for line in lines:
            items = line.split()
            for item in items:
                words.append(item.lower())
        return words


def get_common_words(words1: list[str], words2: list[str]) -> list[str]:
    """
    Get common words from two lists.

    Parameters:
        words1 (list[str]): The first list of words.
        words2 (list[str]): The second list of words.

    Returns:
        list[str]: A list of words common to both input lists.

    Example:
        Input: words1 = ["garden", "ball", "sun"], words2 = ["sheet", "picture", "sun", "ball"]
        Output: ["ball", "sun"]
    """

    return [word for word in words1 if word in words2]


def chars_1_group_exceeds_chars_2_group_count(
        text: str,
        group_1_regex: str = r'(?![aeyuioAEYUIO])[a-zA-Z]',
        group_2_regex: str = r'[aeyuioAEYUIO]'
) -> bool:
    """
    Check if the count of consonants exceeds the count of vowels in a text.

    Parameters:
        text (str): The input text.
        group_1_regex (str): First group of chars.
        group_2_regex (str): Second group of chars

    Returns:
        bool: True if the count of consonants exceeds the count of vowels, False otherwise.

    Example:
        Input: text = "kayak"
        Output: False

        Input: text = "spark"
        Output: True
    """

    grouped_by_chars = defaultdict(int)

    for char in text:
        if re.match(group_1_regex, char):
            grouped_by_chars[group_1_regex] += 1
        elif re.match(group_2_regex, char):
            grouped_by_chars[group_2_regex] += 1
    first_group_count = grouped_by_chars[group_1_regex]
    second_group_count = grouped_by_chars[group_2_regex]

    return first_group_count > second_group_count


def save_filtered_items_to_file(filename: str, items: list[str], filter_fn: Callable[[str], bool]) -> None:
    """
    Save filtered items to a file.

    Parameters:
        filename (str): The name of the file to save the items to.
        items (list[str]): The list of items to save.
        filter_fn (Callable[[str], bool]): A function to filter the items.

    Returns:
        None
    """

    filtered_items = [item for item in items if filter_fn(item)]
    with open(filename, 'w') as f:
        f.writelines(
            filtered_items[i] + '\n'
            if i != len(filtered_items) - 1 else filtered_items[i] for i in range(len(filtered_items)))


def create_string_from_file(filename: str, separator: str) -> str:
    """
    Create a single string from words in a file.

    Parameters:
        filename (str): The name of the file containing words.

    Returns:
        str: A single string containing words from the file, separated by commas and in alphabetical order.
    """

    items = read_from_file(filename)
    return f'{separator}'.join(sorted(items))


def main() -> None:
    words_1 = read_from_file('data/words.txt')
    words_2 = read_from_file('data/words_2.txt')
    print(f'Words from first file: {words_1}')
    print(f'Words from second file: {words_2}')
    common_words = get_common_words(words_1, words_2)
    print(f'Common words: {common_words}')
    save_filtered_items_to_file('data/saved_words.txt', common_words,
                                lambda text: chars_1_group_exceeds_chars_2_group_count(text))
    string_from_file = create_string_from_file('data/saved_words.txt', ',')
    print(f'String from file: {string_from_file}')


if __name__ == '__main__':
    main()
