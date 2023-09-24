#include <stdio.h>
#include <stdlib.h>


int hybridSort(int array[], int size, int threshold);
int insertionSort(int array[], int size);
int merge(int leftArray[], int leftSize, int rightArray[], int rightSize, int array[]);


int hybridSort(int array[], int size, int threshold) {
    
    if (size <= 1) {
        return 0;  // No comparisons needed for array of size 1
    }

    if (size <= threshold) {
        insertionSort(array, size);
        // In real world, we might count comparisons in insertionSort too
        return 0;
    }

    int middle = size / 2;
    int leftSize = middle;
    int rightSize = size - middle;

    // Dynamically allocate memory for left and right arrays
    int* leftArray = (int*)malloc(leftSize * sizeof(int));
    int* rightArray = (int*)malloc(rightSize * sizeof(int));

    for (int i = 0; i < leftSize; i++) {
        leftArray[i] = array[i];
    }

    for (int i = 0; i < rightSize; i++) {
        rightArray[i] = array[leftSize + i];
    }

    int leftComparisons = hybridSort(leftArray, leftSize, threshold);
    int rightComparisons = hybridSort(rightArray, rightSize, threshold);
    int mergeComparisons = merge(leftArray, leftSize, rightArray, rightSize, array);

    free(leftArray);
    free(rightArray);

    return leftComparisons + rightComparisons + mergeComparisons;
}