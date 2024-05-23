# 2. to check weathwer the array is sorted or not:-
def sorted(arr):
    for num in range (len(arr)-1):
        if arr[num]>arr[num+1]:
            return False
        return True
array=[12,32,34,54,56,58]  
print(sorted(array))  