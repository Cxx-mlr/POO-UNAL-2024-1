import platform, locale
import ctypes

try:
    if (system := platform.system()) == "Windows":
        libc = ctypes.cdll.msvcrt
    elif system == "Linux":
        libc = ctypes.CDLL("libc.so.6")
    else:
        raise RuntimeError("Unsupported operating system detected. Only Windows and Linux are supported.")
except OSError as err:
    print(f"Error loading C library: {err}")
else:
    libc.setlocale(locale.LC_ALL, "")
    libc.setlocale(locale.LC_NUMERIC, "C.UTF-8")

def float_to_c_wchar_p(value: float) -> ctypes.c_wchar_p:
    assert isinstance(value, float) or isinstance(value, int), "The value must be either a float or an integer."
    return ctypes.c_wchar_p(f"{value}")