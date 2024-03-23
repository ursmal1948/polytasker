import re
from tasks.common_functions import get_string_until

"""
Write a program where you prompt the user for a string until it contains alternating uppercase letters and digits.
An example of a string meeting this criterion is A9B3C7.
Based on the entered string, generate a new string where each digit is replaced by numbers that are divisors
of the ASCII code of the character preceding the digit and greater than the digit.
For example, for the string B3, the result is B611223366, because the letter B has an ASCII code of 66.
The divisors of 66 are: 1, 2, 3, 6, 11, 22, 33, 66.
Divisors greater than 3 are 6, 11, 22, 33, 66, and they replace the digit 3 in the string.
"""


def does_string_match_regex(text: str, regex: str = r'^([A-Z]\d)+$') -> bool:
    """
    Check if the string matches a given regular expression pattern.

    Parameters:
        text (str): The string to be checked.
        regex (str, optional): The regular expression pattern.

    Returns:
        bool: True if the string matches the pattern, False otherwise.
    """

    if not re.match(regex, text):
        return False
    return True


def get_divisors(n: int) -> list[int] | float:
    """
    Get the divisors of a given integer.

    Parameters:
        n (int): The integer for which divisors are to be found.

    Returns:
        list[int] | float: A list of divisors of the integer.
            Returns infinity if the input is 0.

    Example:
       Input: n = 12
        Output: [1, 2, 3, 4, 6, 12]
    """

    if n == 0:
        return float('inf')
    nn = abs(n) if n < 0 else n
    divisors = {1: 1, 2: [1, 2], 3: [1, 3]}
    if nn in divisors:
        return divisors[n]

    divisors_list = [1]
    i = 2
    while i * i < nn:
        if nn % i == 0:
            divisors_list.extend([i, nn // i])
        i += 1
    if i * i == nn:
        divisors_list.append(i)
    return sorted(divisors_list + [n])


def replace_digits_with_divisors(text: str) -> str:
    """
    Replace digits in a string with divisors greater than the ASCII value of the preceding character.

    Parameters:
        text (str): The input string containing alternating uppercase letters and digits.

    Returns:
        str: The modified string where digits are replaced with their respective divisors.

    Example:
        Input: B9D5
        Output: B11223366D173468
    """

    items = []
    for i in range(1, len(text), 2):
        digit = int(text[i])
        char = text[i - 1]
        char_code = ord(char)
        divisors = [d for d in get_divisors(char_code) if d > digit]
        items.extend([char] + divisors)
    return ''.join(str(i) for i in items)


def main() -> None:
    text = get_string_until("Get string", lambda string: does_string_match_regex(string))
    modified_text = replace_digits_with_divisors(text)
    print(f'Modified text: {modified_text}')


if __name__ == '__main__':
    main()
