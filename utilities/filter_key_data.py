import os
from tqdm import tqdm
import pandas as pd

from .constants import Constants


def filter_key_data(start_id: int, end_id: int, batch_count: int):

    C = Constants()

    def process_file(file_path, save_path):

        data = pd.read_csv(file_path)
        data = data[["length", 
                     "insertion_sort_key_comparison", "insertion_sort_time", 
                     "merge_sort_key_comparison", "merge_sort_time"]]
        
        data.to_csv(save_path, index=False)


    for i in tqdm(range(0, batch_count)):

        print(f"Filtering Key Comparison & Time Complexity for Batch {i}:")
        batch_data_path = C.TC_batch_data_path(i)

        if not os.path.exists(batch_data_path):
            os.makedirs(batch_data_path)

        paths = {
            "files": {
                "random": [C.ID_array_data_path(batch_id=i, data_id=j, order_type="random") 
                    for j in range(start_id, end_id)],

                "ascending": [C.ID_array_data_path(batch_id=i, data_id=j, order_type="ascending") 
                            for j in range(start_id, end_id)],

                "descending": [C.ID_array_data_path(batch_id=i, data_id=j, order_type="descending") 
                            for j in range(start_id, end_id)]
            },

            "save_paths": {
                "random": [C.TC_array_data_path(batch_id=i, data_id=j, order_type="random") 
                    for j in range(start_id, end_id)],

                "ascending": [C.TC_array_data_path(batch_id=i, data_id=j, order_type="ascending") 
                            for j in range(start_id, end_id)],

                "descending": [C.TC_array_data_path(batch_id=i, data_id=j, order_type="descending") 
                            for j in range(start_id, end_id)]
            }
        }

        for key in ["random", "ascending", "descending"]:

            file_paths = paths["files"][key]
            save_paths = paths["save_paths"][key]

            for file_path, save_path in zip(file_paths, save_paths):
                process_file(file_path, save_path)