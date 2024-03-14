"""
Zad 14
Wygeneruj napis składający się z samych liter a lub b o długości podanej
wcześniej od użytkownika. Napis musi zostać wygenerowany tak, żeby różnica
w ilości wystąpień liter b oraz a w napisie nie była większa niż 1. Następnie zmodyfikuj
napis w taki sposób, żeby kolejne litery a i b występowały na przemian. Na przykład na początku
wygenerowano napis abbbaaba, a po modyfikacji otrzymano abababab.
"""


def get_int(message: str) -> int:
    while True:
        try:
            num = int(input(message))
            if num > 0:
                return num
            else:
                print('Enter a positive integer')
        except ValueError:
            print('Please enter a valid integer')


def generate_balanced_string(length: int, letter1: str, letter2: str) -> str:
    letter1_count = length // 2
    letter2_count = length - letter1_count
    return letter1_count * letter1 + letter2_count * letter2


def alternate_chars(text: str) -> str:
    new_text = ''

    unique_letters = list(set(text))  # no order. Ordered dict.fromkeys will provide order but it not necessary here
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
