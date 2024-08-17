from __future__ import annotations

from .Cyclist import Cyclist

class Team:
    def __init__(
            self,
            name: str,
            country: str
    ) -> Team:
        self.__name = name
        self.__country = country
        self.__total_time = 0
        self.__cyclists: Cyclist = []

    def get_name(self) -> str:
        return self.__name
    
    def __set_name(self, new_name: str) -> None:
        self.__name = new_name

    def get_country(self) -> str:
        return self.__country
    
    def __set_country(self, new_country: str) -> None:
        self.__country = new_country

    def add_cyclist(self, cyclist: Cyclist) -> None:
        self.__cyclists.append(cyclist)

    def list_cyclists(self) -> None:
        for cyclist in self.__cyclists:
            print(f"- {cyclist.get_name()}")

    def search_cyclist(self) -> None:
        cyclist_name = input("Ingrese el nombre del ciclista: ")
        for cyclist in self.__cyclists:
            if cyclist._get_name() == cyclist_name:
                print(cyclist)

    def calculate_total_time(self) -> None:
        for cyclist in self.__cyclists:
            self.__total_time += cyclist.get_accumulated_time()

    def __repr__(self) -> str:
        return (
            f"Nombre del equipo: {self.__name}"
            f"\nPaís: {self.__country}"
            f"\nTiempo total del equipo: {self.__total_time:,}"
        )