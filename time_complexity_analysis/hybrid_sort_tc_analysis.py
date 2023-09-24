import pandas as pd
import ast
from typing import Tuple

from sort_functions.sort_functions import PythonSortFunctions


class HybridSortTCA:

    def __init__(self, S: int):

        self.SF = PythonSortFunctions()
        self.S = S


    def hybrid_sort_time_complexity_analysis(self, data: pd.DataFrame) -> None:

        results = data.apply(self.process_row, axis=1, result_type='expand')

        data[["hybrid_sorted_array", "hybrid_sort_key_comparison", 
              "hybrid_sort_time"]] = results
        
        return data


    def process_row(self, row) -> Tuple[list, int, float]:

        array = ast.literal_eval(row["array"])

        hybrid_sorted_arr, hs_key_comparison, hs_runtime = self.SF.hybrid_sort(array, self.S)

        processed_row = [hybrid_sorted_arr, hs_key_comparison, hs_runtime]

        return processed_row