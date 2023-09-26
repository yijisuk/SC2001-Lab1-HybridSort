# SC2001-SCMC-Team8
**Algorithm Design & Analysis Lab 1 - Integration of Merge Sort & Insertion Sort**

## Important File Descriptions
```main.py```: Holds the demonstration code of the insertion, merge, and hybrid sort algorithms. S value is temporarily set to 3. Adjust it accordingly.

```data.py```: Python file that generates multiple batches of input data, and runs through time complexity analysis. The generated data are stored at ```./data_storage/input_data```, yet the folder in this repository is empty due to file size limitations.

```./time_complexity_analysis/time_complexity_analysis.py```: Measures the time taken for sorting the generated input dataset with varying lengths using insertion sort and merge sort.

```./sort_functions/sort_functions.py```: Connects the C shared object file with Python, making the C sorting functions executable through Python.

```./utilities/filter_key_data.py```: Organizes the array length, key comparisons count, and sorting time to a new dataframe set. The organized data are stored at ```./data_storage/time_complexity```.

```s1_observation.ipynb```: Step 1️⃣ - Initial Observation; Jupyter Notebook showing the process of searching the suitable range of S values for testing.

```s2_finding_s.ipynb```: Step 2️⃣ - Finding S; the process of finding the optimal S values through comparisons of sort time and key comparison counts between Hybrid Sort and Insertion & Merge Sorts.

```s3_mergesort_comparison.ipynb```: Step 3️⃣ - Hybrid vs Merge Sort Comparison; comparison on the sort time and key comparison counts between Hybrid Sort and Merge Sort, thus resulting in a final value for the Optimal S.

## Folder Descriptions
```data_generator/```: Holds all Python files relevant to input data generation.

```sort_functions/```: Holds all C & Python files relevant to sorting functions: insertion sort, merge sort, & hybrid sort
- ```sort_functions_c/```: Sorting functions written in C
- ```sort_functions_python/```: Sorting functions written in Python

```time_complexity_analysis/```: Holds all Python functions relevant to time complexity analysis of individual sorting functions.

```utilities/```: Holds all Python functions used for utility purposes.

## Time Complexity Analysis
The Hybrid Sort algorithm integrates both Merge and Insertion Sort. The idea is to set a small integer ```S``` as a threshold for the size of subarrays. Once the size of a subarray in a recursive call of Mergesort is less than or equal to S, the algorithm will switch to Insertion Sort, which is efficient for small-sized input.

1. Time Complexity for splitting an array of initial length $n/S\$ into half until the length $S\$ is reached. & Merging the split, sorted arrays back = $O(nlog_2(n/S))\$
2. Time Complexity for sorting $n/S\$ subarrays of length $S\$ = $O(nS)\$
3. Total Time Complexity of Hybrid Sort = $O(nlog_2(n/S) + nS)\$
