import os
import platform
import time 
import ctypes
from cffi import FFI
from typing import Union, Tuple, List


class SortFunctions:

    def __init__(self):

        base_path = os.path.join("sort_functions", "sort_functions_c")
        self.os_system = platform.system()

        # Establish connections to the C libraries
        if self.os_system == "Darwin" or self.os_system == "Linux":
            
            self.insertion_sort_clibary = ctypes.CDLL(os.path.join(base_path, "insertionSort.so"))
            self.merge_sort_clibrary = ctypes.CDLL(os.path.join(base_path, "mergeSort.so"))
            self.hybrid_sort_clibrary = ctypes.CDLL(os.path.join(base_path, "sort.so"))

        elif self.os_system == "Windows":

            self.insertion_sort_clibary = ctypes.WinDLL(os.path.join(base_path, "insertionSort.dll"))
            self.merge_sort_clibrary = ctypes.WinDLL(os.path.join(base_path, "mergeSort.dll"))
            self.hybrid_sort_clibrary = ctypes.WinDLL(os.path.join(base_path, "sort.dll"))

        
        # Define the sort function inputs and outputs
        self.insertion_sort_clibary.insertionSort.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)
        self.insertion_sort_clibary.insertionSort.restype = None

        self.merge_sort_clibrary.mergeSort.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)
        self.merge_sort_clibrary.mergeSort.restype = None

        self.hybrid_sort_clibrary.sort.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int)
        self.hybrid_sort_clibrary.sort.restype = None


    def sort(self, array: List[int], option: str, return_runtime: bool) -> tuple:

        start_time = None
        elapsed_time = None

        if return_runtime:
            start_time = time.time()

        arr = (ctypes.c_int * len(array))(*array)
        size = len(array)


        if option == "insertion":

            self.insertion_sort_clibary.insertionSort(arr, size)
            sorted_data = list(arr)

        elif option == "merge":

            self.merge_sort_clibrary.mergeSort(arr, size)
            sorted_data = list(arr)


        if return_runtime:
            end_time = time.time()
            elapsed_time = end_time - start_time

            return (sorted_data, elapsed_time)
        
        elif return_runtime == False:
            return sorted_data


    def hybrid_sort(self, array: List[int], threshold: int, return_runtime: bool) -> Union[Tuple, List[int]]:

        start_time = None
        elapsed_time = None

        if return_runtime:
            start_time = time.time()

        arr = (ctypes.c_int * len(array))(*array)
        size = len(array)

        self.hybrid_sort_clibrary.sort(arr, size, threshold)
        sorted_data = list(arr)

        if return_runtime:
            end_time = time.time()
            elapsed_time = end_time - start_time

            return (sorted_data, elapsed_time)

        elif return_runtime == False:
            return sorted_data