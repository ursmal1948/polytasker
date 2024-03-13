"""
6. Napisz program, który pobiera od użytkownika trzy napisy, dopóki ilość samogłosek w napisach nie
będzie taka sama. Następnie przygotuj nowy napis, który będzie sklejeniem trzech pobranych napisów,
które wcześniej zmodyfikowano (ewentualnie zapisano do nowych napisów). Modyfikacja polega na przestawieniu
znaków w napisie w taki sposób, że najpierw występują samogłoski w kolejności wystąpienia w oryginalnym napisie,
a potem spółgłoski w kolejności wystąpienia w oryginalnym napisie. Przykładowo, kiedy mamy napis KAMIZELKA,
po modyfikacji ma postać AIEAKMZLK.
"""


def get_string(message: str) -> str:
    return input(f'{message}:\n')


def count_vowels(text: str) -> int:
    return sum(1 for c in text if c.lower() in 'aeyuio')


def get_strings(message: str, count: int = 3) -> str:
    while True:
        strings = [get_string(f'{i + 1}.{message}') for i in range(count)]
        vowels_count = [count_vowels(string) for string in strings]

        if all(count == vowels_count[0] for count in vowels_count):
            return ''.join(strings)


def rearrange_vowels_consonants(text: str) -> str:
    vowels = [c for c in text if c.isalpha() and c.lower() in 'aeyuio']
    consonants = [c for c in text if c.isalpha() and c.lower() not in 'aeyuio']
    return "".join(vowels + consonants)
