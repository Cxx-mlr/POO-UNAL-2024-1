from __future__ import annotations

class Employee:
    id: str
    name: str
    hours_worked_per_month: float
    hourly_rate: float
    withholding_tax_percentage: float

    def __init__(self, id: str, name: str, hours_worked_per_month: float, hourly_rate: float, withholding_tax_percentage: float) -> Employee:
        self.id = id
        self.name = name
        self.hours_worked_per_month = hours_worked_per_month
        self.hourly_rate = hourly_rate
        self.withholding_tax_percentage = withholding_tax_percentage

    @classmethod
    def new(cls) -> Employee:
        print("Ingrese los datos del empleado")
        id = input("\tCódigo: ")
        name = input("\tNombre: ")
        hours_worked_per_month = float(input("\tHoras trabajadas al mes: "))
        hourly_rate = float(input("\tValor por hora trabajada: "))
        withholding_tax_percentage = float(input("\tPorcentaje de retención en la fuente: "))

        return cls(
            id=id,
            name=name,
            hours_worked_per_month=hours_worked_per_month,
            hourly_rate=hourly_rate,
            withholding_tax_percentage=withholding_tax_percentage
        )

    def calculate_gross_salary(self) -> float:
        return self.hours_worked_per_month * self.hourly_rate
    
    def calculate_net_salary(self) -> float:
        withholding_tax = (self.withholding_tax_percentage / 100) * self.calculate_gross_salary()

        return self.calculate_gross_salary() - withholding_tax
    
    def __str__(self) -> str:
        return (f"\tCódigo: {self.id}" +
                f"\n\tNombre: {self.name}" +
                f"\n\tSalario bruto: {self.calculate_gross_salary():,}" +
                f"\n\tSalario neto: {self.calculate_net_salary():,}")