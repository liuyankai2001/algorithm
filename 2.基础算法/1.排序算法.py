import random


class Sort:
    def __init__(self, arr_num, arr_range):
        self.arr = []
        # self.arr = [3,87,2,93,78,56,61,38,12,40]
        self.arr_num = arr_num
        self.arr_range = arr_range
        self._create_arr()

    def _create_arr(self):
        self.arr.clear()
        for i in range(self.arr_num):
            new_data = random.randint(0, self.arr_range)
            self.arr.append(new_data)

    # 冒泡排序
    def bubble_sort(self):
        arr = self.arr
        for i in range(self.arr_num - 1, 0, -1):
            for j in range(0, i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # 选择排序
    def select_sort(self):
        arr = self.arr
        for i in range(0, self.arr_num - 1):
            minpos = i
            for j in range(i, self.arr_num):
                if arr[minpos] > arr[j]:
                    minpos = j
            arr[minpos], arr[i] = arr[i], arr[minpos]

    # 插入排序
    def insert_sort(self):
        arr = self.arr
        for i in range(1, self.arr_num):
            num = arr[i]
            j = i
            while j > 0:
                if arr[j - 1] > num:
                    arr[j] = arr[j - 1]
                else:
                    break
                j = j - 1
            arr[j] = num

    # 希尔排序
    def shell_sort(self):
        arr = self.arr
        gap = self.arr_num >> 1
        while gap > 0:
            for i in range(gap, self.arr_num):
                num = arr[i]
                j = i
                while j > 0:
                    if arr[j - gap] > num:
                        arr[j] = arr[j - gap]
                    else:
                        break
                    j = j - gap
                arr[j] = num
            gap = gap >> 1

    # 快速排序
    def partition(self, left, right):
        arr = self.arr
        k = left
        for i in range(left, right):
            if arr[i] < arr[right]:
                arr[k], arr[i] = arr[i], arr[k]
                k += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def quick_sort(self, left, right):
        if left < right:
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)

    # 堆排序
    def adjust(self, node_pos, arr_len):
        arr = self.arr
        dad = node_pos
        son = dad * 2 + 1
        while son <= arr_len:
            son = son + 1 if son + 1 <= arr_len and arr[son] < arr[son + 1] else son
            if arr[dad] < arr[son]:
                arr[dad], arr[son] = arr[son], arr[dad]
                dad = son
                son = dad * 2 + 1
            else:
                break

    def heap_sort(self):
        arr = self.arr
        arr_len = self.arr_num
        for node_pos in range((arr_len - 1) // 2 - 1, -1, -1):
            self.adjust(node_pos, arr_len - 1)
        for pos in range(arr_len - 1, 0, -1):
            arr[0], arr[pos] = arr[pos], arr[0]
            self.adjust(0, pos - 1)

    # 归并排序
    def merge(self, left, mid, right):
        arr = self.arr
        arr_b = arr.copy()
        i = left
        j = mid + 1
        k = left
        while i<=mid and j<=right:
            if arr[i]< arr[j]:
                arr_b[k] = arr[i]
                k+=1
                i+=1
            else:
                arr_b[k] = arr[j]
                k += 1
                j += 1
        while i<=mid:
            arr_b[k] = arr[i]
            k += 1
            i += 1
        while j<=right:
            arr_b[k] = arr[j]
            k += 1
            j += 1
        for pos in range(left,right+1):
            arr[pos] = arr_b[pos]

    def merge_sort(self, left, right):
        if left < right:
            mid = (left + right) >> 1
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            self.merge(left, mid, right)


if __name__ == '__main__':
    s = Sort(10, 100)
    print(s.arr)
    # s.bubble_sort()
    # s.select_sort()
    # s.insert_sort()
    # s.shell_sort()
    # s.quick_sort(0,9)
    # s.heap_sort()
    s.merge_sort(0,9)
    print(s.arr)
