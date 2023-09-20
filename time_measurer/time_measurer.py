import os
import ast
from tqdm import tqdm
import pandas as pd
from typing import Tuple
from concurrent.futures import ThreadPoolExecutor

from sort_functions.sort_functions import SortFunctions
from utils.constants import Constants


class TimeMeasurer:

    def __init__(self):

        self.SF = SortFunctions()
        self.C = Constants()


    def time_measure(self):

        with ThreadPoolExecutor() as executor:

            for i in tqdm(range(0, self.C.batch_count)):

                print(f"Analyzing Time Complexity for Batch {i}:")

                # Create a list of file paths for the current batch
                files = {
                    "random": [self.C.ID_array_data_path(batch_id=i, data_id=j, order_type="random") 
                               for j in range(self.C.min_id, self.C.max_id - 1)],

                    # "ascending": [self.C.ID_array_data_path(batch_id=i, data_id=j, order_type="ascending") 
                    #               for j in range(self.C.min_id, self.C.max_id)],

                    # "descending": [self.C.ID_array_data_path(batch_id=i, data_id=j, order_type="descending") 
                    #                for j in range(self.C.min_id, self.C.max_id)]
                }

                # Create a list of all tasks
                tasks = [(file_path, key) for key in files.keys() for file_path in files[key]]

                # Use the executor to apply the base_measure method concurrently on all tasks
                for (file_path, key), df in zip(tasks, executor.map(lambda task: self.base_measure(task[0]), tasks)):
                    df.to_csv(file_path, index=False)


    def base_measure(self, data_path: str) -> pd.DataFrame:

        data = pd.read_csv(data_path)

        results = data.apply(self.process_row, axis=1, result_type='expand')
        print(results)

        data[["insertion_sorted_array", "merge_sorted_array",
              "insertion_sort_time", "merge_sort_time"]] = results

        return data

    def process_row(self, row) -> Tuple[list, list, float, float]:

        array = ast.literal_eval(row["array"])

        insertion_sorted_arr, is_runtime = self.SF.sort(
            array=array, option="insertion", return_runtime=True)

        merge_sorted_arr, ms_runtime = self.SF.sort(
            array=array, option="merge", return_runtime=True)
        
        processed_row = [insertion_sorted_arr, merge_sorted_arr, is_runtime, ms_runtime]

        return processed_row
