# 作者：liuyankai
# 时间：2025年05月27日00时37分53秒
# liuyankai23@mails.ucas.ac.cn
def removeElement(nums, val):
    num_len = len(nums)
    j = num_len-1
    i = 0
    while j>=0 and nums[j]==val:
        j = j-1
    if j == -1:
        return 0
    while i < j:
        if nums[i]==val:
            nums[i],nums[j] = nums[j],nums[i]
            j = j-1
            while j >= 0 and nums[j] == val:
                j = j - 1
        i+=1
    for k in range(0, len(nums)):
        if nums[k]==val:
            return k

if __name__ == '__main__':
    # nums = [3, 2, 2, 3]
    # val = 3
    # nums = [0, 1, 2, 2, 3, 0, 4, 2]
    # val = 2
    nums = [4,2,0,2,2,1,4,4,1,4,3,2]
    val = 4
    k = removeElement(nums,val)
    print(k)