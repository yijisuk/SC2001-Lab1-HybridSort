import random
import pandas as pd


class DataGenerator:
    
    def __init__(self):
        self.data = []


    def base_generation(self, type: str, length: int, 
                        minimum: int, maximum: int) -> None:
    
        if type == "random":
            arr = [random.randint(minimum, maximum) for _ in range(length)]

        else:
            if length > 1:
                max_step = (maximum - minimum) / (length - 1)
                step = random.uniform(0, max_step)
            else:
                step = 0

            if type == "ascending":

                arr = [int(minimum + step * i) for i in range(length)]
                if arr[-1] > maximum:
                    arr[-1] = maximum

            elif type == "descending":

                arr = [int(maximum - step * i) for i in range(length)]
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
                type=type,
                length=length,
                minimum=minimum,
                maximum=maximum
            )
        
        return pd.DataFrame(self.data)