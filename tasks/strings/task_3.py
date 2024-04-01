from tasks.common_functions import get_string_until

"""
Prompt the user for a string until characters with even ASCII codes appear
at even positions and characters with odd ASCII codes appear at odd positions. The string 
must also have an even number of characters. Then apply simple encryption to the string by
swapping each pair of adjacent characters. Finally, save the resulting encrypted string to
a text file named "encrypted.txt".
"""


def has_even_odd_ascii_pattern(text: str) -> bool:
    """
    Checks if the input string meets specific conditions regarding its length and the ASCII values of its characters.
    -> even length
    -> even ascii codes on even positions
    -> odd ascii codes on odd positions

    Parameters:
        text (str): The text to be checked for conditions.

    Returns:
        bool: True if the text meets all the conditions, False otherwise.

    Example:
        Input: "BADC"
        Output: True
    """

    if text == "" or len(text) % 2 != 0:
        return False
    for i in range(len(text)):
        if i % 2 == 0 and ord(text[i]) % 2 == 1:
            return False
        if i % 2 == 1 and ord(text[i]) % 2 == 0:
            return False
    return True


def swap_chars(text: str) -> str:
    """
    Performs simple encryption on the input string by swapping adjacent characters.

    Parameters:
     text (str): The text to be encrypted.

    Returns:
     str: A new string with characters swapped in pairs.

    Example:
        Input: "ABCD"
        Output: "BADC"
    """
    chars = list(text)
    for i in range(0, len(chars) - 1, 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
    return ''.join(chars)


def save_to_file(filename: str, text: str) -> None:
    """
    Saves the given text to a file with the specified filename.

    Parameters:
     filename (str): The name of the file to save the text to.
     text (str): The text to be saved to the file.

    Returns:
     None
    """

    with open(filename, 'w') as f:
        f.write(text)
