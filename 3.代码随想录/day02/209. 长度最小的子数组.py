

def minSubArrayLen(target, nums):
    min_len = 0x3f3f3f3f
    sum = 0
    i = 0
    for j in range(0, len(nums)):
        sum += nums[j]
        while sum >= target:
            cur_len = j - i + 1
            min_len = min(min_len, cur_len)
            sum -= nums[i]
            i += 1

    return min_len if min_len != 0x3f3f3f3f else 0

if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    # target = 11
    # nums = [1, 1, 1, 1, 1, 1, 1, 1]
    k = minSubArrayLen(target, nums)
    print(k)