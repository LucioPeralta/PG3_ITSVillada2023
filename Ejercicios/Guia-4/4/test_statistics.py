from statistics import StatisticsCalculator
import math
import pytest

class TestStatisticsCalculator:
    def test_calculate_statistics(self):
        calculator = StatisticsCalculator()
        numbers = [2, 4, 6, 8, 10]
        mean, std_deviation = calculator.calculate_statistics(numbers)

        assert math.isclose(mean, 6.0)
        assert math.isclose(std_deviation, 2.8284271247461903)

pytest.main()
