class RomanConverter:
    def __init__(self):
        self.roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def roman_to_decimal(self, roman_number):
        decimal_number = 0
        previous_value = 0

        for char in reversed(roman_number):
            value = self.roman_values[char]
            if value < previous_value:
                decimal_number -= value
            else:
                decimal_number += value
            previous_value = value

        return decimal_number
