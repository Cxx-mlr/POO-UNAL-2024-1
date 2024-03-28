from __future__ import annotations
import math

class TriánguloRectángulo:
    base: float
    altura: float

    def __init__(self, base: float, altura: float) -> TriánguloRectángulo:
        self.base = base
        self.altura = altura

    def calcularÁrea(self) -> float:
        return 1/2 * self.base * self.altura
    
    def calcularPerímetro(self) -> float:
        return self.base + self.altura + self.calcularHipotenusa()

    def calcularHipotenusa(self) -> float:
        return math.sqrt(math.pow(self.altura, 2) + math.pow(self.base, 2))
    
    def determinarTipoTriángulo(self) -> float:
        if self.base == self.altura and self.base == self.calcularHipotenusa():
            print("Es un triángulo Equilátero")
        elif self.base != self.altura and self.base != self.calcularHipotenusa():
            print("Es un triángulo Escaleno")
        else:
            print("Es un triángulo Isósceles")