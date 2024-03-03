from ctypes import *
from utils.c_lib_wrapper import libc, float_to_c_wchar_p

def main():
    value = c_double()
    libc.printf(b"Introduzca un %ls para aplicar %ls: ", c_wchar_p("número"), c_wchar_p("potenciación"))
    libc.scanf(b"%lf", byref(value))

    libc.printf(b"(%ls)**2 = %ls\n", float_to_c_wchar_p(value.value), float_to_c_wchar_p(value.value ** 2))
    libc.printf(b"(%ls)**3 = %ls\n", float_to_c_wchar_p(value.value), float_to_c_wchar_p(value.value ** 3))

if __name__ == "__main__":
    main()