import os
from tqdm import tqdm
import pandas as pd

from .shared_constants import SharedConstants
from .data_paths import DataPaths


def filter_key_data(SC: SharedConstants) -> None:

    DP = DataPaths()
    order_types = ["random", "ascending", "descending"]
    

    def process_file(file_path, save_path):

        data = pd.read_csv(file_path)
        data = data[["length", 
                     "insertion_sort_key_comparison", "insertion_sort_time", 
                     "merge_sort_key_comparison", "merge_sort_time"]]
        
        data.to_csv(save_path, index=False)


    for i in tqdm(range(0, SC.batch_count)):

        print(f"Filtering Key Comparison & Time Complexity for Batch {i}:")
        batch_data_path = DP.TC_batch_data_path(i)

        if not os.path.exists(batch_data_path):
            os.makedirs(batch_data_path)

        file_paths_dict = {
            order: DP.generate_paths(
                batch_id=i, SC=SC, 
                order_type=order, paths_option="ID"
            ) 
            for order in order_types
        }

        save_paths_dict = {
            order: DP.generate_paths(
                batch_id=i, SC=SC, 
                order_type=order, paths_option="TC"
            ) 
            for order in order_types
        }


        for key in ["random", "ascending", "descending"]:

            file_paths = file_paths_dict[key]
            save_paths = save_paths_dict[key]

            for file_path, save_path in zip(file_paths, save_paths):
                process_file(file_path, save_path)