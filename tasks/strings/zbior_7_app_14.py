"""
Exercise 14
Generate a string consisting of only letters 'a' or 'b' of a length specified earlier by the user.
The string must be generated in such a way that the difference in the number of occurrences of letters 'b'
and 'a' in the string is not greater than 1. Then modify the string so that consecutive letters 'a' and 'b' alternate.
For example, if the string 'abbbaaba' was generated at the beginning, after modification you should get 'abababab'.
"""
import random


def get_int(message: str) -> int:
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


def generate_balanced_string(length: int, letter1: str, letter2: str) -> str:
    """
    Generate a string of balanced occurrences of two letters.

    Parameters:
        length (int): The length of the generated string.
        letter1 (str): The first letter to include in the string.
        letter2 (str): The second letter to include in the string.

    Returns:
        str: The generated string with balanced occurrences of the two letters.

    Example:
        Input: length = 5, letter1 = "a", letter2 = "b"
        Output: "ababb"
    """

    if length % 2 == 1:
        num = random.randint(1, 2)
        letter_1_length = length // 2 if num == 1 else (length // 2) + 1
    else:

        letter_1_length = length // 2
    letter_2_length = length - letter_1_length

    letter_1_count = 0
    letter_2_count = 0
    balanced_string = ''

    while length > 0:
        random_num = random.randint(1, 2)
        # Jak ciagle bedzie wylosowywana jedynka to jakbym dala length-=1 poza ifami to by dekrementowalo
        # a tutaj tylko jak warunki zachodza.
        if random_num == 1 and letter_1_count != letter_1_length:
            balanced_string += letter1
            letter_1_count += 1
            length -= 1
        elif random_num == 2 and letter_2_count != letter_2_length:
            balanced_string += letter2
            letter_2_count += 1
            length -= 1
    return balanced_string


def alternate_chars(text: str) -> str:
    """
    Modify a string so that consecutive letters alternate.

    Parameters:
        text (str): The input string.

    Returns:
        str: The modified string with alternating consecutive letters.

    Example:
        Input: text = "abbbaaba"
        Output: "abababab"

    """

    new_text = ''

    unique_letters = list(set(text))
    letter1 = unique_letters[0]
    letter2 = unique_letters[1]

    letter1_count = text.count(letter1)
    letter2_count = text.count(letter2)
    letters = letter1 + letter2

    for _ in range(min(letter1_count, letter2_count)):
        new_text += letters
    if letter1_count > letter2_count:
        new_text += letter1
    elif letter2_count > letter1_count:
        new_text += letter2
    return new_text


def main() -> None:
    length = get_int("Get length of the string")
    generated_string = generate_balanced_string(length, "a", "b")
    print(f'Generated string: {generated_string}')
    alternated_chars = alternate_chars(generated_string)
    print(f'Alternated chars: {alternated_chars}')


if __name__ == '__main__':
    main()
