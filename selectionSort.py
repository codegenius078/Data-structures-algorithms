# selection sort algorithm

def selection_sort(data):
    minimum = data[0]
    
    for i in range(len(data)):
        for j in range(len(data)-1):
            if minimum > data[j+1]:
                minimum = data[j+1]
        minimum, data[j+1] = data[j+1], minimum
                
        
        
data = [5,4,3,2,1]
selection_sort(data)
print(data)
    