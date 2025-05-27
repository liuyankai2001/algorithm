# 作者：liuyankai
# 时间：2025年05月27日21时46分14秒
# liuyankai23@mails.ucas.ac.cn
def productExceptSelf(nums):
    pre_nums = nums.copy()
    rear_nums = nums.copy()
    length = len(nums)
    for i in range(1,length):
        pre_nums[i] = pre_nums[i]*pre_nums[i-1]
    for i in range(length-2,-1,-1):
        rear_nums[i] =  rear_nums[i]*rear_nums[i+1]
    answer = [0]*length
    answer[0] = rear_nums[1]
    answer[length-1] = pre_nums[length-2]
    for i in range(1,length-1):
        answer[i] = pre_nums[i-1]* rear_nums[i+1]
    return answer

if __name__ == '__main__':
    nums = [1, 2]
    # nums = [-1,1,0,-3,3]
    answer = productExceptSelf(nums)
    print(answer)