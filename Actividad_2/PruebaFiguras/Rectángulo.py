from __future__ import annotations

class Rectángulo:
    base: float
    altura: float

    def __init__(self, base: float, altura: float) -> Rectángulo:
        self.base = base
        self.altura = altura

    def calcularÁrea(self) -> float:
        return self.base * self.altura
    
    def calcularPerímetro(self) -> float:
        return (self.base * 2) + (self.altura * 2)