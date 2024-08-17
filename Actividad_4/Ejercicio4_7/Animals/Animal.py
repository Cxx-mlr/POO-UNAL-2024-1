from __future__ import annotations

from abc import ABC, abstractmethod

class Animal(ABC):
    _sound: str
    _food: str
    _habitat: str
    _scientific_name: str

    @abstractmethod
    def get_sound(self) -> str:
        return self._sound
    
    @abstractmethod
    def get_food(self) -> str:
        return self._food

    @abstractmethod
    def get_habitat(self) -> str:
        return self._habitat

    @abstractmethod
    def get_scientific_name(self) -> str:
        return self._scientific_name