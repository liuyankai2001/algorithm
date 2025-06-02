# 作者：liuyankai
# 时间：2025年06月02日23时15分04秒
# liuyankai23@mails.ucas.ac.cn
def threeSum(nums):
    import copy
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    di = {}
    for i in range(len(nums)):
        if di.get(nums[i]):
            di[nums[i]].append(i)
        else:
            di[nums[i]] = [i]
    ans = []
    for i in range(len(nums)):
        di_copy = copy.deepcopy(di)
        res = [nums[i]]
        sum = nums[i]
        di_copy[nums[i]].remove(i)
        for j in range(len(nums)):
            if i == j:
                continue

            res.append(nums[j])
            sum += nums[j]
            di_copy[nums[j]].remove(j)

            find = di_copy.get(0 - sum, None)
            if find is None or len(find) == 0:
                continue
            for k in find:
                res1 = copy.deepcopy(res)
                res1.append(nums[k])
                ans.append(res1)
    return ans


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    ans = threeSum(nums)
    print(ans)