from __future__ import annotations
import math

class EquilateralTriangle:
    side_length: float

    def __init__(self, side_length: float) -> EquilateralTriangle:
        self.side_length = side_length

    @classmethod
    def new(cls) -> EquilateralTriangle:
        side_lenght = float(input("Ingrese el lado de un triángulo equilátero: "))
        return cls(side_lenght)

    def calculate_height(self) -> float:
        return math.sqrt(
            math.pow(self.side_length, 2) - math.pow(self.side_length/2, 2)
        )

    def calculate_perimeter(self) -> float:
        return self.side_length * 3
    
    def calculate_area(self) -> float:
        return 1/2 * self.side_length * self.calculate_height()
    
    def __str__(self) -> str:
        return (f"\tPerímetro: {self.calculate_perimeter()}" +
                f"\n\tAltura: {self.calculate_height()}" +
                f"\n\tÁrea: {self.calculate_area()}")