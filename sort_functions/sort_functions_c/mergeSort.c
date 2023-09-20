#include <stdio.h>


int mergeSort(int array[], int size);
int merge(int leftArray[], int leftSize, int rightArray[], int rightSize, int array[]);


int mergeSort(int array[], int size) {

    if (size <= 1) { return 0; }

    int middle = size / 2;
    int leftArray[middle];
    int rightArray[size - middle];

    int i = 0;
    int j = 0;

    for (; i < size; i++) {

        if (i < middle) {
            leftArray[i]  = array[i];
        } else {
            rightArray[j] = array[i];
            j++;
        }
    }

    int leftComparisons = mergeSort(leftArray, middle);
    int rightComparisons = mergeSort(rightArray, size-middle);

    int mergeComparisons = merge(leftArray, middle, rightArray, size-middle, array);

    return leftComparisons + rightComparisons + mergeComparisons;
}


int merge(int leftArray[], int leftSize, int rightArray[], int rightSize, int array[]) {

    int i = 0;
    int l = 0;
    int r = 0;
    int comparisons = 0;

    while (l < leftSize && r < rightSize) {

        comparisons++;

        if (leftArray[l] < rightArray[r]) {
            array[i] = leftArray[l];
            i++;
            l++;
        } else {
            array[i] = rightArray[r];
            i++;
            r++;
        }
    }

    while (l < leftSize) {
        array[i] = leftArray[l];
        i++;
        l++;
    }

    while (r < rightSize) {
        array[i] = rightArray[r];
        i++;
        r++;
    }

    return comparisons;
}