# merge sort algorithm
def merge(left, right):
    merged = []

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    left_tail = left[i:]
    right_tail = right[j:]

    return merged + left_tail + right_tail


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = nums[mid:]
    right = nums[:mid]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    sorted_list = merge(left_sorted, right_sorted)

    return sorted_list


print(merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
