# bubble sort algorithm

def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    

data = [5,4,3,2,1]
bubble_sort(data)
print(data)