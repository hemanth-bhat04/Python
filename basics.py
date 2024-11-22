import time

def count_data_types(sample_list):
    type_count = {}
    for item in sample_list:
        item_type = type(item).__name__  
        if item_type in type_count:
            type_count[item_type] += 1
        else:
            type_count[item_type] = 1
    return type_count


sample_list = [1, 2, "A", "3", True]
start_time = time.time()
result = count_data_types(sample_list)
end_time = time.time()
print("Result:", result)
print("Execution time:", end_time - start_time)


