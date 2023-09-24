import os
import pandas as pd
import glob
from typing import Union, Tuple

from utilities.data_paths import DataPaths


class VisHelperFunctions:

    def __init__(self, batch_count: int):

        self.batch_count = batch_count
        self.DP = DataPaths()


    def get_data(self, data_range_folder: str, data_type: str,
                 batch_id: int, data_id: int, 
                 order_type: str) -> pd.DataFrame:
        
        base_data_path = self.set_base_data_path(data_range_folder=data_range_folder,
                                                  data_type=data_type, batch_id=batch_id)

        data_path = self.search_data_path(base_path=base_data_path, data_id=data_id, order_type=order_type)
        data = pd.read_csv(os.path.join(base_data_path, data_path))

        return data


    def search_data_path(self, base_path: str, data_type: str,
                         data_id: int, order_type: str) -> str:


        def check_validity(f: str, data_type: str, 
                           data_id: int, order_type: str) -> bool:
            
            if data_type == "ID":
                return (f.startswith(f"ID{data_id}-") and f.endswith(f"-{order_type}.csv"))
            elif data_type == "TC":
                return (f.startswith(f"TC{data_id}-") and f.endswith(f"-{order_type}-tc.csv"))


        for f in os.listdir(base_path):
            if os.path.splitext(f)[1] == '.csv' and check_validity(f, data_type, data_id, order_type):
                return f

        return None
    

    def merge_all_batches(self, data_range_folder: str,
                          data_type: str,
                          split: bool = False) -> Union[pd.DataFrame, Tuple[pd.DataFrame, pd.DataFrame]]:

        def get_data_from_batch(batch_id: int) -> pd.DataFrame:

            return self.merge_data(data_range_folder=data_range_folder,
                                   data_type=data_type, batch_id=batch_id)

        merged_df = [get_data_from_batch(batch_id) for batch_id in range(self.batch_count)]
        merged_df = pd.concat(merged_df, ignore_index=True)

        if split == False:
            return merged_df
        
        if data_type == "TC" and split == True:
            insertion_sort = merged_df[["length", "insertion_sort_key_comparison", 
                                        "insertion_sort_time", "order_type"]]
            merge_sort = merged_df[["length", "merge_sort_key_comparison", 
                                    "merge_sort_time", "order_type"]]
        
            return (insertion_sort, merge_sort)
    

    def merge_data(self, data_range_folder: str, 
                   data_type: str, batch_id: int,
                   split: bool = False) -> Union[pd.DataFrame, Tuple[pd.DataFrame, pd.DataFrame]]:
        
        base_data_path = self.set_base_data_path(data_range_folder=data_range_folder,
                                                 data_type=data_type, batch_id=batch_id)

        csv_files = glob.glob(base_data_path + "/*.csv")


        def columns_preprocessing(filename: str) -> pd.DataFrame:

            df = pd.read_csv(filename)

            if data_type == "ID":
                df["order_type"] = filename.split("-")[-1].split(".")[0]
            elif data_type == "TC":
                df["order_type"] = filename.split("-")[-2]

            return df
        
        
        dfs = [columns_preprocessing(file) for file in csv_files]

        merged_df = pd.concat(dfs, ignore_index=True)

        if split == False:
            return merged_df

        if data_type == "TC" and split == True:
            insertion_sort = merged_df[["length", "insertion_sort_key_comparison", 
                                        "insertion_sort_time", "order_type"]]
            merge_sort = merged_df[["length", "merge_sort_key_comparison", 
                                    "merge_sort_time", "order_type"]]
        
            return (insertion_sort, merge_sort)
    

    def set_base_data_path(self, data_range_folder: str, 
                           data_type: str, batch_id: int) -> str:

        base_path = os.path.join("data_storage", data_range_folder)

        if data_type == "ID":
            batch_data_path = self.DP.ID_batch_data_path(batch_id=batch_id, base_path=base_path)

        elif data_type == "TC":
            batch_data_path = self.DP.TC_batch_data_path(batch_id=batch_id, base_path=base_path)

        return batch_data_path