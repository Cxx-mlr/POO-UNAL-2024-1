from __future__ import annotations
import math

class Triangle:
    side_1: float
    side_2: float
    side_3: float

    def __init__(self, side_1: float, side_2: float, side_3: float) -> Triangle:
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    @classmethod
    def new(cls) -> Triangle:
        print("Ingrese los 3 lados del triángulo: ")
        side_1 = float(input("\tLado 1: "))
        side_2 = float(input("\tLado 2: "))
        side_3 = float(input("\tLado 3: "))

        return cls(side_1, side_2, side_3)
    
    def calculate_perimeter(self) -> float:
        return self.side_1 + self.side_2 + self.side_3

    def calculate_semiperimeter(self) -> float:
        return self.calculate_perimeter() / 2
    
    def calculate_area(self) -> float:
        return math.sqrt(self.calculate_semiperimeter() *
                        (self.calculate_semiperimeter() - self.side_1) *
                        (self.calculate_semiperimeter() - self.side_2) *
                        (self.calculate_semiperimeter() - self.side_3)
        )
    
    def __str__(self) -> str:
        return (f"\tPerímetro: {self.calculate_perimeter()}" +
                f"\n\tSemiperímetro: {self.calculate_semiperimeter()}" +
                f"\n\tÁrea: {self.calculate_area()}")