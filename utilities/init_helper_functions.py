class InitHelperFunctions:

    def __init__(self):
        pass

    def get_init_inputs(self):

        start_zero_count = self.get_input("Start Zero Count: ")
        end_zero_count = self.get_input("End Zero Count: ")
        batch_count = self.get_input("Batch Count: ")

        step_size_len = self.get_step_size_len(
            "Step Size for Array Length (Empty for default): ")

        return (start_zero_count, end_zero_count, batch_count, step_size_len)

    def get_input(self, prompt: str):

        while True:
            try:
                value = int(input(prompt))

                return value

            except ValueError:
                print("Please enter a valid integer.")

    def get_step_size_len(self, prompt: str):

        step_size_len = input(prompt)

        try:
            step_size_len = int(step_size_len)
        except:
            step_size_len = None

        return step_size_len
