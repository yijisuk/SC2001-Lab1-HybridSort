import os
from tqdm import tqdm
import pandas as pd

from .constants import Constants


def filter_key_data():

    C = Constants()
    max_range = C.min_id + 2


    def process_file(file_path, save_path):

        data = pd.read_csv(file_path)
        data = data[["length", 
                     "insertion_sort_key_comparison", "insertion_sort_time", 
                     "merge_sort_key_comparison", "merge_sort_time"]]
        
        data.to_csv(save_path, index=False)


    for i in tqdm(range(0, C.batch_count)):

        print(f"Filtering Key Comparison & Time Complexity for Batch {i}:")
        batch_data_path = C.TC_batch_data_path(i)

        if not os.path.exists(batch_data_path):
            os.makedirs(batch_data_path)

        files = {
            "random": [C.ID_array_data_path(batch_id=i, data_id=j, order_type="random") 
                    for j in range(C.min_id, max_range)],

            "ascending": [C.ID_array_data_path(batch_id=i, data_id=j, order_type="ascending") 
                        for j in range(C.min_id, max_range)],

            "descending": [C.ID_array_data_path(batch_id=i, data_id=j, order_type="descending") 
                        for j in range(C.min_id, max_range)]
        }

        save_paths_dict = {
            "random": [C.TC_array_data_path(batch_id=i, data_id=j, order_type="random") 
                    for j in range(C.min_id, max_range)],

            "ascending": [C.TC_array_data_path(batch_id=i, data_id=j, order_type="ascending") 
                        for j in range(C.min_id, max_range)],

            "descending": [C.TC_array_data_path(batch_id=i, data_id=j, order_type="descending") 
                        for j in range(C.min_id, max_range)]
        }

        for key in ["random", "ascending", "descending"]:

            file_paths = files[key]
            save_paths = save_paths_dict[key]

            for file_path, save_path in zip(file_paths, save_paths):
                process_file(file_path, save_path)