from data_generator.main_generator import MainGenerator
from time_complexity_analysis.time_complexity_analysis import TimeComplexityAnalysis

from utilities.filter_key_data import filter_key_data
from utilities.constants import Constants
from utilities.init_helper_functions import InitHelperFunctions


if __name__ == "__main__":

    IHF = InitHelperFunctions()
    start_zero_count, end_zero_count, batch_count, step_size_len = IHF.get_init_inputs()

    # print("Generating Data...")

    # C = Constants()

    # main_generator = MainGenerator(
    #     start_zero_count=start_zero_count, end_zero_count=end_zero_count)

    # main_generator.batch_generation(
    #     batch_count=batch_count, 
    #     minimum_val=1, maximum_val=10**6-1, step_size_len=step_size_len)

    start_id, end_id = 1, end_zero_count - start_zero_count

    TCA = TimeComplexityAnalysis(
        start_id=start_id, end_id=end_id, batch_count=batch_count)
    TCA.time_complexity_analysis()

    # filter_key_data(start_id=start_id, end_id=end_id, batch_count=batch_count)