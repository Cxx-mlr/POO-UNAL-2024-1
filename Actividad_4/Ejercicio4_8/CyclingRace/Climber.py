from __future__ import annotations

from .Cyclist import Cyclist

class Climber(Cyclist):
    def __init__(
            self,
            identifier: int,
            name: str,
            average_acceleration: float,
            ramp_grade: float
    ) -> Climber:
        super().__init__(
            identifier=identifier,
            name=name,
        )
        self.__average_acceleration = average_acceleration
        self.__ramp_grade = ramp_grade

    def get_average_acceleration(self) -> float:
        return self.__average_acceleration
    
    def __set_average_acceleration(self, new_average_acceleration: float) -> None:
        self.__average_acceleration = new_average_acceleration

    def get_ramp_grade(self) -> float:
        return self.__ramp_grade
    
    def __set_ramp_grade(self, new_ramp_grade: float) -> None:
        self.__ramp_grade = new_ramp_grade

    def print_type(self) -> None:
        return "Es un escalador"

    def __repr__(self) -> str:
        return (
            f"{super().__repr__()}"
            f"\nAceleración promedio: {self.__average_acceleration:,} m/s^2"
            f"\nGrado de rampa: {self.__ramp_grade:,}°"
        )