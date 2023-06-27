# linear search algorithm

def linear_search(data, target):
    for i in data:
        if i == target:
            return True
        
    return False


data = [1,2,3,4,5,6,7,8,9]
target = 10
print(linear_search(data, target))
