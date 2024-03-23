from dataclasses import dataclass, field
from typing import Self

"""W pliku tekstowym umieszczono w każdym wierszu kod1 (liczba całkowita
z przedziału <2,9>) po znaku spacji kod2 (liczba całkowita z przedziału
<2,9>) oraz po znaku spacji liczbę zapisaną w kodzie kod1. Przykładowa
postać wiersza w pliku tekstowym to: 2 4 1010, co oznacza, że kod1
to kod dwójkowy, kod2 to kod czwórkowy, natomiast 1010 to liczba
zapisana w tym przypadku w kodzie dwójkowym. Stosując elementy
obiektowości napisz program, który pobierze z pliku tekstowego opisane
wyżej dane i do nowego pliku tekstowego zapisze liczby zapisane
w kodzie kod1 przekonwertowane na kod2. Czyli w przypadku naszego
przykładu w nowym pliku musi znaleźć się 22, co jest reprezentacją
w kodzie czwórkowym liczby 1010 zapisanej binarnie. Wiersze, w których
kod1 okazał się taki sam jak kod2 należy zapisać do osobnego pliku
o wybranej przez Ciebie nazwie.
"""


class FileService:
    @staticmethod
    def read(filename: str) -> list[str]:
        with open(filename, 'r') as f:
            return [line.strip() for line in f.readlines()]

    @staticmethod
    def write(filename: str, data: str) -> None:
        pass


@dataclass
class Numbers:
    initial_base: int = 2
    target_base: int = 4
    code_1_number: str | int = ''

    @classmethod
    def from_text(cls, text: str) -> Self:
        nums = text.split(' ')
        return cls(int(nums[0]), int(nums[1]), nums[2])

    def convert_(self):
        number_decimal = int(self.code_1_number, int(self.initial_base))
        print(f'DECIMAL: {number_decimal}')
        converted_number = Converter.convert_base(number_decimal, self.target_base)
        return converted_number


@dataclass
class NumbersService:
    many_numbers: list[Numbers] = field(default_factory=list)

    def __str__(self) -> str:
        return f'Many numbers: {self.many_numbers}'

    @classmethod
    def from_file(cls, filename: str) -> Self:
        lines = FileService.read(filename)
        return cls([Numbers.from_text(line) for line in lines])


class Converter:
    @staticmethod
    def convert_base(number, target_base: int) -> int | str:
        if number == 0:
            return '0'
        digits = []
        while number:
            digit = number % target_base
            digits.append(str(digit))
            number //= target_base
        return ''.join(digits)[::-1]


def main() -> None:
    n = Numbers(4, 2, '20')
    print(n.convert_())


if __name__ == '__main__':
    main()
