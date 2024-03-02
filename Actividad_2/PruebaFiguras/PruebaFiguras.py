from Círculo import Círculo
from Rectángulo import Rectángulo
from Cuadrado import Cuadrado
from TriánguloRectángulo import TriánguloRectángulo

class PruebaFiguras:
    @staticmethod
    def main():
        figura1: Círculo = Círculo(2)
        figura2: Rectángulo = Rectángulo(1, 2)
        figura3: Cuadrado = Cuadrado(3)
        figura4: TriánguloRectángulo = TriánguloRectángulo(5, 3)

        print(f"El área del círculo es = {figura1.calcularÁrea()}")
        print(f"El perímetro del círculo es = {figura1.calcularPerímetro()}")
        print()
        print(f"El área del rectángulo es = {figura2.calcularÁrea()}")
        print(f"El perímetro del rectángulo es = {figura2.calcularPerímetro()}")
        print()
        print(f"El área del cuadrado es = {figura3.calcularÁrea()}")
        print(f"El perímetro del cuadrado es = {figura3.calcularPerímetro()}")
        print()
        print(f"El área del triángulo es = {figura4.calcularÁrea()}")
        print(f"El perímetro del triángulo es = {figura4.calcularPerímetro()}")
        figura4.determinarTipoTriángulo()