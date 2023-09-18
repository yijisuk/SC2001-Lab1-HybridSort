import os
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

from .data_generator import DataGenerator


class MainGenerator(DataGenerator):

    def __init__(self):
        super().__init__()


    def batch_generation(self, batch_count: int,
                         minimum: int, maximum: int) -> None:
        
        with ThreadPoolExecutor() as executor:

            futures = [executor.submit(self.generate_input_data, batch=i, minimum=minimum, maximum=maximum)
                       for i in range(batch_count)]
            
            for i, future in enumerate(tqdm(futures, desc="Generating batches", total=batch_count)):

                try:
                    future.result()
                    print(f"Completed batch {i}...")

                except Exception as e:
                    print(f"Error in batch {i}: {e}")


    def generate_input_data(self, batch: int, 
                            minimum: int, maximum: int) -> None:
        
        base_path = os.path.join("data_storage", "input_data", f"batch_{batch}")

        if not os.path.exists(base_path):
            os.makedirs(base_path)

        for i in tqdm(range(3, 7), desc=f"Processing batch {batch}"):

            data = self.generate(
                start=10**i, end=10**(i+1), step=10**3,
                minimum=minimum, maximum=maximum
            )

            file_dir = os.path.join(base_path, f"10**{i}-10**{i+1}.csv")
            data.to_csv(file_dir, index=False)
