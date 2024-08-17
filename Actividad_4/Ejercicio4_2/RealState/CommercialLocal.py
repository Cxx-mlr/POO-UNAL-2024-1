from __future__ import annotations

from .Local import Local

class CommercialLocal(Local):
    _price_per_square_meter: float = 3_000_000.0
    def __init__(
            self,
            property_id: int,
            area_in_square_meters: int,
            address: str,
            local_type: Local.Type,
            shopping_center: str,
    ) -> CommercialLocal:
        super().__init__(
            property_id=property_id,
            area_in_square_meters=area_in_square_meters,
            address=address,
            local_type=local_type,
        )
        self._shopping_center = shopping_center
    
    def __repr__(self) -> str:
        return (
            f"{super().__repr__()}"
            f"\nCentro comercial: {self._local_type}"
        )