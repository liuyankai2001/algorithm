# 作者：liuyankai
# 时间：2025年05月24日21时20分30秒
# liuyankai23@mails.ucas.ac.cn
class BSearch:
    def __init__(self):
        self.arr = [12, 31, 41, 45, 47, 54, 61, 77, 87, 90]
        self.arr_len = 10

    def binary_search(self, target):
        arr = self.arr
        low = 0
        high = self.arr_len - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

if __name__ == '__main__':
    b = BSearch()
    target = 61
    print(b.arr)
    pos = b.binary_search(target)
    print(f"target 的位置是{pos}") if pos >=0 else print(f"target is not in arr")