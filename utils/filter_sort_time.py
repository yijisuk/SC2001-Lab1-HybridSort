import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

from .constants import Constants


def filter_sort_time():

    C = Constants()


    def process_file(file_path, save_path):

        data = pd.read_csv(file_path)
        data = data[["length", "insertion_sort_time", "merge_sort_time"]]
        data.to_csv(save_path, index=False)


    with ThreadPoolExecutor() as executor:

        for i in range(0, C.batch_count):

            batch_data_path = C.TC_batch_data_path(i)

            if not os.path.exists(batch_data_path):
                os.makedirs(batch_data_path)

            files = {
                "random": [C.ID_array_data_path(batch_id=i, data_id=j, order_type="random") 
                           for j in range(C.min_id, C.max_id)],

                "ascending": [C.ID_array_data_path(batch_id=i, data_id=j, order_type="ascending") 
                              for j in range(C.min_id, C.max_id)],

                "descending": [C.ID_array_data_path(batch_id=i, data_id=j, order_type="descending") 
                               for j in range(C.min_id, C.max_id)]
            }

            save_paths_dict = {
                "random": [C.TC_array_data_path(batch_id=i, data_id=j, order_type="random") 
                           for j in range(C.min_id, C.max_id)],

                "ascending": [C.TC_array_data_path(batch_id=i, data_id=j, order_type="ascending") 
                              for j in range(C.min_id, C.max_id)],
                              
                "descending": [C.TC_array_data_path(batch_id=i, data_id=j, order_type="descending") 
                               for j in range(C.min_id, C.max_id)]
            }

            for key in ["random", "ascending", "descending"]:

                file_paths = files[key]
                save_paths = save_paths_dict[key]

                for file_path, save_path in zip(file_paths, save_paths):
                    executor.submit(process_file, file_path, save_path)