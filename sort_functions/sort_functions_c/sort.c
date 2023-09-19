#include <stdio.h>


void sort(int array[], int size, int threshold);
void insertionSort(int array[], int size);
void mergeSort(int array[], int size);
void merge(int leftArray[], int leftSize, int rightArray[], int rightSize, int array[]);


void sort(int array[], int size, int threshold) {

    int temp;

    if (size <= threshold) {
        // sort using insertion sort
        insertionSort(array, size);
        
    } else {
        // sort using mergesort
        mergeSort(array, size);
    }
}