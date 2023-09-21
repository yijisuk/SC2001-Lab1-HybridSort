import os


class Constants:

    def __init__(self):

        self.min_zero_count = 3
        self.max_zero_count = 4
        
        self.min_id = 1
        self.max_id = self.max_zero_count - self.min_zero_count
        self.batch_count = 3


    def ID_batch_data_path(self, batch: int) -> str:

        return os.path.join("data_storage", "input_data", f"batch_{batch}")


    def ID_array_data_path(self, batch_id: int, data_id: int, order_type: str) -> str:

        zero_count = 2 + data_id
        return os.path.join(
            self.ID_batch_data_path(batch_id), 
            f"{self.base_file_name(data_id, zero_count, order_type)}.csv")


    def TC_batch_data_path(self, batch: int) -> str:

        return os.path.join("data_storage", "time_complexity", f"batch_{batch}")
    

    def TC_array_data_path(self, batch_id: int, data_id: int, order_type: str) -> str:

        zero_count = 2 + data_id
        return os.path.join(
            self.TC_batch_data_path(batch_id), 
            f"{self.base_file_name(data_id, zero_count, order_type)}-tc.csv")
    

    def base_file_name(self, data_id: int, zero_count: int, order_type: str) -> str:

        return f"ID{data_id}-10p{zero_count}-10p{zero_count+1}-{order_type}"