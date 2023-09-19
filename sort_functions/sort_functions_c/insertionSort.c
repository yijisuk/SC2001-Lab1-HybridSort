#include <stdio.h>


void insertionSort(int array[], int size);


void insertionSort(int array[], int size) {

    int temp;

    for (int i = 0; i < size; i++) {

        for (int j = i; j > 0; j--) {

            if (array[j] < array[j-1]) {

                temp = array[j];
                array[j] = array[j-1];
                array[j-1] = temp;

            } else { break; }
        }
    }
}