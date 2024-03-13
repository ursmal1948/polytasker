import random
import string
from typing import Callable
from collections import defaultdict
from algohub.data.random_number import rand_chr


# 1. Napisz program, w którym generujesz napis. Napis składa się z parzystej
# ilości znaków. Ilość znaków losujesz z przedziału <30,100>. Znaki
# na pozycjach parzystych w napisie są losowane jako litery z przedziału
# <A,K>. Natomiast znaki na pozycjach nieparzystych w napisie są losowane
# jako litery z przedziału <L,Z>. Dla wygenerowanego napisu:

# -> Zlicz, ile jest w nim liter o kodzie ASCII podzielnym przez 5.
#  Wygeneruj na podstawie otrzymanego napisu nowy napis, w którym każdą
# literę poprzedzisz jej odpowiednikiem – małą literą. Przykładowo
# dla napisu: ABCD wynikiem będzie aAbBcCdD.

# -> Wygeneruj na podstawie otrzymanego napisu nowy napis, w którym każdą
# literę zastąpisz wyrazem zaczynającym się od tej litery. Przykładowy
# zbiór wyrazów umieść w tablicy jednowymiarowej napisów, którą
# wcześniej przygotujesz lub pobierzesz z pliku tekstowego. Jeżeli
# w zbiorze wyrazów jest więcej wyrazów zaczynających się od tej samej
# litery, wybierz ten o większej sumie kodów ASCII. Przykładowo dla
# napisu ABC wynikiem może być AdamBeataCelina.

def get_length_until(r_min: int, r_max: int, condition_fn: Callable[[int], bool]) -> int:
    if r_min > r_max:
        raise ValueError("Incorrect range")
    while not (condition_fn(v := random.randint(r_min, r_max))):
        pass
    return v


def generate_string(length: int, even_min_char: str, even_max_char: str, odd_min_char: str, odd_max_char: str) -> str:
    chars = []
    for i in range(length):
        if i % 2 == 0:
            chars.append(rand_chr(even_min_char, even_max_char))
        else:
            chars.append(rand_chr(odd_min_char, odd_max_char))

    return ''.join(chars)


def count_feature_occurrences(
        text: str,
        featuer_check: Callable[[str], bool] = lambda c: ord(c) % 5 == 0):
    return sum(1 for c in text if featuer_check(c))


def modify_text(text: str) -> str:
    chars = list(text)
    for i in range(len(chars)):
        char = chars[i]
        if char.isalpha() and char.isupper():
            chars[i] = chars[i].lower() + chars[i]
    return ''.join(chars)


def read_from_file(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [word.strip() for word in f.readlines()]


def find_words_starting_with_letter(items: list[str], letter: str) -> str | list[str]:
    return [c for c in items if c[0] == letter]


def select_representative_word_by_first_letter(items: list[str]) -> dict[str, str]:
    group_by_letter = defaultdict(str)
    for letter in string.ascii_uppercase:
        matching_words = find_words_starting_with_letter(items, letter)
        selected_word = matching_words[0] if len(matching_words) == 1 else max(matching_words,
                                                                               key=lambda word: sum(
                                                                                   ord(char) for char in word))
        group_by_letter[letter] = selected_word
    return dict(group_by_letter)


def map_characters_to_representative_words(text: str, filename: str) -> str:
    strings = read_from_file(filename)
    representative_word = select_representative_word_by_first_letter(strings)
    mapped_words = [representative_word[char] for char in text]
    return '|'.join(mapped_words)
