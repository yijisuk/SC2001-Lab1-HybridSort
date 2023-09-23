class SharedConstants:

    def __init__(self, 
                 start_zero_count: int, end_zero_count: int, 
                 start_id: int, end_id: int,
                 batch_count: int, step_size_len: int):

        self.start_zero_count = start_zero_count
        self.end_zero_count = end_zero_count
        self.start_id = start_id
        self.end_id = end_id
        self.batch_count = batch_count
        self.step_size_len = step_size_len