import time
import ctypes

clibrary = ctypes.CDLL("./sort_functions/sort.so")

# Define the sort function inputs and outputs
clibrary.sort.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int)
clibrary.sort.restype = None


def sort(array: list, threshold: int, return_runtime: bool) -> tuple:

    start_time = None
    elapsed_time = None

    if return_runtime:
        start_time = time.time()

    arr = (ctypes.c_int * len(array))(*array)
    size = len(array)

    clibrary.sort(arr, size, threshold)
    sorted_data = list(arr)

    if return_runtime:
        end_time = time.time()
        elapsed_time = end_time - start_time

    return (sorted_data, elapsed_time)