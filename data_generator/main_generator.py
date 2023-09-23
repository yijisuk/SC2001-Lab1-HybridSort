import os
from tqdm import tqdm

from .data_batch_generator import DataBatchGenerator
from utilities.shared_constants import SharedConstants
from utilities.data_paths import DataPaths


class MainGenerator(DataBatchGenerator):

    """
    Main Generator Class for creating multiple batches of data.
    """

    def __init__(self, SC: SharedConstants):

        super().__init__(SC=SC)
        self.DP = DataPaths()


    def batch_generation(self, minimum_val: int, maximum_val: int) -> None:
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
        for i in tqdm(range(self.SC.batch_count), desc="Generating batches"):

            try:
                self.generate_input_data(
                    batch_count=i, 
                    minimum_val=minimum_val, maximum_val=maximum_val, 
                    step_size_len=self.SC.step_size_len)
                
                print(f"Completed batch {i}...")

            except Exception as e:
                print(f"Error in batch {i}: {e}")


    def generate_input_data(self, batch_count: int,
                            minimum_val: int, maximum_val: int,
                            step_size_len: any) -> None:
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

        base_path = self.DP.ID_batch_data_path(batch_count)

        if not os.path.exists(base_path):
            os.makedirs(base_path)

        # Base function for processing arrays of length from 10**i to 10**(i+1)

        def process_type(i: int, id_val: int,
                         sort_type: str, step_size: any = None) -> None:

            # If step is not specified, set step to 10**i
            if step_size == None:
                step_size = 10**i

            # Calls the .generate() function from the DataBatchGenerator class
            data = self.generate(
                sort_type=sort_type,
                start_len=10**i, end_len=10**(i+1), step_size_len=step_size,
                minimum_val=minimum_val, maximum_val=maximum_val
            )

            # Save the dataset to a csv file
            file_dir = self.DP.ID_array_data_path(
                batch_id=batch_count, zero_count=i,
                data_id=id_val, order_type=sort_type)
            
            data.to_csv(file_dir, index=False)

        # Process random, ascending, and descending arrays for each length in between min_zero_count and max_zero_count
        id_val = 1
        for i in tqdm(range(self.SC.start_zero_count, self.SC.end_zero_count), desc=f"Processing batch {batch_count}"):

            for type in ["random", "ascending", "descending"]:
                process_type(i, id_val, type, step_size_len)
            
            id_val += 1