# 作者：liuyankai
# 时间：2025年05月29日20时17分26秒
# liuyankai23@mails.ucas.ac.cn
import copy
import sys


def main():
    res = 0x3f3f3f3f
    n, m = map(int, input().strip().split())
    arr = []
    for i in range(n):
        arr_line = list(map(int, input().strip().split()))
        arr.append(arr_line.copy())

    if m > 1:
        arr1 = copy.deepcopy(arr)
        # 竖着切
        for li in arr1:
            for i in range(1, len(li)):
                li[i] += li[i - 1]
        for col in range(1, m):
            a = 0
            b = 0
            for i in range(0, n):
                a += arr1[i][col - 1]
                b += (arr1[i][m - 1] - arr1[i][col - 1])
                res = min(res, abs(a - b))

    if n > 1:
        arr1 = copy.deepcopy(arr)
        # 横着切
        for j in range(m):
            for i in range(1, n):
                arr1[i][j] += arr1[i - 1][j]
        for row in range(1, n):
            a = 0
            b = 0
            for i in range(0, n):
                a += arr1[row - 1][i]
                b += (arr1[m - 1][i] - arr1[row - 1][i])
                res = min(res, abs(a - b))
    print(res)



if __name__ == '__main__':
    main()