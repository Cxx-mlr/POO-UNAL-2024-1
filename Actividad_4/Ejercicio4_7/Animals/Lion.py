from .Feline import Feline

class Lion(Feline):
    def get_sound(self) -> str:
        return "Rugido"
    
    def get_food(self) -> str:
        return "Carnívoro"
    
    def get_habitat(self) -> str:
        return "Praderas"
    
    def get_scientific_name(self) -> str:
        return "Panthera Leo"