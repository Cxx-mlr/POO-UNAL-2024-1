from ctypes import *
from utils.c_lib_wrapper import libc

import atexit

class Person(Structure):
    _fields_ = [
        ("name", c_wchar_p),
        ("age", c_int)
    ]

def make_person(name: c_wchar_p, age: c_int):
    person_ptr = libc.malloc(sizeof(Person))
    person_ptr.contents.name = name
    person_ptr.contents.age = age

    atexit.register(libc.free, person_ptr)

    return person_ptr

def main():
    juan_age = c_int()
    libc.printf(b"Introduzca la edad de Juan: ")
    libc.scanf(b"%d", byref(juan_age))

    libc.malloc.restype = POINTER(Person)

    juan_ptr    = make_person(name="Juan"   , age=juan_age)
    alberto_ptr = make_person(name="Alberto", age=int(2/3 * juan_ptr.contents.age))
    ana_ptr     = make_person(name="Ana"    , age=int(4/3 * juan_ptr.contents.age))
    mom_ptr     = make_person(name="Mamá"   , age=int(juan_ptr.contents.age + alberto_ptr.contents.age + ana_ptr.contents.age))

    libc.printf(b"Las edades son:\n")
    libc.printf(b"%ls: %d\n", juan_ptr.contents.name, juan_ptr.contents.age)
    libc.printf(b"%ls: %d\n", alberto_ptr.contents.name, alberto_ptr.contents.age)
    libc.printf(b"%ls: %d\n", ana_ptr.contents.name, ana_ptr.contents.age)
    libc.printf(b"%ls: %d\n", mom_ptr.contents.name, mom_ptr.contents.age)

if __name__ == "__main__":
    main()