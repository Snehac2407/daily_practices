def move_zeros_to_end(arr):
    position = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[position], arr[i] = arr[i], arr[position]
            position += 1

    return arr

input_array = [1, 0, 2, 3, 0, 4, 0, 1]
output_array = move_zeros_to_end(input_array)
print(output_array)