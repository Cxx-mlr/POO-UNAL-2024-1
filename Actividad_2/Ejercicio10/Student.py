from __future__ import annotations

TUITION_FEE_BASE = 50_000
THRESHOLD_ASSETS = 2_000_000
THRESHOLD_SOCIAL_STRATUM = 3
INCREASING_PERCENTAGE = 3

class Student:
    registration_number: str
    name: str
    assets: float
    social_stratum: int

    def __init__(self, registration_number: str, name: str, assets: float, social_stratum: int) -> Student:
        self.registration_number = registration_number
        self.name = name
        self.assets = assets
        self.social_stratum = social_stratum

    @classmethod
    def new(cls) -> Student:
        print("Ingrese los datos del estudiante")
        registration_number = input("\tNúmero de inscripción: ")
        name = input("\tNombre: ")
        assets = float(input("\tPatrimonio: "))
        social_stratum = int(input("\tEstrato social: "))

        return cls(
            registration_number=registration_number,
            name=name,
            assets=assets,
            social_stratum=social_stratum
        )

    def calculate_tuition_feed(self) -> float:
        if self.assets > THRESHOLD_ASSETS and self.social_stratum > THRESHOLD_SOCIAL_STRATUM:
            return (INCREASING_PERCENTAGE / 100) * TUITION_FEE_BASE + TUITION_FEE_BASE
        else:
            return TUITION_FEE_BASE