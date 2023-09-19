#include <stdio.h>


void mergeSort(int array[], int size);
void merge(int leftArray[], int leftSize, int rightArray[], int rightSize, int array[]);


void mergeSort(int array[], int size) {

    if (size <= 1) { return; }

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

    mergeSort(leftArray, middle);
    mergeSort(rightArray, size-middle);

    merge(
        leftArray, middle, 
        rightArray, size-middle, 
        array);
}


void merge(int leftArray[], int leftSize, int rightArray[], int rightSize, int array[]) {

    int i = 0;
    int l = 0;
    int r = 0;

    while (l < leftSize && r < rightSize) {

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
}