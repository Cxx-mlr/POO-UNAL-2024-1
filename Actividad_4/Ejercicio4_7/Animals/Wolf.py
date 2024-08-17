from .Canid import Canid

class Wolf(Canid):
    def get_sound(self) -> str:
        return "Aullido"
    
    def get_food(self) -> str:
        return "Carnívoro"
    
    def get_habitat(self) -> str:
        return "Bosque"
    
    def get_scientific_name(self) -> str:
        return "Canis Lupus"