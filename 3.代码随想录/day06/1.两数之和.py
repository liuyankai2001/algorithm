# 作者：liuyankai
# 时间：2025年06月02日15时11分57秒
# liuyankai23@mails.ucas.ac.cn
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hash_map = {}
    for i in range(len(nums)):
        if hash_map.get(nums[i]):
            hash_map[nums[i]].append(i)
        else:
            hash_map[nums[i]] = [i]
    for k in hash_map.keys():
        key = target - k
        if key == k:
            if len(hash_map.get(key)) > 1:
                return hash_map.get(key)
            else:
                continue
        res = hash_map.get(key, -1)
        if res == -1:
            continue
        else:
            second = res[0]
            first = hash_map.get(k)[0]
            return [first, second]

if __name__ == '__main__':
    nums = [2,4,11,3]
    target = 6
    print(twoSum(nums, target))
