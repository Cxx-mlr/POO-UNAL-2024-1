from __future__ import annotations

from .UrbanHouse import UrbanHouse

class GatedCommunityHouse(UrbanHouse):
    _price_per_square_meter: float = 2_500_000.0
    def __init__(
            self,
            property_id: int,
            area_in_square_meters: int,
            address: str,
            number_of_rooms: int,
            number_of_bathrooms: int,
            number_of_floors: int,
            management_fee: float,
            has_swimming_pool: bool,
            has_sports_fields: bool
    ) -> GatedCommunityHouse:
        super().__init__(
            property_id=property_id,
            area_in_square_meters=area_in_square_meters,
            address=address,
            number_of_rooms=number_of_rooms,
            number_of_bathrooms=number_of_bathrooms,
            number_of_floors=number_of_floors,
        )
        self._management_fee = management_fee
        self._has_swimming_pool = has_swimming_pool
        self._has_sports_fields = has_sports_fields

    def __repr__(self) -> str:
        return (
            f"{super().__repr__()}"
            f"\nValor de la administración: ${self._management_fee}"
            f"\nTiene piscina? {self._has_swimming_pool}"
            f"\nTiene campos deportivos? {self._has_sports_fields}"
        )