from utils.c_lib_wrapper import libc, float_to_c_wchar_p
from ctypes import *

def calculate_salary(hours_worked: int, hourly_rate: float, tax_rate: float) -> float:
    gross_salary = hours_worked * hourly_rate
    withholding_tax = (tax_rate / 100) * gross_salary
    net_salary = gross_salary - withholding_tax

    return gross_salary, withholding_tax, net_salary

def main():
    hours_worked = 48
    hourly_rate = 5000
    tax_rate = 12.5

    gross_salary, withholding_tax, net_salary = calculate_salary(hours_worked, hourly_rate, tax_rate)

    libc.printf(b"Salario bruto: %ls\n", float_to_c_wchar_p(gross_salary))
    libc.printf(b"%ls de impuestos: %ls\n", c_wchar_p("Retención"), float_to_c_wchar_p(withholding_tax))
    libc.printf(b"Salario neto: %ls\n", float_to_c_wchar_p(net_salary))

if __name__ == "__main__":
    main()