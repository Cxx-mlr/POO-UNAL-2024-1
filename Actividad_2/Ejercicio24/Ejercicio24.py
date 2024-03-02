from Sphere import Sphere

class Ejercicio24:
    @staticmethod
    def main():
        a: Sphere = Sphere.new("A")
        b: Sphere = Sphere.new("B")
        c: Sphere = Sphere.new("C") 

        if a.weight < b.weight:
            if b.weight < c.weight:
                weightiest = c
            else:
                weightiest = b
        else:
            if a.weight < c.weight:
                weightiest = c
            else:
                weightiest = a

        print(f"\nLa esfera de mayor peso es {weightiest}")