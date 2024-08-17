from __future__ import annotations

from .Cyclist import Cyclist

class Sprinter(Cyclist):
    def __init__(
            self,
            identifier: int,
            name: str,
            average_power: float,
            average_speed: float
    ) -> Sprinter:
        super().__init__(
            identifier=identifier,
            name=name,
        )
        self.__average_power = average_power
        self.__average_speed = average_speed

    def get_average_power(self) -> float:
        return self.__average_power
    
    def __set_average_power(self, new_average_power: float) -> None:
        self.__average_power = new_average_power

    def get_average_speed(self) -> float:
        return self.__average_speed
    
    def __set_average_speed(self, new_average_speed: float) -> None:
        self.__average_speed = new_average_speed

    def print_type(self) -> None:
        return "Es un velocista"

    def __repr__(self) -> str:
        return (
            f"{super().__repr__()}"
            f"\nPotencia promedio: {self.__average_power:,} w"
            f"\nVelocidad promedio: {self.__average_speed:,} km/h"
        )