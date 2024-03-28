from Círculo import Círculo
from Rectángulo import Rectángulo
from Cuadrado import Cuadrado
from TriánguloRectángulo import TriánguloRectángulo

class PruebaFiguras:
    @staticmethod
    def main():
        círculo: Círculo = Círculo(2)
        rectángulo: Rectángulo = Rectángulo(1, 2)
        cuadrado: Cuadrado = Cuadrado(3)
        triángulo_rectángulo: TriánguloRectángulo = TriánguloRectángulo(5, 3)

        print(f"El área del círculo es = {círculo.calcularÁrea()}")
        print(f"El perímetro del círculo es = {círculo.calcularPerímetro()}")
        print()
        print(f"El área del rectángulo es = {rectángulo.calcularÁrea()}")
        print(f"El perímetro del rectángulo es = {rectángulo.calcularPerímetro()}")
        print()
        print(f"El área del cuadrado es = {cuadrado.calcularÁrea()}")
        print(f"El perímetro del cuadrado es = {cuadrado.calcularPerímetro()}")
        print()
        print(f"El área del triángulo es = {triángulo_rectángulo.calcularÁrea()}")
        print(f"El perímetro del triángulo es = {triángulo_rectángulo.calcularPerímetro()}")
        triángulo_rectángulo.determinarTipoTriángulo()