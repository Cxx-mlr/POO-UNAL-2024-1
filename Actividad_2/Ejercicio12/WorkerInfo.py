from __future__ import annotations

THRESHOLD_REGULAR_HOURS = 40
THRESHOLD_OVERTIME_HOURS = 8

class WorkerInfo:
    name: str
    hours_worked_per_week: float
    hourly_rate: float

    def __init__(self, name: str, hours_worked_per_week: float, hourly_rate: float) -> WorkerInfo:
        self.name = name
        self.hours_worked_per_week = hours_worked_per_week
        self.hourly_rate = hourly_rate

    @classmethod
    def new(cls) -> WorkerInfo:
        print("Ingrese los datos del trabajador")
        name = input("\tNombre: ")
        hours_worked_per_week = float(input("\tHoras trabajadas en la semana: "))
        hourly_rate = float(input("\tTarifa por hora: "))
        return cls(name=name, hours_worked_per_week=hours_worked_per_week, hourly_rate=hourly_rate)

    def calculate_final_payment(self) -> float:
        regular_hours = 0
        overtime_hours = 0
        regular_pay =  0
        overtime_pay = 0
        excess_overtime_hours = 0

        if self.hours_worked_per_week > THRESHOLD_REGULAR_HOURS:
            regular_hours = THRESHOLD_REGULAR_HOURS
            overtime_hours = self.hours_worked_per_week - regular_hours

            if overtime_hours > THRESHOLD_OVERTIME_HOURS:
                excess_overtime_hours = overtime_hours - THRESHOLD_OVERTIME_HOURS
                overtime_hours = 8
        else:
            regular_hours = self.hours_worked_per_week
        
        regular_pay = self.hourly_rate * regular_hours
        overtime_pay = (self.hourly_rate * 2 * overtime_hours +
                        self.hourly_rate * 3 * excess_overtime_hours)

        return regular_pay + overtime_pay