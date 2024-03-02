from Sphere import Sphere

class Ejercicio15:
    @staticmethod
    def main():
        print("Se necesitan tres esferas con el mismo peso y una esfera de peso diferente")
        a: Sphere = Sphere.new("A")
        b: Sphere = Sphere.new("B")
        c: Sphere = Sphere.new("C")
        d: Sphere = Sphere.new("D")

        s = "La esfera {} es la diferente y es de {} peso"

        if a.weight == b.weight and a.weight == c.weight:
            x = d
            if d.weight > a.weight:
                y = "mayor"
            else:
                y = "menor"
        elif a.weight == b.weight and a.weight == d.weight:
            x = c
            if c.weight > a.weight:
                y = "mayor"
            else:
                y = "menor"
        elif a.weight == c.weight and a.weight == d.weight:
            x = b
            if b.weight > a.weight:
                y = "mayor"
            else:
                y = "menor"
        else:
            x = a
            if a.weight > b.weight:
                y = "mayor"
            else:
                y = "menor"
        
        print(s.format(x, y))