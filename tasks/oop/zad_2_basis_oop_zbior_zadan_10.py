import re
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
    def write(filename: str, data: list[str]) -> None:
        with open(filename, 'w') as f:
            f.writelines(data[i] + "\n" if i != len(data) - 1 else data[i] for i in range(len(data)))


@dataclass
class EncodedLine:
    initial_base: int = 2
    target_base: int = 4
    code_1_number: str | int = ''

    @classmethod
    def from_text(cls, text: str) -> Self:
        if not re.match(r'^\d|10 \d|10 \d+$', text):
            raise ValueError("Incorrect format of the data")

        nums = text.split(' ')
        return cls(int(nums[0]), int(nums[1]), nums[2])

    def convert(self):
        decimal_number = int(self.code_1_number, self.initial_base)
        print(f'DECIMAL: {decimal_number}')
        return Converter.convert_base(decimal_number, self.target_base)


@dataclass
class EncodedLinesService:
    numbers: list[EncodedLine] = field(default_factory=list)

    def __str__(self) -> str:
        return f'Encoded numbers.: {self.numbers}'

    def convert_numbers(self):
        converted_numbers = []
        for number in self.numbers:
            converted_number = number.convert()
            converted_numbers.append(converted_number)
        return converted_numbers

    def write_converted_numbers(self, filename: str) -> None:
        FileService.write(filename, self.convert_numbers())

    @classmethod
    def from_file(cls, filename: str) -> Self:
        lines = FileService.read(filename)
        return cls([EncodedLine.from_text(line) for line in lines])


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
    n = EncodedLine(2, 4, '1010')
    print(n.convert())
    numbers_service = EncodedLinesService.from_file('data/codes.txt')
    print(numbers_service)
    print(numbers_service.convert_numbers())
    numbers_service.write_converted_numbers("data/encoded.txt")


if __name__ == '__main__':
    main()
