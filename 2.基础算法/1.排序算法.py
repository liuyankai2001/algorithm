import random


class Sort:
    def __init__(self, arr_num, arr_range):
        self.arr = []
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
        pass

    # 选择排序
    def select_sort(self):
        pass

    # 插入排序
    def insert_sort(self):
        pass

    # 希尔排序
    def shell_sort(self):
        pass

    # 快速排序
    def partition(self, left, right):
        pass

    def quick_sort(self, left, right):
        pass


if __name__ == '__main__':
    s = Sort(10, 100)
    print(s.arr)
