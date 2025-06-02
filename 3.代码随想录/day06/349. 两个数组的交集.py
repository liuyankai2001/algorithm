# 作者：liuyankai
# 时间：2025年06月02日14时17分34秒
# liuyankai23@mails.ucas.ac.cn
def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    set1 = set(nums1)
    set2 = set(nums2)
    return set1 & set2


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(intersection(nums1,nums2))