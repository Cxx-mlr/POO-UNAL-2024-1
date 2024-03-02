class Ejercicio11:
    @staticmethod
    def main():
        print("Introduzca 3 números distintos")
        number_1 = float(input("\tnúmero 1: "))
        number_2 = float(input("\tnúmero 2: "))
        number_3 = float(input("\tnúmero 3: "))

        if number_1.is_integer(): number_1 = int(number_1)
        if number_2.is_integer(): number_2 = int(number_2)
        if number_3.is_integer(): number_3 = int(number_3)

        if number_1 < number_2:
            if number_2 < number_3:
                greatest = number_3
            else:
                greatest = number_2
        else:
            if number_1 < number_3:
                greatest = number_3
            else:
                greatest = number_1

        print(f"\nEl valor mayor entre {number_1}, {number_2} y {number_3} es {greatest}")