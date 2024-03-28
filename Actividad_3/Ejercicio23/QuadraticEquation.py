from __future__ import annotations
import math

class QuadraticEquation:
    a: float
    b: float
    c: float

    def __init__(self, a: float, b: float, c: float) -> QuadraticEquation:
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def new(cls) -> QuadraticEquation:
        a = float(input("Coeficiente a: "))
        b = float(input("Coeficiente b: "))
        c = float(input("Coeficiente c: "))

        return cls(a, b, c)

    def calculate_discriminant(self) -> float:
        return math.pow(self.b, 2) - 4 * self.a * self.c
    
    def find_solutions(self):
        discr = self.calculate_discriminant()
        if discr < 0:
            print("La ecuación no tiene solución en los números reales.")
        else:
            x_1 = (-self.b + math.sqrt(discr))/(2 * self.a)
            if discr == 0:
                print("La solución a la ecuación de segundo grado es:")
                print(f"\tx_1 = {x_1}")
            else:
                x_2 = (-self.b - math.sqrt(discr))/(2 * self.a)
                print("Las soluciones a la ecuación de segundo grado son:")
                print(f"\tx_1 = {x_1}")
                print(f"\tx_2 = {x_2}")