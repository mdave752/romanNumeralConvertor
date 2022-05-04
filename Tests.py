import unittest

from RomanToInteger import RomanToInteger
from IntegerToRoman import IntegerToRoman


class Tests(unittest.TestCase):
    def test_valid_numeral(self):
        data = "XVII"
        result = RomanToInteger().convert(data)
        self.assertEqual(result, 17)

    def test_valid_integer(self):
        data = 30
        result = IntegerToRoman().convert(data)
        self.assertEqual(result, "XXX")

    def test_bad_type_IntToRoman(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = IntegerToRoman().convert(data)

    def test_bad_type_RomToInt(self):
        data = 30
        with self.assertRaises(TypeError):
            result = RomanToInteger().convert(data)

    def test_invalid_string_RomToInt(self):
        data = "MMAXVI"
        with self.assertRaises(ValueError):
            result = RomanToInteger().convert(data)

    def test_invalid_no_string_RomToInt(self):
        data = ""
        with self.assertRaises(TypeError):
            result = RomanToInteger().convert(data)

    def test_value_range_RomToInt(self):
        data = "MMMCMMXLDCVIIIII"
        with self.assertRaises(TypeError):
            result = RomanToInteger().convert(data)

    def test_value_range_IntToRom(self):
        data = -1
        with self.assertRaises(ValueError):
            result = IntegerToRoman().convert(data)

    def test_convert_IntToString_to_RomToString(self):
        data = 23
        with self.assertRaises(TypeError):
            result = IntegerToRoman.convert(RomanToInteger().convert(data))
            self.assertEqual(result, 23)


if __name__ == '__main__':
    unittest.main()
