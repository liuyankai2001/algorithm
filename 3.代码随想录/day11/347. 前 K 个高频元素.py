# 作者：liuyankai
# 时间：2025年06月08日18时00分29秒
# liuyankai23@mails.ucas.ac.cn
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    di = {}
    for i in nums:
        if di.get(i):
            di[i] += 1
        else:
            di[i] = 1
    di_items = di.items()
    res = sorted(di_items, key=lambda x: x[1], reverse=True)
    ans = []
    for i in res:
        ans.append(i[0])
        if len(ans) == k:
            return ans

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(topKFrequent(nums, k))