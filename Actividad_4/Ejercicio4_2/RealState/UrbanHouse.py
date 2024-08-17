from __future__ import annotations

from .House import House

class UrbanHouse(House):
    def __init__(
            self,
            property_id: int,
            area_in_square_meters: int,
            address: str,
            number_of_rooms: int,
            number_of_bathrooms: int,
            number_of_floors: int,
    ) -> UrbanHouse:
        super().__init__(
            property_id=property_id,
            area_in_square_meters=area_in_square_meters,
            address=address,
            number_of_rooms=number_of_rooms,
            number_of_bathrooms=number_of_bathrooms,
            number_of_floors=number_of_floors,
        )

    def __repr__(self) -> str:
        return super().__repr__()