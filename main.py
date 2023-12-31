import random
from sort_functions.sort_functions import PythonSortFunctions, CSortFunctions


if __name__ == "__main__":

    SF = PythonSortFunctions()
    # SF = CSortFunctions()

    test_arr = [random.randint(0, 100) for _ in range(15)]

    insertion_sort, is_key_comparison, is_runtime = SF.sort(test_arr, "insertion")
    merge_sort, ms_key_comparison, ms_runtime = SF.sort(test_arr, "merge")
    hybrid_sort, hs_key_comparison, hs_runtime = SF.hybrid_sort(test_arr, 3)

    print(f"Insertion sort: {insertion_sort} with {is_key_comparison} key comparions, in {is_runtime} seconds")
    print(f"Merge sort: {merge_sort} with {ms_key_comparison} key comparions, in {ms_runtime} seconds")
    print(f"Hybrid sort: {hybrid_sort} with {hs_key_comparison} key comparions, in {hs_runtime} seconds")