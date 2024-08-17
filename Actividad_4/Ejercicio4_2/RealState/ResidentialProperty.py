from __future__ import annotations

from .Property import Property

class ResidentialProperty(Property):
    def __init__(
            self,
            property_id: int,
            area_in_square_meters: int,
            address: str,
            number_of_rooms: int,
            number_of_bathrooms: int,
    ) -> ResidentialProperty:
        super().__init__(
            property_id=property_id,
            area_in_square_meters=area_in_square_meters,
            address=address,
        )
        self._number_of_rooms = number_of_rooms
        self._number_of_bathrooms = number_of_bathrooms

    def __repr__(self) -> str:
        return (
            f"{super().__repr__()}"
            f"\nNúmero de habitaciones: {self._number_of_rooms}"
            f"\nNúmero de baños: {self._number_of_bathrooms}"
        )