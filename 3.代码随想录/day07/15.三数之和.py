# 作者：liuyankai
# 时间：2025年06月02日23时15分04秒
# liuyankai23@mails.ucas.ac.cn
def threeSum(nums):
    import copy
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    ans = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if (nums[i] + nums[left] + nums[right]) > 0:
                right -= 1
            elif (nums[i] + nums[left] + nums[right]) < 0:
                left += 1
            else:
                ans.append([nums[i], nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return ans


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    ans = threeSum(nums)
    print(ans)