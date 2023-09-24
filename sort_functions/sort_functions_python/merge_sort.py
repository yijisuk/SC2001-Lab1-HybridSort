def merge_sort(arr):

    if len(arr) <= 1:
        return arr, 0

    # Split the array into two halves
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Recursively sort both halves
    left_sorted, left_comparisons = merge_sort(left_half)
    right_sorted, right_comparisons = merge_sort(right_half)

    # Merge the sorted halves and get the number of comparisons done during merge
    merged, merge_comparisons = merge(left_sorted, right_sorted)

    # Return merged array and total comparisons
    total_comparisons = left_comparisons + right_comparisons + merge_comparisons
    
    return merged, total_comparisons


def merge(left, right):

    merged = []
    left_index, right_index = 0, 0
    comparisons = 0

    # Traverse both left and right arrays
    while left_index < len(left) and right_index < len(right):

        comparisons += 1

        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If left array still has elements, add them to merged list
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # If right array still has elements, add them to merged list
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged, comparisons