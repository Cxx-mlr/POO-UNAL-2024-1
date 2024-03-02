from __future__ import annotations
import math

class Círculo:
    radio: float

    def __init__(self, radio: float) -> Círculo:
        self.radio = radio

    def calcularÁrea(self) -> float:
        return math.pi * math.pow(self.radio, 2)
    
    def calcularPerímetro(self) -> float:
        return (2 * math.pi) * self.radio