from __future__ import annotations
import math

class Grades:
    def __init__(self) -> Grades:
        self.grade_list = [0, 0, 0, 0, 0]

    def calculate_average(self) -> float:
        return sum(self.grade_list) / len(self.grade_list)
    
    def calculate_standard_deviation(self) -> float:
        average = self.calculate_average()
        total_sum = 0

        for grade in self.grade_list:
            total_sum += math.pow(grade - average, 2)

        return math.sqrt(total_sum / len(self.grade_list))
    
    def calculate_min(self) -> float:
        return min(self.grade_list)
    
    def calculate_max(self) -> float:
        return max(self.grade_list)