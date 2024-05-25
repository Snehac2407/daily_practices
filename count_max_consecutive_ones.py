def count_max_consecutive_ones(array):
    max_count = 0
    current_count = 0
    for i in array:
        if i == 1:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
    return max_count
array = [1, 1, 0, 1, 1, 1]
max_consecutive_ones = count_max_consecutive_ones(array)
print(max_consecutive_ones) 
