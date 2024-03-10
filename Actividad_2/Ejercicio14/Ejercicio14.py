from Department import Department

class Ejercicio14:
    @staticmethod
    def main():
        monthly_salary: float = float(input("Ingrese el salario mensual de los vendedores: "))
        Department.base_salary = monthly_salary

        print("\nIngrese las ventas de cada departamento")

        dep_1: Department = Department.new("1")
        dep_2: Department = Department.new("2")
        dep_3: Department = Department.new("3")

        print()
        print("Se muestran los datos ingresados e información adicional")
        print(f"\tVentas del departamento {dep_1.id}: ${dep_1.sales}")
        print(f"\tVentas del departamento {dep_2.id}: ${dep_2.sales}")
        print(f"\tVentas del departamento {dep_3.id}: ${dep_3.sales}")
        print()
        print(f"\tVentas totales de la empresa: ${Department.total_sales}")
        print("\tPorcentaje del 33% de las ventas totales de la empresa: " \
              f"${(Department.total_sales * 0.33):.2f}")
        print()
        print(f"\tSalario mensual del departamento {dep_1.id}: ${dep_1.calculate_monthly_salary()}")
        print(f"\tSalario mensual del departamento {dep_2.id}: ${dep_2.calculate_monthly_salary()}")
        print(f"\tSalario mensual del departamento {dep_3.id}: ${dep_3.calculate_monthly_salary()}")