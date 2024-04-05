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


class Converter:
    @staticmethod
    def convert_to_base(number: int, target_base: int) -> str:
        if number == 0:
            return '0'
        digits = []
        while number:
            digit = number % target_base
            digits.append(str(digit))
            number //= target_base
        return ''.join(digits)[::-1]

    @staticmethod
    def convert_to_hex(number: int) -> str:
        binary_num = Converter.convert_to_base(number, 2)
        print(binary_num)
        while len(binary_num) % 4 != 0:
            binary_num = '0' + binary_num
        groups_of_four = [binary_num[i:i + 4] for i in range(0, len(binary_num), 4)]
        numbers = []
        for group in groups_of_four:
            pow_ = len(group) - 1
            sum_ = 0
            for d in group:
                if d == '1':
                    sum_ += (2 ** pow_)
                pow_ -= 1
            numbers.append(sum_)

        decimal_to_hex = {
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'
        }
        return ''.join(decimal_to_hex[n] if n >= 10 else str(n) for n in numbers)


@dataclass
class EncodedLine:
    code1: int = 2
    code2: int = 4
    code1_number: str = ''

    @classmethod
    def from_text(cls, text: str, regex: str = r'^([2-9]|10|16) ([2-9]|10|16) ([0-9A-F]+)$') -> Self:
        if not re.match(regex, text):
            raise ValueError("Incorrect format of the data")

        nums = text.split(' ')
        return cls(int(nums[0]), int(nums[1]), nums[2])

    def is_same_code(self) -> bool:
        return self.code1 == self.code2

    def convert(self):
        decimal_number = int(self.code1_number, self.code1)
        if self.code2 == 16:
            return Converter.convert_to_hex(decimal_number)
        return Converter.convert_to_base(decimal_number, self.code2)


@dataclass
class EncodedLinesService:
    lines: list[EncodedLine] = field(default_factory=list)

    def __str__(self) -> str:
        return f'Encoded numbers.: {self.lines}'

    def convert_numbers(self):
        return [line.convert() for line in self.lines]

    def write_converted_numbers(self, filename: str) -> None:
        FileService.write(filename, self.convert_numbers())

    @classmethod
    def from_file(cls, filename: str) -> Self:
        lines = FileService.read(filename)
        encoded_lines = [EncodedLine.from_text(line) for line in lines]
        return cls([line for line in encoded_lines if not line.is_same_code()])


def main() -> None:
    n = EncodedLine(2, 4, '1010')
    print(n.convert())
    numbers_service = EncodedLinesService.from_file('data/codes.txt')
    print(numbers_service)
    print(numbers_service.convert_numbers())
    numbers_service.write_converted_numbers("data/encoded.txt")
    print(EncodedLine(3, 2, '1212').convert())
    # print(EncodedLine(2, 16, '11011').convert())
    print(EncodedLine(10, 16, '14').convert())
    lines = EncodedLinesService.from_file("data/codes.txt")
    print(lines)
    print(Converter.convert_to_base(22, 8))


if __name__ == '__main__':
    main()
