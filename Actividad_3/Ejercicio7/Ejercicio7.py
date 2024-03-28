class Ejercicio7:
    @staticmethod
    def main():
        a = float(input("Introduzca un número a comparar: "))
        b = float(input("Introduzca otro número a comparar: "))

        if a.is_integer(): a = int(a)
        if b.is_integer(): b = int(b)

        if a < b:
            print(f"{a} es menor que {b}")
        elif a == b:
            print(f"{a} es igual a {b}")
        else:
            print(f"{a} es mayor que {b}")