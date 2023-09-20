import os
from tqdm import tqdm

from .data_generator import DataGenerator
from utils.constants import Constants


class MainGenerator(DataGenerator):

    def __init__(self):

        super().__init__()
        self.C = Constants()


    def batch_generation(self, batch_count: int,
                         minimum: int, maximum: int) -> None:
        
        for i in tqdm(range(batch_count), desc="Generating batches"):

            try:
                self.generate_input_data(batch=i, minimum=minimum, maximum=maximum)
                print(f"Completed batch {i}...")

            except Exception as e:
                print(f"Error in batch {i}: {e}")


    def generate_input_data(self, batch: int, 
                            minimum: int, maximum: int) -> None:
    
        base_path = self.C.ID_batch_data_path(batch)

        if not os.path.exists(base_path):
            os.makedirs(base_path)


        def process_type(i, type):

            data = self.generate(
                type=type,
                start=10**i, end=10**(i+1), step=10**i,
                minimum=minimum, maximum=maximum
            )

            file_dir = self.C.ID_array_data_path(batch_id=batch, data_id=i-2, order_type=type)
            data.to_csv(file_dir, index=False)


        for i in tqdm(range(self.C.min_zero_count, self.C.max_zero_count), desc=f"Processing batch {batch}"):

            for type in ["random", "ascending", "descending"]:
                process_type(i, type)