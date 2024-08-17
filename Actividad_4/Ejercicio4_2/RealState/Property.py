from __future__ import annotations

class Property:
    def __init__(
            self,
            property_id: int,
            area_in_square_meters: int,
            address: str,
    ) -> Property:
        self._property_id = property_id
        self._area_in_square_meters = area_in_square_meters
        self._address = address

    def calculate_sale_price(self, price_per_square_meter: float) -> float:
        self._sale_price: float = price_per_square_meter * self._area_in_square_meters
        return self._sale_price
    
    def __repr__(self) -> str:
        return (
            f"Identificador inmobiliario: {self._property_id}"
            f"\nÁrea: {self._area_in_square_meters}"
            f"\nDirección: {self._address}"
            f"\nPrecio de venta: ${self._sale_price:,}"
        )