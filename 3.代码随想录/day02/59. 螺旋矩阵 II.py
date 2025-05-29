# 作者：liuyankai
# 时间：2025年05月29日19时23分25秒
# liuyankai23@mails.ucas.ac.cn
def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    arr = [[0 for h in range(0,n)] for i in range(0,n)]

    i = 0
    j = 0
    this_num = 1
    while this_num <=n*n:
        while j<n and arr[i][j]==0:
            arr[i][j] = this_num
            j+=1
            this_num+=1
        j-=1
        i+=1
        while i<n and arr[i][j]==0:
            arr[i][j] = this_num
            i += 1
            this_num += 1
        i-=1
        j-=1
        while j>=0 and arr[i][j]==0:
            arr[i][j] = this_num
            j -= 1
            this_num += 1
        j+=1
        i-=1
        while i>=0 and arr[i][j]==0:
            arr[i][j] = this_num
            i -= 1
            this_num += 1
        i+=1
        j+=1
    return arr

if __name__ == '__main__':
    n = 3
    res = generateMatrix(n)
    print(res)