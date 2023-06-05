from roman_conversion import RomanConverter

class TestRomanConversion:
    def test_roman_to_decimal(self):
        converter = RomanConverter()

        assert converter.roman_to_decimal("III") == 3
        assert converter.roman_to_decimal("IX") == 9
        assert converter.roman_to_decimal("LVIII") == 58
        assert converter.roman_to_decimal("MCMXCIV") == 1994

TestRomanConversion().test_roman_to_decimal()
