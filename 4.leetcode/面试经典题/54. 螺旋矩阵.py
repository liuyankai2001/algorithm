# 作者：liuyankai
# 时间：2025年06月02日22时34分31秒
# liuyankai23@mails.ucas.ac.cn
def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    res = []
    m = len(matrix)
    n = len(matrix[0])
    num = 1
    i = 0
    j = 0
    while num <= m * n:
        while j < n and matrix[i][j] != 0:
            res.append(matrix[i][j])
            matrix[i][j] = 0
            j += 1
            num += 1
        i += 1
        j -= 1
        while i < m and matrix[i][j] != 0:
            res.append(matrix[i][j])
            matrix[i][j] = 0
            i += 1
            num += 1
        i -= 1
        j -= 1
        while j >= 0 and matrix[i][j] != 0:
            res.append(matrix[i][j])
            matrix[i][j] = 0
            j -= 1
            num += 1
        j += 1
        i -= 1
        while i >= 0 and matrix[i][j] != 0:
            res.append(matrix[i][j])
            matrix[i][j] = 0
            i -= 1
            num += 1
        i += 1
        j += 1
    return res

if __name__ == '__main__':
    matrix = [[2,5],[8,4],[0,-1]]
    res = spiralOrder(matrix)
    print(res)