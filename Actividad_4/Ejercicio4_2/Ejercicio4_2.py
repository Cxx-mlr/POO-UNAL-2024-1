from RealState.FamilyApartment import FamilyApartment
from RealState.StudioApartment import StudioApartment

class Ejercicio4_2:
	@staticmethod
	def main():
		family_apartment = FamilyApartment(
			property_id=103067,
			area_in_square_meters=120,
			address="Avenida Santander 45-45",
			number_of_rooms=3,
			number_of_bathrooms=2,
			management_fee=200_000,
		)
		family_apartment.calculate_sale_price(family_apartment._price_per_square_meter)

		print("-- Apartamento Familiar")
		print(family_apartment)
		
		print()

		studio_apartment = StudioApartment(
			property_id=12354,
			area_in_square_meters=50,
			address="Avenida Caracas 30-15"
		)
		studio_apartment.calculate_sale_price(studio_apartment._price_per_square_meter)

		print("-- Apartamento Estudio")
		print(studio_apartment)