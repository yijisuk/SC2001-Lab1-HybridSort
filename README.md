# SC2001-SCMC-Team8
**Algorithm Design & Analysis**

## Important File Descriptions
```main.py```: Currently holds the demonstration of the hybrid sort algorithm. S value is temporarily set to 3.

```data.py```: Python file that generates multiple batches of input data. The generated data are stored at ```./data_storage/input_data```, yet it's not on this repository due to file size limitation.

```./time_complexity_analysis/time_complexity_analysis.py```: Measures the time taken for sorting the generated input dataset with varying lengths using insertion sort and merge sort. Later the retrieved values will be used to find S value of the hybrid sort algorithm.

```./sort_functions/sort_functions.py```: Connects the C shared object file with Python, making the C sorting functions executable through Python.

```./utils/filter_key_data.py```: Organizes the array length, key comparisons count, and sorting time to a new dataframe. The organized data are stored at ```./data_storage/time_complexity```.

```input_data_vis.ipynb```: Jupyter Notebook file for visualizing the generated input data

## Folder Descriptions
```data_generator```: Holds all Python files relevant to input data generation.

```sort_functions```: Holds all Python & C files relevant to sorting functions
- ```sort_functions_c```: Sorting functions written in C: insertion sort, merge sort, & hybrid sort

```time_measurer```: Holds all Python files relevant to sorting time complexity analysis.

```utils```: Holds all utility-related Python files.
