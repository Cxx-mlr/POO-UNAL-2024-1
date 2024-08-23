from __future__ import annotations
import math

from .GeometricFigure import GeometricFigure

class Pyramid(GeometricFigure):
    def __init__(
            self,
            base: float,
            height: float,
            apothem: float,
    ) -> Pyramid:
        self.__base = base
        self.__height = height
        self.__apothem = apothem
        super().set_volume(self.calculate_volume())
        super().set_surface_area(self.calculate_surface_area())

    def calculate_volume(self) -> float:
        return (math.pow(self.__base, 2) * self.__height) / 3

    def calculate_surface_area(self) -> float:
        base_area = math.pow(self.__base, 2)
        side_area = 2 * self.__base * self.__apothem
        return base_area + side_area