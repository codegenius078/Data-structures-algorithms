# ternary search algorithm

def ternary_search(data, target):
    l = 0
    r = len(data)-1
    
    while r >= l:
        mid1 = l + (r-l) // 3
        mid2 = r - (r-l) // 3
        
        if target == data[mid1]:
            return True
        if target == data[mid2]:
            return True
        
        if target < mid1:
            r = mid1 - 1
        elif target > data[mid2]:
            l = mid2 + 1
        else:
            l = mid1 + 1
            r = mid2 - 1
            
    return False


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
print(ternary_search(data, target))
