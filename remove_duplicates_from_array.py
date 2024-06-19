def remove_duplicates(sorted_array):
    if not sorted_array:
        return []

    ptr = [sorted_array[0]]

    for i in range(1, len(sorted_array)):
        if sorted_array[i] != sorted_array[i-1]:
            ptr.append(sorted_array[i])

    return ptr

# Example usage:
input_array = [1, 1, 2, 2, 3, 3, 3]
output_array = remove_duplicates(input_array)
print(output_array)  
