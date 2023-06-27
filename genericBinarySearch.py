# Generic binary search algorithm

def condition(data, target, mid):
    mid_number = data[mid]
    if mid_number == target:
        if data[mid-1] >= 0 and data[mid-1] == target:
            return "left"
        else:
            return "found"
    elif mid_number < target:
        return "left"
    else:
        return "right"

def binary_search(data, target):
    low = 0
    high = len(data)
    
    while low < high:
        mid = (low + high) // 2
        result = condition(data, target, mid)
        
        if result == "found":
            return mid
        elif result == "left":
            high = mid - 1
        elif result == "right":
            low = mid + 1
            
    return -1

data = [9,8,7,6,5,4,3,3,3,2,1]
target = 3
print(binary_search(data, target))
