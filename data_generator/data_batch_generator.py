import numpy as np
import pandas as pd

from utilities.constants import Constants


class DataBatchGenerator:

    """
    Base Generator Class for creating a single batch of data
    """

    def __init__(self, start_zero_count: int, end_zero_count: int):

        self.data = []

        self.start_zero_count = start_zero_count
        self.end_zero_count = end_zero_count

        self.C = Constants()

    def base_generation(self, sort_type: str, array_len: int,
                        minimum_val: int, maximum_val: int) -> None:
        """
        Generates a single array of given length and type, 
        with values between the given minimum and maximum.
        """

        if sort_type == "random":
            # If type is "random", generate an array of randomly ordered integers in between the given minimum and maximum
            arr = np.random.randint(
                minimum_val, maximum_val + 1, size=array_len).tolist()

        else:
            # For the cases when type is either "ascending" or "descending",

            if array_len > 1:
                # First generate a random step size between 1 and the maximum possible step size
                max_step = (maximum_val - minimum_val) / (array_len - 1)
                step = np.random.uniform(1, max_step)
            else:
                step = 0

            if sort_type == "ascending":
                # If type is "ascending", generate an array of ascending integers in between the given minimum and maximum
                start_ascending = np.random.uniform(
                    minimum_val, maximum_val - step * (array_len - 1))

                arr = (start_ascending + np.arange(array_len)
                       * step).astype(int).tolist()

                if arr[-1] > maximum_val:
                    arr[-1] = maximum_val

            elif sort_type == "descending":
                # If type is "descending", generate an array of descending integers in between the given minimum and maximum
                start_descending = np.random.uniform(
                    minimum_val + step * (array_len - 1), maximum_val)

                arr = (start_descending - np.arange(array_len)
                       * step).astype(int).tolist()

                if arr[-1] < minimum_val:
                    arr[-1] = minimum_val

        # Append the generated array to self.data.
        append_row = {
            "length": array_len,
            "array": arr
        }

        self.data.append(append_row)

    def generate(self, sort_type: str,
                 start_len: int, end_len: int, step_size_len: int,
                 minimum_val: int, maximum_val: int) -> pd.DataFrame:
        """
        Generates input data for a single batch.
        Manages the creation of a dataframe holding arrays of different lengths,
        and returns the dataframe.

        Parameters:
            type (str): Type of array to generate.
            start (int): Starting length of the array.
            end (int): Ending length of the array.
            step (int): Step size to take in between each array length.
            minimum (int): Minimum value of the array.
            maximum (int): Maximum value of the array.

        Returns:
            pd.DataFrame: Dataframe holding arrays of different lengths.
        """

        if end_len >= 10**self.end_zero_count:
            end_len += step_size_len

        # Loop through the lengths from start to end, with step size step
        for length in range(start_len, end_len, step_size_len):

            # Call the base_generation function to generate a single array,
            # The generated array will be appended to self.data.
            self.base_generation(
                sort_type=sort_type, array_len=length,
                minimum_val=minimum_val, maximum_val=maximum_val
            )

        # Convert self.data to a dataframe and return it.
        return_df = pd.DataFrame(self.data)
        self.data.clear()

        return return_df
