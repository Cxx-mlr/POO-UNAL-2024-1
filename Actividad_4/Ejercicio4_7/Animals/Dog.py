from .Canid import Canid

class Dog(Canid):
    def get_sound(self) -> str:
        return "Ladrido"
    
    def get_food(self) -> str:
        return "Carnívoro"
    
    def get_habitat(self) -> str:
        return "Doméstico"
    
    def get_scientific_name(self) -> str:
        return "Canis Lupus Familiaris"