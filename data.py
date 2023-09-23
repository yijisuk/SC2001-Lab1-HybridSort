from data_generator.main_generator import MainGenerator
from time_complexity_analysis.time_complexity_analysis import TimeComplexityAnalysis

from utilities.filter_key_data import filter_key_data
from utilities.constants import Constants
from utilities.init_helper_functions import InitHelperFunctions


if __name__ == "__main__":

    IHF = InitHelperFunctions()
    start_zero_count, end_zero_count, batch_count, step_size_len = IHF.get_init_inputs()

    print("Generating Data...")

    C = Constants()

    MainGenerator().batch_generation(
        batch_count=batch_count, 
        minimum_val=1, maximum_val=10**6-1, step_size_len=step_size_len)

    start_id, end_id = C.min_id, C.max_id

    TCA = TimeComplexityAnalysis()
    TCA.time_complexity_analysis(start_id=start_id, end_id=end_id)
    filter_key_data(start_id=start_id, end_id=end_id)