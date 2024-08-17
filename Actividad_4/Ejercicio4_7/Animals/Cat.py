from .Feline import Feline

class Cat(Feline):
    def get_sound(self) -> str:
        return "Maullido"
    
    def get_food(self) -> str:
        return "Ratones"
    
    def get_habitat(self) -> str:
        return "Doméstico"
    
    def get_scientific_name(self) -> str:
        return "Felis Silvestris Catus"