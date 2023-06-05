import math

class StatisticsCalculator:
    def calculate_statistics(self, numbers):
        n = len(numbers)

        if n == 0:
            return None, None

        mean = sum(numbers) / n
        variance = sum((x - mean) ** 2 for x in numbers) / n
        std_deviation = math.sqrt(variance)

        return mean, std_deviation
