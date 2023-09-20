import os
import platform
import time 
import ctypes
from typing import List


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
        self.insertion_sort_clibary.insertionSort.restype = ctypes.c_int

        self.merge_sort_clibrary.mergeSort.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)
        self.merge_sort_clibrary.mergeSort.restype = ctypes.c_int

        self.hybrid_sort_clibrary.sort.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int)
        self.hybrid_sort_clibrary.sort.restype = ctypes.c_int


    def sort(self, array: List[int], option: str) -> list:

        start_time = time.time()

        arr = (ctypes.c_int * len(array))(*array)
        size = len(array)


        if option == "insertion":

            key_comparisons = self.insertion_sort_clibary.insertionSort(arr, size)
            sorted_data = list(arr)

        elif option == "merge":

            key_comparisons = self.merge_sort_clibrary.mergeSort(arr, size)
            sorted_data = list(arr)


        end_time = time.time()
        elapsed_time = end_time - start_time

        return [sorted_data, key_comparisons, elapsed_time]


    def hybrid_sort(self, array: List[int], threshold: int) -> dict:

        start_time = time.time()

        arr = (ctypes.c_int * len(array))(*array)
        size = len(array)

        key_comparisons = self.hybrid_sort_clibrary.sort(arr, size, threshold)
        sorted_data = list(arr)

        end_time = time.time()
        elapsed_time = end_time - start_time

        return [sorted_data, key_comparisons, elapsed_time]