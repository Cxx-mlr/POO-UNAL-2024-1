from __future__ import annotations

class Employee:
    name: str
    hourly_rate: float
    hours_worked_per_month: float

    def __init__(self, name: str, hourly_rate: float, hours_worked_per_month: float) -> Employee:
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked_per_month = hours_worked_per_month

    @classmethod
    def new(cls) -> Employee:
        print("Ingrese los datos del empleado")
        name = input("\tNombre: ")
        hourly_rate = float(input("\tSalario básico por hora: "))
        hours_worked_per_month = float(input("\tHoras trabajadas en el mes: "))

        return cls(name=name, hourly_rate=hourly_rate, hours_worked_per_month=hours_worked_per_month)

    def calculate_net_salary(self) -> float:
        return self.hourly_rate * self.hours_worked_per_month

    def __str__(self) -> str:
        employee_info = f"\tNombre: {self.name}"
        net_salary = self.calculate_net_salary()

        if net_salary > 450_000:
            employee_info += f"\n\tSalario mensual: {net_salary}"
        return employee_info