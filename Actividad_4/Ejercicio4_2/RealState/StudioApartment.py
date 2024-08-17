from __future__ import annotations

from .Apartment import Apartment

class StudioApartment(Apartment):
    _price_per_square_meter: float = 1_500_000
    def __init__(
            self,
            property_id: int,
            area_in_square_meters: int,
            address: str,
    ) -> StudioApartment:
        super().__init__(
            property_id=property_id,
            area_in_square_meters=area_in_square_meters,
            address=address,
            number_of_rooms=1,
            number_of_bathrooms=1,
        )

    def __repr__(self) -> str:
        return super().__repr__()