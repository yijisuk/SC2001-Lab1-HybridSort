import ast
from tqdm import tqdm
import pandas as pd
from typing import Tuple

from sort_functions.sort_functions import PythonSortFunctions
from utilities.shared_constants import SharedConstants
from utilities.data_paths import DataPaths


class TimeComplexityAnalysis:

    def __init__(self, SC: SharedConstants):

        self.SC = SC
        self.SF = PythonSortFunctions()
        self.DP = DataPaths()


    def time_complexity_analysis(self) -> None:

        order_types = ["random", "ascending", "descending"]

        for i in tqdm(range(0, self.SC.batch_count)):

            print(f"Analyzing Time Complexity for Batch {i}:")

            # Create a list of file paths for the current batch
            files = {
                order: self.DP.generate_paths(
                    batch_id=i, SC=self.SC, 
                    order_type=order, paths_option="ID"
                ) 
                for order in order_types
            }

            # Create a list of all tasks
            tasks = [(file_path, key) for key in files.keys() for file_path in files[key]]

            # Directly call the base_measure method for all tasks
            for file_path, _ in tasks:

                df = self.base_analysis(file_path)
                df.to_csv(file_path, index=False)


    def base_analysis(self, data_path: str) -> pd.DataFrame:

        data = pd.read_csv(data_path)

        # temp line
        data = data[data["length"] <= 2000]

        results = data.apply(self.process_row, axis=1, result_type='expand')

        data[["insertion_sorted_array", "merge_sorted_array",
              "insertion_sort_key_comparison", "insertion_sort_time", 
              "merge_sort_key_comparison", "merge_sort_time"]] = results

        return data


    def process_row(self, row) -> Tuple[list, list, int, float, int, float]:

        array = ast.literal_eval(row["array"])

        insertion_sorted_arr, is_key_comparison, is_runtime = self.SF.sort(
            array=array, option="insertion")

        merge_sorted_arr, ms_key_comparison, ms_runtime = self.SF.sort(
            array=array, option="merge")
        
        processed_row = [insertion_sorted_arr, merge_sorted_arr, 
                         is_key_comparison, is_runtime, 
                         ms_key_comparison, ms_runtime]

        return processed_row