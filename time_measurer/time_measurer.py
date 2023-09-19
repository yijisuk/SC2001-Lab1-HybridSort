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
            for i in tqdm(range(0, 3)):

                print(f"Analyzing Time Complexity for Batch {i}:")
                batch_data_path = self.C.batch_data_path(i)

                # Create a list of file paths for the current batch
                files = [
                    os.path.join(batch_data_path, self.C.dataOne),
                    os.path.join(batch_data_path, self.C.dataTwo),
                    # os.path.join(batch_data_path, self.C.dataThree),
                    # os.path.join(batch_data_path, self.C.dataFour)
                ]

                # Use the executor to apply the base_measure method concurrently on all files
                results = list(executor.map(self.base_measure, files))

                # Save each processed dataframe back to its file
                for df, file_path in zip(results, files):
                    df.to_csv(file_path, index=False)


    def base_measure(self, data_path: str) -> pd.DataFrame:

        data = pd.read_csv(data_path)

        results = data.apply(self.process_row, axis=1, result_type='expand')
        data[["insertion_sorted_array", "merge_sorted_array", "insertion_sort_time", "merge_sort_time"]] = results

        return data
    

    def process_row(self, row) -> Tuple[list, list, float, float]:

        array = ast.literal_eval(row["array"])

        insertion_sorted_arr, is_runtime = self.SF.sort(
            array=array, option="insertion", return_runtime=True)

        merge_sorted_arr, ms_runtime = self.SF.sort(
            array=array, option="merge", return_runtime=True)

        return insertion_sorted_arr, merge_sorted_arr, is_runtime, ms_runtime