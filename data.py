from data_generator.main_generator import MainGenerator


if __name__ == "__main__":
    
    MainGenerator().batch_generation(
        batch_count=3, minimum=1, maximum=10**6-1)