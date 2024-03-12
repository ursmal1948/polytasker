from typing import Callable

"""
Pobieraj od użytkownika napis, dopóki na pozycjach parzystych nie będą
występowały znaki o parzystych kodach ASCII, a na pozycjach
nieparzystych znaki o nieparzystych kodach ASCII. Napis musi również
posiadać parzystą ilość znaków. Następnie zastosuj proste szyfrowanie
napisu, które zamieni dwa sąsiadujące ze sobą znaki miejscami.
Otrzymany zaszyfrowany napis zapisz do pliku tekstowego o nazwie
zaszyfrowany.txt.
"""


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


def is_valid(text: str) -> bool:
    """
    Checks if the string meets the requirements:
    -> even length
    -> even ascii codes on even positions (0-indexed(
    -> odd ascii codes on odd positions
    :param text: str text to be checked for conditions
    :return bool: True if text meets all the conditions, False otherwise
    """
    if len(text) % 2 != 0:
        return False
    for i in range(len(text)):
        if i % 2 == 0 and ord(text[i]) % 2 == 1:
            return False
        if i % 2 == 1 and ord(text[i]) % 2 == 0:
            return False
    return True


def swap_chars(text: str) -> str:
    """
    Performs simple encryption on the string by swapping characters
    :param text: str the text to be encry[ted
    :return str: new string with swapped characters
    """
    chars = list(text)
    for i in range(0, len(chars), 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
    return ''.join(chars)


def save_to_file(filename: str, text: str) -> None:
    """
    Saves the given text to the file
    :param filename: str the name of the file to save the text to
    :param text: str the text to be saved to the file
    :return: None
    """

    with open(filename, 'w') as f:
        f.write(text)
