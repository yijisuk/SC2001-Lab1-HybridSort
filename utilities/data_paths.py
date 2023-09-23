import os
from itertools import chain

from .shared_constants import SharedConstants


class DataPaths:

    def __init__(self):
        pass


    def ID_batch_data_path(self, batch: int, base_path: str = "data_storage") -> str:

        return os.path.join(base_path, "input_data", f"batch_{batch}")


    def ID_array_data_path(self, batch_id: int, zero_count: int,
                           data_id: int, order_type: str,
                           base_path: str = "data_storage") -> str:

        file_path = os.path.join(
            self.ID_batch_data_path(batch_id, base_path),
            f"{self.base_file_name(data_id, zero_count, order_type)}.csv")

        return file_path


    def TC_batch_data_path(self, batch: int, base_path: str = "data_storage") -> str:

        return os.path.join(base_path, "time_complexity", f"batch_{batch}")


    def TC_array_data_path(self, batch_id: int, zero_count: int,
                           data_id: int, order_type: str,
                           base_path: str = "data_storage") -> str:

        file_path = os.path.join(
            self.TC_batch_data_path(batch_id, base_path),
            f"{self.base_file_name(data_id, zero_count, order_type)}-tc.csv")
        
        return file_path
    

    def generate_paths(self, batch_id: int, SC: SharedConstants,
                       order_type: str, paths_option: str) -> list:

        if paths_option == "ID":
            return_list = [[self.ID_array_data_path(batch_id=batch_id, zero_count=zc, 
                                            data_id=j, order_type=order_type) 
                    for j in range(SC.start_id, SC.end_id)] 
                    for zc in range(SC.start_zero_count, SC.end_zero_count)]
        
        elif paths_option == "TC":
            return_list = [[self.TC_array_data_path(batch_id=batch_id, zero_count=zc, 
                                            data_id=j, order_type=order_type) 
                    for j in range(SC.start_id, SC.end_id)] 
                    for zc in range(SC.start_zero_count, SC.end_zero_count)]
            
        return list(chain.from_iterable(return_list))


    def base_file_name(self, data_id: int, zero_count: int, order_type: str) -> str:

        return f"ID{data_id}-10p{zero_count}-10p{zero_count+1}-{order_type}"
