def sortedSquares(nums):
    nums1 = []
    nums2 = []
    for i in nums:
        if i < 0:
            nums1.append(i * i)
        else:
            nums2.append(i * i)
    len1 = len(nums1)
    len2 = len(nums2)
    i = len1 - 1
    j = 0
    k = 0
    while i >= 0 and j < len2:
        if nums1[i] < nums2[j]:
            nums[k] = nums1[i]
            k += 1
            i -= 1
        else:
            nums[k] = nums2[j]
            k += 1
            j += 1
    while i >= 0:
        nums[k] = nums1[i]
        k += 1
        i -= 1
    while j < len2:
        nums[k] = nums2[j]
        k += 1
        j += 1
    return nums

if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    nums = sortedSquares(nums)
    print(nums)