def binary_search(arr, low, high, k):
    low = low
    high = high
    mid = (low + high) // 2
    if k not in arr:
        return -1

    if k == arr[mid]:
        return mid
    elif k < arr[mid]:
        return binary_search(arr, low, mid-1, k)
    else:
        return binary_search(arr, mid+1, high, k)

    return -1


list1 = [x for x in range(2, 101)]
print(binary_search(list1, 0, len(list1), 1))
