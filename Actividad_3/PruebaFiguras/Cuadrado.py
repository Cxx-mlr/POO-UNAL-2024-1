from __future__ import annotations
import math

class Cuadrado:
    lado: float

    def __init__(self, lado: float) -> Cuadrado:
        self.lado = lado

    def calcularÁrea(self) -> float:
        return math.pow(self.lado, 2)
    
    def calcularPerímetro(self) -> float:
        return 4 * self.lado