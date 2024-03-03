from ctypes import *
from utils.c_lib_wrapper import libc, float_to_c_wchar_p
from math import pi

def main():
    radius = c_double()
    libc.printf(b"Introduzca el radio del %ls", c_wchar_p("círculo: "))
    libc.scanf(b"%lf", byref(radius))

    libc.printf(b"%ls: %ls\n", c_wchar_p("área"), float_to_c_wchar_p(pi*radius.value**2))
    libc.printf(b"longitud de la circunferencia: %ls\n", float_to_c_wchar_p(2*pi*radius.value))

if __name__ == "__main__":
    main()