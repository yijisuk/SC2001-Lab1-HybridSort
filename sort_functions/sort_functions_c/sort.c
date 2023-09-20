#include <stdio.h>


__declspec(dllexport) void sort(int array[], int size, int threshold);
__declspec(dllexport) void insertionSort(int array[], int size);
__declspec(dllexport) void mergeSort(int array[], int size);
__declspec(dllexport) void merge(int leftArray[], int leftSize, int rightArray[], int rightSize, int array[]);


__declspec(dllexport) void sort(int array[], int size, int threshold) {

    int temp;

    if (size <= threshold) {
        // sort using insertion sort
        insertionSort(array, size);
        
    } else {
        // sort using mergesort
        mergeSort(array, size);
    }
}