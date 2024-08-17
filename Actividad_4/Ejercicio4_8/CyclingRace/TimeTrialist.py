from __future__ import annotations

from .Cyclist import Cyclist

class TimeTrialist(Cyclist):
    def __init__(
            self,
            identifier: int,
            name: str,
            maximum_speed: float,
    ) -> TimeTrialist:
        super().__init__(
            identifier=identifier,
            name=name,
        )
        self.__maximum_speed = maximum_speed

    def get_maximum_speed(self) -> float:
        return self.__maximum_speed
    
    def __set_maximum_speed(self, new_maximum_speed: float) -> None:
        self.__maximum_speed = new_maximum_speed

    def print_type(self) -> None:
        return "Es un contrarrelojista"

    def __repr__(self) -> str:
        return (
            f"{super().__repr__()}"
            f"\nVelocidad máxima: {self.__maximum_speed:,} km/h"
        )