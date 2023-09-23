from data_generator.main_generator import MainGenerator
from time_complexity_analysis.time_complexity_analysis import TimeComplexityAnalysis

from utilities.filter_key_data import filter_key_data
from utilities.shared_constants import SharedConstants
from utilities.data_paths import DataPaths
from utilities.init_helper_functions import InitHelperFunctions


if __name__ == "__main__":

    IHF = InitHelperFunctions()
    start_zero_count, end_zero_count, batch_count, step_size_len = IHF.get_init_inputs()
    start_id = 1
    end_id = start_id + (end_zero_count - start_zero_count)

    SC = SharedConstants(
        start_zero_count=start_zero_count, end_zero_count=end_zero_count,
        start_id=start_id, end_id=end_id,
        batch_count=batch_count, step_size_len=step_size_len
    )

    print("Generating Data...")

    # main_generator = MainGenerator(SC=SC)
    # main_generator.batch_generation(
    #     minimum_val=1, maximum_val=10**6-1)
    

    TCA = TimeComplexityAnalysis(SC=SC)
    TCA.time_complexity_analysis()

    filter_key_data(SC=SC)