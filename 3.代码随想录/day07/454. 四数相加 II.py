# 作者：liuyankai
# 时间：2025年06月02日16时45分44秒
# liuyankai23@mails.ucas.ac.cn
def fourSumCount(nums1, nums2, nums3, nums4):
    ans = 0
    d1 = {}
    d2 = {}
    d3 = {}
    d4 = {}
    for i in range(len(nums1)):
        if d1.get(nums1[i]):
            d1[nums1[i]] += 1
        else:
            d1[nums1[i]] = 1

    for i in range(len(nums2)):
        if d2.get(nums2[i]):
            d2[nums2[i]] += 1
        else:
            d2[nums2[i]] = 1

    for i in range(len(nums3)):
        if d3.get(nums3[i]):
            d3[nums3[i]] += 1
        else:
            d3[nums3[i]] = 1

    for i in range(len(nums4)):
        if d4.get(nums4[i]):
            d4[nums4[i]] += 1
        else:
            d4[nums4[i]] = 1

    for i in d1.keys():
        res = i
        for j in d2.keys():
            res =i+j
            for k in d3.keys():
                res =i+j+k
                find_d4 = d4.get(0 - res,None)
                if find_d4:
                    ans = ans + d1.get(i) * d2.get(j) * d3.get(k) * find_d4
                    print(i,j,k,0-res)
    return ans

if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    print(fourSumCount(nums1, nums2, nums3, nums4))