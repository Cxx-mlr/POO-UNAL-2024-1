from Animals.Cat import Cat
from Animals.Dog import Dog
from Animals.Wolf import Wolf
from Animals.Lion import Lion
from Animals.Animal import Animal

class Ejercicio4_7:
	@staticmethod
	def main():
		animals: list[Animal] = [Cat(), Dog(), Wolf(), Lion()]

		for animal in animals:
			print(f"-- {animal.get_scientific_name()}")
			print(f"Sonido: {animal.get_sound()}")
			print(f"Alimentos: {animal.get_food()}")
			print(f"Hábitat: {animal.get_habitat()}")
			print()