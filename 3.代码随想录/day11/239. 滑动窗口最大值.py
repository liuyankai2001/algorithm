# 作者：liuyankai
# 时间：2025年06月08日13时05分37秒
# liuyankai23@mails.ucas.ac.cn
class Queue:
    def __init__(self):
        self.arr = []

    def add(self, x):
        while len(self.arr) > 0 and self.arr[0] < x:
            self.arr.pop(0)
        self.arr.append(x)

    def delete(self, x):
        if self.arr[0] == x:
            self.arr.pop(0)
        while len(self.arr) > 1 and self.arr[0] < self.arr[1]:
            self.arr.pop(0)

    def get_max(self):
        return self.arr[0]

    def pop_item(self):
        self.arr.pop(0)

    def smax(self):
        return self.arr[self.k-1]


def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    ans = []
    queue = Queue()
    i = 0
    j = 0
    while j < len(nums):
        queue.add(nums[j])
        if j - i >= k:
            queue.delete(nums[i])
            i += 1
        if j-i+1>=k:
            ans.append(queue.get_max())

        j += 1
    return ans

if __name__ == '__main__':
    nums = [9,10,9,-7,-4,-8,2,-6]
    k = 5
    print(maxSlidingWindow(nums, k))