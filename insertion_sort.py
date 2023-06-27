# insertion sort algorithm

def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i - 1
        while j >= 0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums


list1 = [6, 5, 4, 3, 2, 1]
print(insertion_sort(list1))
