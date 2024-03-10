from __future__ import annotations

class Sphere:
    weight: float
    id: str

    def __init__(self, weight: float, id: str) -> Sphere:
        self.weight = weight
        self.id = id
    
    @classmethod
    def new(cls, id: str) -> Sphere:
        weight = input(f"Peso de la esfera {id}: ")
        return Sphere(id=id, weight=weight)
    
    def __str__(self) -> str:
        return self.id