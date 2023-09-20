from data_generator.main_generator import MainGenerator
from time_complexity_analysis.time_complexity_analysis import TimeComplexityAnalysis
from utils.filter_key_data import filter_key_data


if __name__ == "__main__":
    
    MainGenerator().batch_generation(
        batch_count=3, minimum=1, maximum=10**6-1)
    
    TCA = TimeComplexityAnalysis()
    TCA.time_complexity_analysis()
    filter_key_data()