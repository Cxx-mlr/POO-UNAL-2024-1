from utils.c_lib_wrapper import libc, float_to_c_wchar_p

def main():
    sum = 0
    x, y = 20, 40

    sum += x
    x += y**2
    sum += x/y

    libc.printf(b"El valor de la suma es: %ls\n", float_to_c_wchar_p(sum))

if __name__ == "__main__":
    main()