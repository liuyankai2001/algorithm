# 作者：liuyankai
# 时间：2025年05月29日20时03分28秒
# liuyankai23@mails.ucas.ac.cn
import sys

def main():
    num = int(int(sys.stdin.readline()))
    arr = [int(int(sys.stdin.readline())) for i in range(num)]

    arr1 = arr.copy()
    for i in range(1,num):
        arr1[i] += arr1[i-1]


    for line in sys.stdin:
        a, b = map(int, line.strip().split())
        print(arr1[b]-arr1[a]+arr[a])

if __name__ == '__main__':
    main()