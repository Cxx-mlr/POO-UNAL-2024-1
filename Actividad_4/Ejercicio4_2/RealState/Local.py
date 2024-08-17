from __future__ import annotations

from .Property import Property

class Local(Property):
    class LocalType:
        INTERNAL: int = 0
        STREET: int = 1

    def __init__(
            self,
            property_id: int,
            area_in_square_meters: int,
            address: str,
            local_type: LocalType,
    ) -> Local:
        super().__init__(
            property_id=property_id,
            area_in_square_meters=area_in_square_meters,
            address=address
        )
        self._local_type: Local.LocalType = local_type
    
    def __repr__(self) -> str:
        return (
            f"{super().__repr__()}"
            f"\nTipo de local: {self._local_type}"
        )