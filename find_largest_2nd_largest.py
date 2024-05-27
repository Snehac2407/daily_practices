def find_largest_and_sec_largest(arr):
    if len(arr) < 2:
        return None
    largest = sec_largest = 0
    for num in arr:
        if num > largest:
            sec_largest = largest
            largest = num
        elif num > sec_largest and num != largest:
            sec_largest = num

    return largest, sec_largest

# Example usage
arr = []
largest, sec_largest = find_largest_and_sec_largest(arr)
print(f"Largest: {largest}, sec Largest: {sec_largest}")
# Output: Largest: 5, sec Largest: 4
