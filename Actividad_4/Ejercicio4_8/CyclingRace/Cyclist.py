from __future__ import annotations

from abc import ABC, abstractmethod

class Cyclist(ABC):
    def __init__(
            self,
            identifier: int,
            name: str
    ) -> Cyclist:
        self.__identifier = identifier
        self.__name = name
        self.__accumulated_time = 0

    def get_identifier(self) -> int:
        return self.__identifier
    
    def __set_identifier(self, new_identifier) -> None:
        self.__identifier = new_identifier

    def get_name(self) -> str:
        return self.__name
    
    def __set_name(self, new_name: str) -> None:
        self.__name = new_name

    def get_general_position(self, general_position: int) -> int:
        return general_position
    
    def __set_general_position(self, general_position: int) -> None:
        self.__general_position: int = general_position

    def get_accumulated_time(self) -> float:
        return self.__accumulated_time
    
    def __set_accumulated_time(self, new_accumulated_time: float) -> None:
        self.__accumulated_time = new_accumulated_time

    @abstractmethod
    def print_type(self) -> None:
        pass

    def __repr__(self) -> str:
        return (
            f"Identificador: {self.__identifier}"
            f"\nNombre: {self.__name}"
            f"\nTiempo Acumulado: {self.__accumulated_time:,}"
        )