from __future__ import annotations

class Person:
    def __init__(
            self,
            first_name: str,
            last_name: str,
            phone: str,
            address: str
    ) -> Person:
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address