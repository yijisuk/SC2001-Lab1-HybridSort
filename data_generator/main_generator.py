import os
from tqdm import tqdm

from .data_batch_generator import DataBatchGenerator
from utils.constants import Constants


class MainGenerator(DataBatchGenerator):

    """
    Main Generator Class for creating multiple batches of data.
    """

    def __init__(self):

        super().__init__()
        self.C = Constants()


    def batch_generation(self, batch_count: int,
                         minimum: int, maximum: int, step: any) -> None:
        
        """
        Generates multiple batches of data.

        Parameters:
            batch_count (int): Number of batches to generate.
            minimum (int): Minimum value of the array.
            maximum (int): Maximum value of the array.
            step (any): Step size to take in between each array length.

        Returns:
            None
        """

        # Loop through the number of batches
        for i in tqdm(range(batch_count), desc="Generating batches"):

            try:
                self.generate_input_data(
                    batch=i, minimum=minimum, maximum=maximum, step=step)
                print(f"Completed batch {i}...")

            except Exception as e:
                print(f"Error in batch {i}: {e}")


    def generate_input_data(self, batch: int,
                            minimum: int, maximum: int, step: any) -> None:
        
        """
        Generates input data for a single batch.
        Manages the creation of the save directory, 
        dataset creation, and saving of the dataset.
        
        Parameters:
            batch (int): Batch number.
            minimum (int): Minimum value of the array.
            maximum (int): Maximum value of the array.
            step (any): Step size to take in between each array length.

        Returns:
            None
        """

        base_path = self.C.ID_batch_data_path(batch)

        if not os.path.exists(base_path):
            os.makedirs(base_path)


        # Base function for processing arrays of length from 10**i to 10**(i+1)
        def process_type(i, type, step=None):

            # If step is not specified, set step to 10**i
            if step == None:
                step = 10**i

            # Calls the .generate() function from the DataBatchGenerator class
            data = self.generate(
                type=type,
                start=10**i, end=10**(i+1), step=step,
                minimum=minimum, maximum=maximum
            )

            # Save the dataset to a csv file
            file_dir = self.C.ID_array_data_path(
                batch_id=batch, data_id=i-2, order_type=type)
            data.to_csv(file_dir, index=False)


        # Process random, ascending, and descending arrays for each length in between min_zero_count and max_zero_count
        for i in tqdm(range(self.C.min_zero_count, self.C.max_zero_count), desc=f"Processing batch {batch}"):

            for type in ["random", "ascending", "descending"]:
                process_type(i, type, step)