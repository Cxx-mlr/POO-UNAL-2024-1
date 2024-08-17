from __future__ import annotations

from .House import House

class RuralHouse(House):
    _price_per_square_meter: float = 1_500_000.0
    def __init__(
            self,
            property_id: int,
            area_in_square_meters: int,
            address: str,
            number_of_rooms: int,
            number_of_bathrooms: int,
            number_of_floors: int,
            distance_from_municipal_seat: int,
            altitude: int,
    ) -> RuralHouse:
        super().__init__(
            property_id=property_id,
            area_in_square_meters=area_in_square_meters,
            address=address,
            number_of_rooms=number_of_rooms,
            number_of_bathrooms=number_of_bathrooms,
            number_of_floors=number_of_floors,
        )
        self._distance_from_municipal_seat = distance_from_municipal_seat
        self._altitude = altitude

    def __repr__(self) -> str:
        return (
            f"{super().__repr__()}"
            f"\nDistancia la cabecera municipal: {self._distance_from_municipal_seat} km."
            f"\nAltitud sobre el nivel del mar: {self._altitude} metros."
        )