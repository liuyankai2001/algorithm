
def containsNearbyDuplicate(nums, k: int) -> bool:
    d = dict()
    for i in range(0 ,len(nums)):
        if d.get(nums[i]) is None:
            d[nums[i]] =[i]
        else:
            d[nums[i]].append(i)
    di = list(d.values())
    for l in di:
        for i in range(len(l )-1 ,0,-1):
            l[i] = abs(l[i ] -l[ i -1])
    for l in di:
        for i in range(1,len(l)):
            if l[i]<= k:
                return True
    return False

if __name__ == '__main__':
    nums = [1,2,3,1,2,3]
    k = 2
    res = containsNearbyDuplicate(nums,k)
    print(res)