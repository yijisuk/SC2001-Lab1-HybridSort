#include <stdio.h>


int insertionSort(int array[], int size);


int insertionSort(int array[], int size) {

    int temp;
    int comparisons = 0;

    for (int i = 0; i < size; i++) {

        for (int j = i; j > 0; j--) {

            comparisons++;

            if (array[j] < array[j-1]) {

                temp = array[j];
                array[j] = array[j-1];
                array[j-1] = temp;

            } else { break; }
        }
    }

    return comparisons;
}