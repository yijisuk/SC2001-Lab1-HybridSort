import os


class Constants:

    def __init__(self):

        self.dataOne = "10**3-10**4.csv"
        self.dataTwo = "10**4-10**5.csv"
        self.dataThree = "10**5-10**6.csv"
        self.dataFour = "10**6-10**7.csv"


    def batch_data_path(self, batch: int):
        return os.path.join("data_storage", "input_data", f"batch_{batch}")