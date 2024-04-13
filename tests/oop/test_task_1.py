import unittest

import pytest

from tasks.oop.task_1 import (
    Converter,
    EncodedLine,
    EncodedLinesService
)


class TestConverter:
    @pytest.mark.parametrize("decimal_number, base, expected_conversion", [
        (10, 2, '1010'),
        (13, 4, '31'),
        (22, 8, '26'),

    ])
    def test_convert_base(self, decimal_number, base, expected_conversion):
        conversion = Converter.convert_to_base(decimal_number, base)
        assert conversion == expected_conversion

    def test_convert_to_hex(self):
        decimal_number = 58
        conversion = Converter.convert_to_hex(decimal_number)
        assert conversion == "3A"


class TestEncodedLineMethods:

    def test_from_text(self):
        text = "2 10 10011"
        expected_result = EncodedLine(2, 10, '10011')
        result = EncodedLine.from_text(text)
        assert result == expected_result

    def test_from_text_incorrect_format(self):
        text = "2 A1 1001"
        with pytest.raises(ValueError) as e:
            EncodedLine.from_text(text)
        assert str(e.value) == "Incorrect format of the data"

    def test_is_same_code(self):
        encoded_line = EncodedLine(2, 2, "101")
        result = encoded_line.is_same_code()
        assert result == True

    @pytest.mark.parametrize("code1, code2, number, expected_result", [
        [3, 2, '1212', '110010'],
        [2, 16, '11011', '1B'],
        [2, 16, '11011', '1B'],
        [8, 10, '1254', '684'],
    ])
    def test_convert(self, code1, code2, number, expected_result):
        encoded_line = EncodedLine(code1, code2, number)
        assert encoded_line.convert() == expected_result


class TestEncodedLinesServiceMethods(unittest.TestCase):
    def setUp(self):
        self.encoded_lines = [
            EncodedLine(2, 4, '11010'),
            EncodedLine(3, 2, '11010'),
            EncodedLine(4, 8, '1231'),
            EncodedLine(10, 16, '11')
        ]
        self.conversions = ['122', '1101111', '155', 'B']
        self.file_path = 'tests/oop/data/task_1_codes.txt'

    def test_convert_numbers(self):
        encoded_lines_service = EncodedLinesService(self.encoded_lines)
        converted_numbers = encoded_lines_service.convert_numbers()
        self.assertEqual(converted_numbers, self.conversions)

    def test_from_file(self):
        lines = EncodedLinesService.from_file(self.file_path)
        expected_lines = EncodedLinesService(lines=[EncodedLine(code1=2, code2=4, code1_number='11010'),
                                                    EncodedLine(code1=10, code2=16, code1_number='14')])

        self.assertEqual(lines, expected_lines)
