from sort_functions.sort_functions import SortFunctions


if __name__ == "__main__":

    SF = SortFunctions()

    test_arr = [5, 1, 8, 2, 0, 3]

    insertion_sort, is_runtime = SF.sort(test_arr, "insertion", True)
    merge_sort, ms_runtime = SF.sort(test_arr, "merge", True)
    hybrid_sort, hs_runtime = SF.hybrid_sort(test_arr, 3, True)

    print(f"Insertion sort: {insertion_sort} in {is_runtime} seconds")
    print(f"Merge sort: {merge_sort} in {ms_runtime} seconds")
    print(f"Hybrid sort: {hybrid_sort} in {hs_runtime} seconds")