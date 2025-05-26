# 作者：liuyankai
# 时间：2025年05月27日00时16分08秒
# liuyankai23@mails.ucas.ac.cn
def merge(nums1, m, nums2, n) -> None:
    nums = [0] * (m + n)
    k = 0
    i = 0
    j = 0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            nums[k] = nums1[i]
            k = k + 1
            i = i + 1
        else:
            nums[k] = nums2[j]
            k = k + 1
            j = j + 1
    while i<m:
        nums[k] = nums1[i]
        k = k + 1
        i = i + 1
    while j<n:
        nums[k] = nums2[j]
        k = k + 1
        j = j + 1
    for pos in range(0, m + n):
        nums1[pos] = nums[pos]
    print(nums1)


if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    # nums1 = []
    # m = 0
    # nums2 = [1]
    # n = 1
    merge(nums1, m, nums2, n)
