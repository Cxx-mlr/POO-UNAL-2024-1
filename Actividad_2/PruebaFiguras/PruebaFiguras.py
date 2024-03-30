from Círculo import Círculo
from Rectángulo import Rectángulo
from Cuadrado import Cuadrado
from TriánguloRectángulo import TriánguloRectángulo

class PruebaFiguras:
    @staticmethod
    def main():
        radio_círculo = float(input("Ingrese el valor del radio del círculo: "))
        círculo: Círculo = Círculo(radio_círculo)

        base_rectángulo = float(input("Ingrese el valor de la base del rectángulo: "))
        altura_rectángulo = float(input("Ingrese el valor de la altura del rectángulo: "))
        rectángulo: Rectángulo = Rectángulo(
            base=base_rectángulo,
            altura=altura_rectángulo
        )

        lado_cuadrado = float(input("Ingrese el valor del lado del cuadrado: "))
        cuadrado: Cuadrado = Cuadrado(
            lado=lado_cuadrado
        )

        base_triángulo_rectángulo = float(input("Ingrese el valor de la base del triángulo rectángulo: "))
        altura_triángulo_rectángulo = float(input("Ingrese el valor de la altura del triángulo rectángulo: "))
        triángulo_rectángulo: TriánguloRectángulo = TriánguloRectángulo(
            base=base_triángulo_rectángulo,
            altura=altura_triángulo_rectángulo
        )

        print("\n\n")
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