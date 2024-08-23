from __future__ import annotations

class GeometricFigure:
    def __init__(self) -> GeometricFigure:
        self.__volume: float = 0.0
        self.__surface_area: float = 0.0

    def set_volume(self, new_volume: float) -> None:
        self.__volume = new_volume

    def set_surface_area(self, new_surface_area: float) -> None:
        self.__surface_area = new_surface_area

    def get_volume(self) -> float:
        return self.__volume
    
    def get_surface_area(self) -> float:
        return self.__surface_area