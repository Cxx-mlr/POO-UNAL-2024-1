from __future__ import annotations

from .Apartment import Apartment

class FamilyApartment(Apartment):
    _price_per_square_meter: float = 2_000_000.0
    def __init__(
            self,
            property_id: int,
            area_in_square_meters: int,
            address: str,
            number_of_rooms: int,
            number_of_bathrooms: int,
            management_fee: float,
    ) -> FamilyApartment:
        super().__init__(
            property_id=property_id,
            area_in_square_meters=area_in_square_meters,
            address=address,
            number_of_rooms=number_of_rooms,
            number_of_bathrooms=number_of_bathrooms,
        )
        self._management_fee = management_fee

    def __repr__(self) -> str:
        return (
            f"{super().__repr__()}"
            f"\nValor de la administración: ${self._management_fee:,}"
        )