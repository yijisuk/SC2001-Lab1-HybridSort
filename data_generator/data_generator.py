import numpy as np
import pandas as pd


class DataGenerator:
    
    def __init__(self):
        self.data = []


    def base_generation(self, type: str, length: int, 
                        minimum: int, maximum: int) -> None:

        if type == "random":
            arr = np.random.randint(minimum, maximum + 1, size=length).tolist()

        else:
            if length > 1:
                max_step = (maximum - minimum) / (length - 1)
                step = np.random.uniform(1, max_step)
            else:
                step = 0

            if type == "ascending":
                start_ascending = np.random.uniform(minimum, maximum - step * (length - 1))
                arr = (start_ascending + np.arange(length) * step).astype(int).tolist()
                if arr[-1] > maximum:
                    arr[-1] = maximum

            elif type == "descending":
                start_descending = np.random.uniform(minimum + step * (length - 1), maximum)
                arr = (start_descending - np.arange(length) * step).astype(int).tolist()
                if arr[-1] < minimum:
                    arr[-1] = minimum
        
        append_row = {
            "length": length,
            "array": arr
        }
        
        self.data.append(append_row)


    def generate(self, type: str,
                 start: int, end: int, step: int,
                 minimum: int, maximum: int) -> pd.DataFrame:

        for length in range(start, end, step):

            self.base_generation(
                type=type, length=length,
                minimum=minimum, maximum=maximum
            )

        return_df = pd.DataFrame(self.data)
        self.data.clear()
        
        return return_df