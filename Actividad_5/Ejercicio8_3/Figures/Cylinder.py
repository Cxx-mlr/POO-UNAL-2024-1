from __future__ import annotations
import math

from .GeometricFigure import GeometricFigure

class Cylinder(GeometricFigure):
    def __init__(self, radius: float, height: float) -> Cylinder:
        self.__radius = radius
        self.__height = height
        super().set_volume(self.calculate_volume())
        super().set_surface_area(self.calculate_surface_area())

    def calculate_volume(self) -> float:
        return math.pi * math.pow(self.__radius, 2) * self.__height

    def calculate_surface_area(self) -> float:
        return (
            2 * math.pi * self.__radius * self.__height
            + 2 * math.pi * math.pow(self.__radius, 2)
        )