import os

from .shared_constants import SharedConstants


class DataPaths:

    def __init__(self):
        pass


    def ID_batch_data_path(self, batch_id: int, base_path: str = "data_storage") -> str:

        return os.path.join(base_path, "input_data", f"batch_{batch_id}")


    def ID_array_data_path(self, batch_id: int, zero_count: int,
                           data_id: int, order_type: str,
                           base_path: str = "data_storage") -> str:

        file_path = os.path.join(
            self.ID_batch_data_path(batch_id, base_path),
            f"{self.base_file_name(data_id, zero_count, order_type)}.csv")

        return file_path


    def TC_batch_data_path(self, batch_id: int, base_path: str = "data_storage") -> str:

        return os.path.join(base_path, "time_complexity", f"batch_{batch_id}")


    def TC_array_data_path(self, batch_id: int, zero_count: int,
                           data_id: int, order_type: str,
                           base_path: str = "data_storage") -> str:

        file_path = os.path.join(
            self.TC_batch_data_path(batch_id, base_path),
            f"{self.base_file_name(data_id, zero_count, order_type)}-tc.csv")
        
        return file_path
    

    def generate_paths(self, batch_id: int, SC: SharedConstants,
                       order_type: str, paths_option: str) -> list:

        return_list = self.aggregate_batch_data_paths(
            batch_id=batch_id, SC=SC, 
            order_type=order_type, paths_option=paths_option
        )
            
        return return_list
    

    def aggregate_batch_data_paths(self, 
                                   batch_id: int, SC: SharedConstants,
                                   order_type: str, paths_option: str) -> list:

        data_id = 1
        return_list = []

        if paths_option == "ID":
            for zc in range(SC.start_zero_count, SC.end_zero_count):

                return_list.append(self.ID_array_data_path(
                    batch_id=batch_id, zero_count=zc, 
                    data_id=data_id, order_type=order_type))
                
                data_id += 1

        elif paths_option == "TC":
            for zc in range(SC.start_zero_count, SC.end_zero_count):

                return_list.append(self.TC_array_data_path(
                    batch_id=batch_id, zero_count=zc, 
                    data_id=data_id, order_type=order_type))
                
                data_id += 1

        return return_list


    def base_file_name(self, data_id: int, zero_count: int, order_type: str) -> str:

        return f"ID{data_id}-10p{zero_count}-10p{zero_count+1}-{order_type}"