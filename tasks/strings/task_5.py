from collections import Counter
from dataclasses import dataclass
import random

"""
Generate a string consisting of only letters 'a' or 'b' of a length specified earlier by the user.
The string must be generated in such a way that the difference in the number of occurrences of letters 'b'
and 'a' in the string is not greater than 1. Then modify the string so that consecutive letters 'a' and 'b' alternate.
For example, if the string 'abbbaaba' was generated at the beginning, after modification you should get 'abababab'.
"""


@dataclass
class CharacterPair:
    char_1: str = "A"
    char_2: str = "B"

    def generate_balanced_string(self, length: int = 7) -> str:
        """
        Generate a string consisting of balanced occurrences of two characters.

        Parameters:
            length (int): The length of the generated string. Defaults to 7.

        Returns:
            str: The generated string with balanced occurrences of the two characters.

        Example:
            Input:
             character_pair = CharacterPair()
             character_pair.generate_balanced_string(10)
             Output:
            'AABABABBAB'
        """

        char_1_length = length // 2
        char_2_length = length - char_1_length
        random_number = random.randint(1, 2)

        if length % 2 != 0 and random_number == 1:
            char_1_length, char_2_length = char_2_length, char_1_length

        string = self.char_1 * char_1_length + self.char_2 * char_2_length
        return ''.join(random.sample(string, len(string)))

    def alternate_chars(self, text: str) -> str:
        """
        Modify a string so that consecutive letters alternate.

        Parameters:
            text (str): The input string.

        Returns:
            str: The modified string with alternating consecutive letters.

        Raises:
            ValueError: If either char_1 or char_2 is not present in the text.

        Example:
            Input:
             character_pair = CharacterPair("a", "b")
             character_pair.alternate_chars("abbbaaba")
             Output:
            'abababab'
        """

        if self.char_1 not in text or self.char_2 not in text:
            raise ValueError(f'Both {self.char_1} and {self.char_2} must be present in the text.')

        new_text = ''
        chars_counter = Counter(text)
        char_1_count = chars_counter[self.char_1]
        char_2_count = chars_counter[self.char_2]
        chars = self.char_1 + self.char_2

        for _ in range(min(char_1_count, char_2_count)):
            new_text += chars

        if char_1_count > char_2_count:
            new_text += self.char_1 * (char_1_count - char_2_count)
        elif char_2_count > char_1_count:
            new_text += self.char_2 * (char_2_count - char_1_count)
        return new_text


def main() -> None:
    char1 = "a"
    char2 = "b"
    character_pair = CharacterPair(char1, char2)
    balanced_string = character_pair.generate_balanced_string(9)
    print(balanced_string)
    print(character_pair.alternate_chars(balanced_string))


if __name__ == '__main__':
    main()
