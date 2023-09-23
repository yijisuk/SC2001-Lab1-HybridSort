import numpy as np
import pandas as pd


class DataBatchGenerator:

    """
    Base Generator Class for creating a single batch of data
    """

    def __init__(self):
        self.data = []


    def base_generation(self, type: str, length: int,
                        minimum: int, maximum: int) -> None:
        
        """
        Generates a single array of given length and type, 
        with values between the given minimum and maximum.
        """

        if type == "random":
            # If type is "random", generate an array of randomly ordered integers in between the given minimum and maximum
            arr = np.random.randint(minimum, maximum + 1, size=length).tolist()

        else:
            # For the cases when type is either "ascending" or "descending",

            if length > 1:
                # First generate a random step size between 1 and the maximum possible step size
                max_step = (maximum - minimum) / (length - 1)
                step = np.random.uniform(1, max_step)
            else:
                step = 0

            if type == "ascending":
                # If type is "ascending", generate an array of ascending integers in between the given minimum and maximum
                start_ascending = np.random.uniform(
                    minimum, maximum - step * (length - 1))
                
                arr = (start_ascending + np.arange(length)
                       * step).astype(int).tolist()
                
                if arr[-1] > maximum:
                    arr[-1] = maximum

            elif type == "descending":
                # If type is "descending", generate an array of descending integers in between the given minimum and maximum
                start_descending = np.random.uniform(
                    minimum + step * (length - 1), maximum)
                
                arr = (start_descending - np.arange(length)
                       * step).astype(int).tolist()
                
                if arr[-1] < minimum:
                    arr[-1] = minimum

        # Append the generated array to self.data.
        append_row = {
            "length": length,
            "array": arr
        }

        self.data.append(append_row)


    def generate(self, type: str,
                 start: int, end: int, step: int,
                 minimum: int, maximum: int) -> pd.DataFrame:
        
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

        # Loop through the lengths from start to end, with step size step
        for length in range(start, end, step):

            # Call the base_generation function to generate a single array,
            # The generated array will be appended to self.data.
            self.base_generation(
                type=type, length=length,
                minimum=minimum, maximum=maximum
            )

        # Convert self.data to a dataframe and return it.
        return_df = pd.DataFrame(self.data)
        self.data.clear()

        return return_df
