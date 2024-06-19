# def no_appers_once(array):
#     unique_no=0
#     for i in array:
#         if i == unique_no:
#             pass
#         else:
#             return unique_no
# arr=array=[12,23,32,12,32]
# print(no_appers_once(arr))


def find_unique_number(arr):
    unique_number = 0
    for num in arr:
        unique_number ^= num
    return unique_number

# Example usage:
arr = [2, 3, 2, 4, 4, 5, 3]
print(find_unique_number(arr))  # Output: 5
