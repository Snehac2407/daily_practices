# 1. find the largest elementin array 
def  largest_element(arr):
    if not arr:
        return None
    largest=arr[0]
    for num in arr:
        if num >largest:
            largest=num
    return largest
array=[24,32,21,12,23]
print(largest_element(array))

# 2. to check weathwer the array is sorted or not:-
def sorted(arr):
    for num in range (len(arr)-1):
        if arr[num]>arr[num+1]:
            return False
        return True
array=[12,32,34,54,56,58]  
print(sorted(array))  



# 3. find the largest and the second largest element of a array:-
def find_largest_and_second_largest(arr):
    if len(arr) < 2:
        return None
    
    largest = second_largest = float('-inf')  #Initialize the largest and second largest
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    # If second_largest is still float('-inf'), it means no second largest was found
    if second_largest == float('-inf'):
        second_largest = None

    return largest, second_largest

# Example usage
array = [1, 2, 3, 4, 5]
largest, second_largest = find_largest_and_second_largest(array)
print("Largest:", largest)              # Output: 5
print("Second Largest:", second_largest)  # Output: 4

array = [5, 5, 5]
largest, second_largest = find_largest_and_second_largest(array)
print("Largest:", largest)              # Output: 5
print("Second Largest:", second_largest)  # Output: None


