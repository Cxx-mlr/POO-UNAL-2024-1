from __future__ import annotations

class Sphere:
    weight: float
    name: str

    def __init__(self, weight: float, name: str) -> Sphere:
        self.weight = weight
        self.name = name
    
    @classmethod
    def new(cls, name: str) -> Sphere:
        weight = input(f"Peso de la esfera {name}: ")
        return Sphere(name=name, weight=weight)
    
    def __str__(self) -> str:
        return self.name