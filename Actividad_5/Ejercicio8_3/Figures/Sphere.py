from __future__ import annotations
import math

from .GeometricFigure import GeometricFigure

class Sphere(GeometricFigure):
    def __init__(self, radius: float) -> Sphere:
        self.__radius = radius
        super().set_volume(self.calculate_volume())
        super().set_surface_area(self.calculate_surface_area())

    def calculate_volume(self) -> float:
        return 4/3 * math.pi * math.pow(self.__radius, 3)

    def calculate_surface_area(self) -> float:
        return 4 * math.pi * math.pow(self.__radius, 2)