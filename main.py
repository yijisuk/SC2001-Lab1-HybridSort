from sort import sort


if __name__ == "__main__":

    test_arr = [5, 1, 8, 2, 0, 3]
    test_sorted, runtime = sort(test_arr, 3, True)
    
    print(test_sorted)
    print(runtime)