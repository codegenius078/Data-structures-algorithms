def first_element_k_times(arr, k):
    hold_counts = dict()
    first_occurence = 0

    for i in range(len(arr)):
        if arr[i] in hold_counts:
            hold_counts[arr[i]] += 1
        else:
            hold_counts[arr[i]] = 1

        for j in hold_counts:
            if hold_counts[j] == k:
                first_occurence = j

    if first_occurence != 0:
        return first_occurence

    return -1


list1 = [1, 7, 4, 3, 4, 8, 7]
print(first_element_k_times(list1, 2))
