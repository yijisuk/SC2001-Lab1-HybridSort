#include <stdio.h>


int sort(int array[], int size, int threshold);
int insertionSort(int array[], int size);
int mergeSort(int array[], int size);
int merge(int leftArray[], int leftSize, int rightArray[], int rightSize, int array[]);


int sort(int array[], int size, int threshold) {

    if (size <= threshold) {
        // sort using insertion sort
        return insertionSort(array, size);
        
    } else {
        // sort using mergesort
        return mergeSort(array, size);
    }
}