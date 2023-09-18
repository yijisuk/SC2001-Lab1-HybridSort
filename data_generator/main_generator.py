import os
from tqdm import tqdm

from .data_generator import DataGenerator


class MainGenerator(DataGenerator):

    def __init__(self):
        super().__init__()


    def batch_generation(self, batch_count: int,
                         minimum: int, maximum: int) -> None:
        
        for i in range(batch_count):

            print(f"Generating batch {i}...")

            self.generate_input_data(
                batch=i,
                minimum=minimum,
                maximum=maximum
            )


    def generate_input_data(self, batch: int, 
                            minimum: int, maximum: int) -> None:

        base_path = os.path.join("data_storage", "input_data", f"batch_{batch}")

        if not os.path.exists(base_path):
            os.makedirs(base_path)

        for i in tqdm(range(3, 7)):

            data = self.generate(
                start=10**i, end=10**(i+1),
                minimum=minimum, maximum=maximum
            )

            file_dir = os.path.join(base_path, f"10**{i}-10**{i+1}.csv")
            data.to_csv(file_dir, index=False)