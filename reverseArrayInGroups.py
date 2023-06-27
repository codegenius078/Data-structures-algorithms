def reverse_in_groups(arr, n, k):
    i = 0
    while i < n:
        l = i
        r = min(i + k - 1, n - 1)
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        i += k


list1 = [1, 2, 3, 4, 5]
reverse_in_groups(list1, len(list1), 3)
print(list1)
