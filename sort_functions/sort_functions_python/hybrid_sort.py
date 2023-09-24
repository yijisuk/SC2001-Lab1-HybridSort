from .insertion_sort import insertion_sort
from .merge_sort import merge_sort, merge


def hybrid_sort(array: list, threshold: int) -> tuple:

    if len(array) <= 1:
        return array, 0

    # Recursively sort both halves
    if len(array) <= threshold:
        return insertion_sort(array)

    else:
        # Split the array into two halves
        middle = len(array) // 2
        left_half = array[:middle]
        right_half = array[middle:]

        left_sorted, left_comparisons = hybrid_sort(left_half, threshold)
        right_sorted, right_comparisons = hybrid_sort(right_half, threshold)

        # Merge the two halves and count the comparisons
        merged_array, merge_comparisons = merge(left_sorted, right_sorted)

        total_comparisons = left_comparisons + right_comparisons + merge_comparisons

        return (merged_array, total_comparisons)