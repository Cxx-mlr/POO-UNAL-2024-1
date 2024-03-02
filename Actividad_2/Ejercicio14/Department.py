from __future__ import annotations
from typing import ClassVar

class Department:
    id: str
    sales: float
    base_salary: float

    total_sales: ClassVar[float] = 0

    def __init__(self, id: str, sales: float) -> Department:
        self.id = id
        self.sales = sales

        Department.total_sales += sales

    @classmethod
    def new(cls, id: str) -> Department:
        sales = float(input(f"\tVentas del departamento {id}: "))
        return cls(id=id, sales=sales)
    
    def calculate_monthly_salary(self):
        if self.sales > (0.33 * Department.total_sales):
            return Department.base_salary * 1.2
        else:
            return Department.base_salary