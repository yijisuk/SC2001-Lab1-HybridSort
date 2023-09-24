def insertion_sort(array):

    key_comparisons = 0

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            key_comparisons += 1
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array, key_comparisons