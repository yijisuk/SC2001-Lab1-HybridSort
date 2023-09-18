import random
import pandas as pd


class DataGenerator:
    
    def __init__(self):
        self.data = []


    def base_generation(self, length: int, 
                        minimum: int, maximum: int) -> None:
    
        arr = [random.randint(minimum, maximum) for _ in range(length)]
        
        append_row = {
            "length": length,
            "array": arr
        }
        
        self.data.append(append_row)


    def generate(self, start: int, end: int, step: int,
                 minimum: int, maximum: int) -> pd.DataFrame:

        for length in range(start, end, step):
            self.base_generation(
                length=length,
                minimum=minimum,
                maximum=maximum
            )
        
        return pd.DataFrame(self.data)