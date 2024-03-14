from typing import Callable

"""
W dwóch przygotowanych przez Ciebie plikach tekstowych znajdują się w każdym wierszu
słowa. Nie wiemy, ile jest słów w każdym pliku. Napisz program, który do trzeciego pliku
zapisuje tylko te słowa, które pojawiły się jednocześnie w dwóch plikach i zawierają w sobie
więcej spółgłosek niż samogłosek. Ze słów w trzecim pliku tekstowym utwórz jeden napis, w którym
kolejne słowa są oddzielone przecinkami i występują w kolejności alfabetycznej.
"""


def read_from_file(filename: str) -> list[str]:
    with open(filename, 'r') as f:
        multiple_items = [line.strip() for line in f.readlines()]
        words = []
        for row in multiple_items:
            items = row.split()
            for item in items:
                words.append(item.lower())
        return words


def get_common_words(words1: list[str], words2: list[str]) -> list[str]:
    return [word for word in words1 if word in words2]


def consonants_exceeds_vowels_count(text: str) -> bool:
    consonants_count = sum(1 for c in text if c.isalpha() and c.lower() not in 'aeyuio')
    vowels_count = sum(1 for c in text if c.isalpha() and c.lower() in 'aeyuio')
    return consonants_count > vowels_count


def save_fileterd_items_to_file(filename: str, items: list[str], filter_fn: Callable[[str], bool]) -> None:
    filtered_items = [item for item in items if filter_fn(item)]
    with open(filename, 'w') as f:
        f.writelines(
            filtered_items[i] + '\n'
            if i != len(filtered_items) - 1 else filtered_items[i] for i in range(len(filtered_items)))


def create_string_from_file(filename: str) -> str:
    items = read_from_file(filename)
    print(items)
    return ','.join(sorted(items))
